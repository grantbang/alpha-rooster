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
from pydantic import BaseModel
from dotenv import load_dotenv
from urllib.parse import urlencode
from datetime import datetime

# Import BigQuery client
from app.bigquery_client import insert_user_event, validate_connection

# Import offer configuration
from app.offer_config import get_offer_config, build_maxbounty_url

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

# Root endpoint - Landing page with Facebook domain verification
@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """
    Root landing page. Uses base.html template which includes Facebook domain verification meta tag.
    This page serves as a simple landing until the full game flow is built.
    """
    logger.info("Root endpoint accessed")
    return templates.TemplateResponse("home.html", {
        "request": request
    })

# Privacy Policy
@app.get("/privacy", response_class=HTMLResponse)
async def privacy_policy(request: Request):
    """Render privacy policy page."""
    return templates.TemplateResponse("privacy.html", {"request": request, "pixel_id": os.getenv("META_PIXEL_ID", "")})

# Terms of Service
@app.get("/terms", response_class=HTMLResponse)
async def terms_of_service(request: Request):
    """Render terms of service page."""
    return templates.TemplateResponse("terms.html", {"request": request, "pixel_id": os.getenv("META_PIXEL_ID", "")})

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

@app.get("/lander", response_class=HTMLResponse)
async def get_lander(request: Request, fbclid: str | None = None):
    """
    Render the direct-response landing page (no game, form-first).
    Logs lander_load event to BigQuery.

    Args:
        fbclid: Optional Facebook click id auto-appended by FB ads
    """
    logger.info(f"/lander GET accessed fbclid={fbclid}")

    try:
        event_id = str(uuid.uuid4())
        insert_user_event(
            event_id=event_id,
            event_type="lander_load",
            fbclid=fbclid,
            variant_id="lander_v1",
            user_agent=request.headers.get("user-agent")
        )
    except Exception as e:
        logger.error(f"BigQuery insert failed for lander_load: {e}")

    return templates.TemplateResponse("lander.html", {
        "request": request,
        "fbclid": fbclid or "",
        "event_id": event_id,
        "pixel_id": os.getenv("META_PIXEL_ID", ""),
    })


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
        "fbclid": fbclid or "",
        "event_id": event_id,
        "pixel_id": os.getenv("META_PIXEL_ID", ""),
    })


class GameSubmitRequest(BaseModel):
    event_id: str
    fbclid: str = ""
    first_name: str
    last_name: str
    email: str


class LanderSubmitRequest(BaseModel):
    event_id: str
    fbclid: str = ""
    first_name: str
    last_name: str
    email: str


@app.post("/lander/submit")
async def post_lander_submit(payload: LanderSubmitRequest):
    """
    Log name/email capture from lander page to BigQuery.
    Called via fetch() just before redirect to Champion with prepop.

    Args:
        payload: JSON body with event_id, fbclid, first_name, last_name, email

    Returns:
        dict: {"status": "ok"}
    """
    logger.info(f"📝 Lander submit: event_id={payload.event_id} email={payload.email}")

    try:
        insert_user_event(
            event_id=payload.event_id,
            event_type="lander_submit",
            fbclid=payload.fbclid or None,
            variant_id="lander_v1",
            user_agent=None
        )
        logger.info(f"✅ BigQuery lander_submit logged for event_id={payload.event_id} email={payload.email}")
    except Exception as e:
        logger.error(f"❌ BigQuery lander_submit failed: {e}")
        # Non-blocking — don't stop the redirect

    return {"status": "ok"}


@app.post("/game/submit")
async def post_game_submit(payload: GameSubmitRequest):
    """
    Log name/email capture from game page to BigQuery.
    Called via fetch() just before redirect to Champion with prepop.

    Args:
        payload: JSON body with event_id, fbclid, first_name, last_name, email

    Returns:
        dict: {"status": "ok"}
    """
    logger.info(f"📝 Game submit: event_id={payload.event_id} email={payload.email}")

    try:
        insert_user_event(
            event_id=payload.event_id,
            event_type="game_submit",
            fbclid=payload.fbclid or None,
            variant_id="champion-auto",
            user_agent=None
        )
        logger.info(f"✅ BigQuery game_submit logged for event_id={payload.event_id} email={payload.email}")
    except Exception as e:
        logger.error(f"❌ BigQuery game_submit failed: {e}")
        # Non-blocking — don't stop the redirect

    return {"status": "ok"}


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
    
    # Phase 4.2: Send conversion event to Facebook CAPI
    # This closes the attribution loop and improves ad performance
    try:
        from app.facebook_capi import send_conversion_event
        
        # Lookup fbclid from original event (stored in user_events table)
        # For now we'll use event_id as fbclid since they match in our flow
        # TODO: Query BigQuery user_events to get actual fbclid if needed
        
        send_conversion_event(
            event_id=subId1,
            fbclid=subId1,  # In our flow, event_id IS the fbclid from the click
            payout=payout,
            user_agent=request.headers.get("user-agent"),
            client_ip=request.client.host if request.client else None
        )
        logger.info(f"📡 CAPI conversion event sent for {subId1}")
        
    except Exception as e:
        logger.error(f"❌ CAPI event failed: {e}")
        # Don't fail the postback - MaxBounty needs 200 response
    
    return {
        "status": "success",
        "event_id": subId1,
        "payout": payout,
        "message": "Conversion tracked"
    }

# ============================================================
# NEW: Dynamic Offer-Specific Qualification Routes
# ============================================================

@app.get("/qualify/{offer_slug}", response_class=HTMLResponse)
async def get_qualify_offer(request: Request, offer_slug: str, fbclid: str | None = None):
    """
    Render offer-specific pre-qualifier form.
    Dynamic route: /qualify/champion-auto, /qualify/champion-home, etc.
    
    Args:
        offer_slug: Offer identifier (e.g., "champion-auto")
        fbclid: Facebook click ID from ad URL parameters
    
    Returns:
        HTMLResponse: Pre-qualifier form or 404 if offer not found
    """
    logger.info(f"/qualify/{offer_slug} GET accessed fbclid={fbclid}")
    
    # Get offer configuration
    offer_config = get_offer_config(offer_slug)
    if not offer_config:
        logger.warning(f"Offer not found or inactive: {offer_slug}")
        raise HTTPException(status_code=404, detail="Offer not found")
    
    # Generate event ID for tracking
    event_id = str(uuid.uuid4())
    
    # Log page view to BigQuery
    try:
        insert_user_event(
            event_id=event_id,
            event_type="qualify_page_view",
            fbclid=fbclid,
            variant_id=offer_slug,
            user_agent=request.headers.get("user-agent")
        )
    except Exception as e:
        logger.error(f"BigQuery insert failed for qualify_page_view: {e}")
    
    # Render qualify_offer.html template with orange branding
    return templates.TemplateResponse("qualify_offer.html", {
        "request": request,
        "offer_slug": offer_slug,
        "offer_name": offer_config["name"],
        "fbclid": fbclid or "",
        "event_id": event_id,
        "pixel_id": os.getenv("META_PIXEL_ID", "")
    })


@app.post("/qualify/{offer_slug}/submit")
async def post_qualify_offer(
    request: Request,
    offer_slug: str,
    fbclid: str = Form(""),
    event_id: str = Form(...)
):
    """
    Simple redirect to MaxBounty - no form collection.
    User just clicks button, we track the click, redirect to MaxBounty's funnel.
    
    Args:
        offer_slug: Offer identifier
        fbclid: Facebook click ID (hidden field)
        event_id: Unique event ID (hidden field)
    
    Returns:
        RedirectResponse: To MaxBounty offer
    """
    logger.info(f"/qualify/{offer_slug}/submit POST - redirecting to MaxBounty")
    
    # Get offer configuration
    offer_config = get_offer_config(offer_slug)
    if not offer_config:
        raise HTTPException(status_code=404, detail="Offer not found")
    
    # Store click event in BigQuery
    try:
        insert_user_event(
            event_id=event_id,
            event_type="qualify_submit",
            fbclid=fbclid or None,
            variant_id=offer_slug,
            user_agent=request.headers.get("user-agent")
        )
        logger.info(f"✅ Stored click for event_id={event_id}")
    except Exception as e:
        logger.error(f"❌ BigQuery insert failed: {e}")
        # Don't block redirect if BigQuery fails
    
    # Build MaxBounty redirect URL (no prepop, just tracking)
    redirect_url = build_maxbounty_url(offer_config, event_id, {}, fbclid)
    
    logger.info(f"🚀 Redirecting to MaxBounty: {redirect_url[:100]}...")
    
    # Redirect to MaxBounty offer
    return RedirectResponse(url=redirect_url, status_code=302)

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Alpha Rooster server...")
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
