"""
Alpha Rooster - Main FastAPI Application
Phase 3.1: Basic Setup
"""

import os
import logging
from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from urllib.parse import urlencode

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
    """
    logger.info(f"/qualify GET accessed fbclid={fbclid}")
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
    
    Args:
        fbclid: Optional Facebook click id (preserved from /qualify)
    """
    logger.info(f"/game GET accessed fbclid={fbclid}")
    return templates.TemplateResponse("game.html", {
        "request": request,
        "fbclid": fbclid or "demo",
        "pixel_id": os.getenv("META_PIXEL_ID", ""),
    })

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Alpha Rooster server...")
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
