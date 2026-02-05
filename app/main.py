"""
Alpha Rooster - Main FastAPI Application
Phase 3.5: BigQuery Integration
"""

import os
import logging
import uuid
from fastapi import FastAPI, Request, Form, HTTPException, Query
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from urllib.parse import urlencode
from datetime import datetime

# Import BigQuery client
from app.bigquery_client import insert_user_event, validate_connection

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Alpha Rooster",
    description="Social-to-CPA Game Engine",
    version="10.0"
)

# Startup event - validate BigQuery connection
@app.on_event("startup")
async def startup_event():
    """Validate BigQuery connection on app startup."""
    logger.info("🚀 Starting Alpha Rooster application...")
    try:
        if validate_connection():
            logger.info("✅ BigQuery connection validated")
        else:
            logger.warning("⚠️  BigQuery connection validation failed")
    except Exception as e:
        logger.error(f"❌ BigQuery connection error: {e}")

# Mount static files (CSS, JS, images)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup Jinja2 templates
templates = Jinja2Templates(directory="app/templates")

# Root endpoint - Test that server is running
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """
    Test endpoint to verify FastAPI is working.
    """
    logger.info("Root endpoint accessed")
    return """
    <html>
        <head>
            <title>Alpha Rooster - Server Running</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 50px auto;
                    padding: 20px;
                    text-align: center;
                }
                h1 { color: #2ecc71; }
                .status { 
                    background: #ecf0f1; 
                    padding: 20px; 
                    border-radius: 8px;
                    margin: 20px 0;
                }
                code {
                    background: #34495e;
                    color: #ecf0f1;
                    padding: 2px 6px;
                    border-radius: 3px;
                }
            </style>
        </head>
        <body>
            <h1>✅ Alpha Rooster Server Running!</h1>
            <div class="status">
                <h2>Phase 3.1: Local Development Setup</h2>
                <p><strong>Status:</strong> Server is operational</p>
                <p><strong>Next:</strong> Build pre-qualifier form (Phase 3.2)</p>
            </div>
            <div class="status">
                <h3>Quick Test:</h3>
                <p>If you can see this page, your FastAPI server is working correctly.</p>
                <p>Access at: <code>http://localhost:8080</code></p>
            </div>
        </body>
    </html>
    """

# Health check endpoint
@app.get("/health")
async def health_check():
    """
    Health check endpoint for monitoring.
    Returns server status and configuration info.
    """
    return {
        "status": "healthy",
        "phase": "3.1",
        "message": "Alpha Rooster server operational"
    }

@app.get("/qualify", response_class=HTMLResponse)
async def get_qualify(request: Request, fbclid: str | None = None):
    """
    Render pre-qualifier form. Preserves fbclid if provided.
    Logs page_view event to BigQuery.
    """
    logger.info(f"/qualify GET accessed fbclid={fbclid}")
    
    # Log page view to BigQuery
    try:
        event_id = str(uuid.uuid4())
        insert_user_event(
            event_id=event_id,
            event_type="page_view",
            fbclid=fbclid,
            variant_id="qualify_v1",
            user_agent=request.headers.get("user-agent")
        )
    except Exception as e:
        # Don't block page load if BigQuery fails
        logger.error(f"BigQuery insert failed for page_view: {e}")
    
    return templates.TemplateResponse("qualify.html", {
        "request": request,
        "fbclid": fbclid,
        "error": None,
        "pixel_id": os.getenv("META_PIXEL_ID", ""),
    })

@app.post("/qualify")
async def post_qualify(
    request: Request,
    age_range: str = Form(...),
    state: str = Form(...),
    fbclid: str | None = Form(None),
):
    """
    Validate pre-qualifier inputs and redirect qualified users to /game.

    Args:
        age_range: "under_25" | "25_34" | "35_54" | "55_plus"
        state: Two-letter US state code
        fbclid: Optional Facebook click id to preserve
    Returns:
        RedirectResponse to /game with query params
    Raises:
        HTTPException: 400 on validation error
    """
    logger.info(f"/qualify POST age_range={age_range} state={state} fbclid={fbclid}")

    # Log qualify_submit event to BigQuery
    try:
        event_id = str(uuid.uuid4())
        insert_user_event(
            event_id=event_id,
            event_type="qualify_submit",
            fbclid=fbclid,
            variant_id="qualify_v1",
            user_agent=request.headers.get("user-agent")
        )
    except Exception as e:
        # Don't block form processing if BigQuery fails
        logger.error(f"BigQuery insert failed for qualify_submit: {e}")

    valid_states = {
        "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA","HI","ID","IL","IN","IA","KS","KY","LA","ME","MD","MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ","NM","NY","NC","ND","OH","OK","OR","PA","RI","SC","SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"
    }
    valid_ages = {"under_25","25_34","35_54","55_plus"}

    try:
        if age_range not in valid_ages:
            raise ValueError("Invalid age range")
        if state not in valid_states:
            raise ValueError("Invalid state")

        # Qualification rule: require age >= 25 (not under_25)
        qualified = age_range != "under_25"
        if not qualified:
            logger.info("User did not qualify (age under 25)")
            # Re-render with error message
            return templates.TemplateResponse("qualify.html", {
                "request": request,
                "fbclid": fbclid,
                "error": "Sorry, this offer requires age 25+.",
                "pixel_id": os.getenv("META_PIXEL_ID", ""),
            })

        # Preserve fbclid and route to game
        params = {"fbclid": fbclid} if fbclid else {}
        redirect_url = f"/game"
        if params:
            redirect_url = f"/game?{urlencode(params)}"
        logger.info(f"Qualified. Redirecting to {redirect_url}")
        return RedirectResponse(url=redirect_url, status_code=302)

    except ValueError as e:
        logger.error(f"Validation error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unexpected error in /qualify: {e}")
        raise HTTPException(status_code=500, detail="Internal error")

@app.get("/game", response_class=HTMLResponse)
async def get_game(request: Request, fbclid: str | None = None):
    """
    Render the spin wheel game. User plays to win their reward tier.
    Logs game_load event to BigQuery.
    
    Args:
        fbclid: Optional Facebook click id (preserved from /qualify)
    """
    logger.info(f"/game GET accessed fbclid={fbclid}")
    
    # Log game page load to BigQuery
    try:
        event_id = str(uuid.uuid4())
        insert_user_event(
            event_id=event_id,
            event_type="game_load",
            fbclid=fbclid,
            variant_id="wheel_v1",
            user_agent=request.headers.get("user-agent")
        )
    except Exception as e:
        # Don't block page load if BigQuery fails
        logger.error(f"BigQuery insert failed for game_load: {e}")
    
    return templates.TemplateResponse("game.html", {
        "request": request,
        "fbclid": fbclid or "demo",
        "pixel_id": os.getenv("META_PIXEL_ID", ""),
    })

# ============================================================================
# PHASE 4.1: POSTBACK ENDPOINT
# ============================================================================

@app.get("/postback")
async def maxbounty_postback(
    request: Request,
    subId1: str = Query(..., alias="subId1", description="Event ID from click"),
    payout: float = Query(..., description="Payout amount from MaxBounty"),
    secret: str = Query(..., description="Security token")
):
    """
    MaxBounty Postback Endpoint - Receives conversion notifications
    
    Called by MaxBounty when a user completes the insurance quote form.
    URL format: https://playtosave.net/postback?subId1=EVENT_ID&payout=6.75&secret=YOUR_SECRET
    
    Args:
        subId1: The event_id we passed in the tracking link (fbclid)
        payout: The payout amount (usually $6.75)
        secret: Security token to verify request is from MaxBounty
    
    Returns:
        dict: Success response with event_id
    
    Raises:
        HTTPException: If secret token is invalid
    """
    logger.info(f"📡 Postback received: event_id={subId1}, payout=${payout}")
    
    # Security: Verify secret token
    expected_secret = os.getenv("AFFILIATE_SECRET")
    if not expected_secret:
        logger.error("❌ AFFILIATE_SECRET not configured in environment")
        raise HTTPException(status_code=500, detail="Server configuration error")
    
    if secret != expected_secret:
        logger.warning(f"⚠️  Invalid secret token from IP: {request.client.host}")
        raise HTTPException(status_code=401, detail="Unauthorized")
    
    # Log conversion to BigQuery
    try:
        from app.bigquery_client import insert_conversion_signal
        
        conversion_data = {
            "event_id": subId1,
            "fbclid": None,  # Will be None for postback (we have it in user_events)
            "payout": payout,
            "offer_id": "29678",  # YourInsurancePath Auto Insurance
            "conversion_time": datetime.utcnow().isoformat(),
            "raw_postback": str(request.url)  # Store full URL for debugging
        }
        
        insert_conversion_signal(conversion_data)
        logger.info(f"✅ Conversion logged to BigQuery: {subId1}")
        
    except Exception as e:
        logger.error(f"❌ BigQuery insert failed for conversion: {e}")
        # Don't fail the postback - MaxBounty needs 200 response
    
    # TODO Phase 4.2: Send conversion event to Facebook CAPI
    # This will close the attribution loop and improve ad performance
    
    return {
        "status": "success",
        "event_id": subId1,
        "payout": payout,
        "message": "Conversion tracked"
    }

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Alpha Rooster server...")
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
