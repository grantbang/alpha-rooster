"""
Alpha Rooster - Main FastAPI Application
Phase 3.1: Basic Setup
"""

import os
import logging
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

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

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting Alpha Rooster server...")
    uvicorn.run(app, host="0.0.0.0", port=8080, log_level="info")
