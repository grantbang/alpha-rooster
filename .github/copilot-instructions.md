# GitHub Copilot Instructions for Alpha Rooster

## Project Context
This is **Alpha Rooster v10.0** - a social-to-CPA arbitrage system using Meta Ads + gamification + affiliate offers.

**Tech Stack:** Python 3.11, FastAPI, BigQuery, Meta Ads API, Cloud Run  
**Current Phase:** See `README.md` Part 3 for detailed build checklist  
**Documentation:** All specs in `README.md` (Parts 1-6)

---

## Core Rules (Always Enforce)

### 1. No Placeholder Code
- Every function must be **runnable immediately**
- Use real API connections (BigQuery, Meta CAPI, affiliate networks)
- No `TODO` comments, no `pass` statements, no mock data in production code
- If credentials needed, use `os.getenv()` with validation

**Example - FORBIDDEN:**
```python
def send_to_bigquery(data):
    # TODO: Implement later
    print("Would send:", data)
```

**Example - REQUIRED:**
```python
def send_to_bigquery(data):
    client = bigquery.Client(project=os.getenv("GCP_PROJECT_ID"))
    errors = client.insert_rows_json(table_id, [data])
    if errors:
        raise Exception(f"BigQuery error: {errors}")
```

### 2. Environment Variables Only
- **NEVER** hardcode: API keys, project IDs, pixel IDs, URLs
- **ALWAYS** use `.env` file with validation
- Add startup check that fails fast if vars missing

### 3. Comprehensive Error Handling
- Every external API call wrapped in try/except
- Log errors with `logging.error()` (not just print)
- Return meaningful error messages
- Include retry logic for transient failures (use `tenacity` library)

### 4. Logging Everywhere
```python
import logging
logging.basicConfig(level=logging.INFO)

# At start of every function:
logging.info(f"Function started with params: {param1}, {param2}")

# At critical points:
logging.info(f"BigQuery insert successful: {event_id}")

# On errors:
logging.error(f"CAPI failed for {event_id}: {str(e)}")
```

### 5. Type Hints & Docstrings
- All functions have type hints: `def func(param: str) -> dict:`
- All functions have docstrings explaining Args, Returns, Raises
- Use Google-style docstrings

---

## Phase-Based Development

**Current phase tracking:** User will specify in chat which phase they're on.

### Phase 1: Foundation (Setup only, minimal coding)
- Focus: Account creation, GCP setup, legal docs
- Code: Environment validation, config loading
- No game mechanics yet

### Phase 2: Creative Assets (No backend coding)
- Focus: Ad creative files, copy docs, tracking spreadsheet
- Code: None (asset organization only)

### Phase 3: Game App (Core development)
**Sub-phases:**
- 3.1: Local dev setup → Verify: `uvicorn app.main:app` runs
- 3.2: Pre-qualifier → Verify: Form submits, redirects work
- 3.3: Game engine → Verify: Wheel spins in browser, confetti shows
- 3.4: Meta Pixel → Verify: Events appear in Network tab
- 3.5: BigQuery → Verify: `SELECT *` shows inserted events
- 3.6: Deployment → Verify: Public URL responds

**Don't mix sub-phases.** Complete 3.1 before starting 3.2.

### Phase 4: Signal Loop
- 4.1: Postback endpoint → Verify: `curl` test returns 200
- 4.2: CAPI integration → Verify: Test Events shows event
- 4.3: Validation → Verify: Full flow works end-to-end

### Phase 5: Analytics
- Focus: BigQuery views, dashboards, alerts
- Verify: Can run queries and get results

### Phase 6: Launch
- Focus: Meta campaign setup, monitoring
- Verify: Ads running, clicks arriving

---

## Code Generation Standards

### FastAPI Routes
```python
@app.post("/endpoint")
async def endpoint_name(
    request: Request,
    param1: str,
    param2: float = None
) -> dict:
    """
    Brief description.
    
    Args:
        request: FastAPI Request object
        param1: Description
        param2: Optional description
    
    Returns:
        dict: {"status": "success", "data": {...}}
    
    Raises:
        HTTPException: If validation fails
    """
    logging.info(f"Endpoint called with: {param1}, {param2}")
    
    try:
        # Implementation
        result = do_something(param1)
        return {"status": "success", "data": result}
    except ValueError as e:
        logging.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal error")
```

### BigQuery Operations
```python
from google.cloud import bigquery
import os

client = bigquery.Client(project=os.getenv("GCP_PROJECT_ID"))

def insert_event(event_id: str, fbclid: str, variant_id: str) -> bool:
    """Insert game event to BigQuery."""
    table_id = f"{os.getenv('GCP_PROJECT_ID')}.{os.getenv('BIGQUERY_DATASET')}.game_events"
    
    row = {
        "event_id": event_id,
        "fbclid": fbclid,
        "variant_id": variant_id,
        "timestamp": datetime.utcnow().isoformat()
    }
    
    errors = client.insert_rows_json(table_id, [row])
    if errors:
        logging.error(f"BigQuery insert failed: {errors}")
        raise Exception(f"BigQuery error: {errors}")
    
    logging.info(f"Inserted event {event_id} to BigQuery")
    return True
```

### Meta CAPI Events
```python
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.user_data import UserData

FacebookAdsApi.init(access_token=os.getenv("META_ACCESS_TOKEN"))

def send_conversion_event(fbclid: str, event_id: str, payout: float) -> dict:
    """Send conversion event to Meta CAPI."""
    user_data = UserData(fbc=f"fb.1.{int(time.time())}.{fbclid}")
    
    event = Event(
        event_name="Purchase",
        event_time=int(time.time()),
        event_id=event_id,  # Deduplication
        user_data=user_data,
        custom_data={"value": payout, "currency": "USD"}
    )
    
    event_request = EventRequest(
        events=[event],
        pixel_id=os.getenv("META_PIXEL_ID")
    )
    
    response = event_request.execute()
    logging.info(f"CAPI response: {response}")
    return response
```

---

## Testing Requirements

### After generating ANY code:
1. **Provide test command:**
   ```bash
   # Example for testing route locally:
   uvicorn app.main:app --reload
   curl http://localhost:8080/endpoint
   ```

2. **Provide verification query (if applicable):**
   ```sql
   -- Verify BigQuery insert:
   SELECT * FROM rooster_data.game_events 
   ORDER BY timestamp DESC LIMIT 5
   ```

3. **Provide expected output:**
   ```json
   // Expected API response:
   {"status": "success", "event_id": "abc-123"}
   ```

### Test Checklist Template (include with every feature):
```markdown
## Testing [Feature Name]

### Local Test:
```bash
# Command to run:
[exact command]

# Expected output:
[show expected response]
```

### Verification:
- [ ] Runs without errors
- [ ] Logs appear in console
- [ ] Data appears in BigQuery/Meta (if applicable)
- [ ] Error handling works (test with invalid input)

### Edge Cases Tested:
- [ ] Missing parameters
- [ ] Invalid data types
- [ ] API unavailable (disconnect internet)
```

---

## Common Patterns

### Configuration Validation (add to main.py startup)
```python
REQUIRED_ENV_VARS = [
    "GCP_PROJECT_ID",
    "BIGQUERY_DATASET",
    "META_PIXEL_ID",
    "META_ACCESS_TOKEN",
    "AFFILIATE_SECRET"
]

for var in REQUIRED_ENV_VARS:
    value = os.getenv(var)
    if not value:
        raise EnvironmentError(f"Missing required env var: {var}")
    logging.info(f"✓ {var} loaded")
```

### Retry Logic (for API calls)
```python
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=10))
def call_external_api():
    # Will retry up to 3 times with exponential backoff
    response = requests.post(url, data=data)
    response.raise_for_status()
    return response.json()
```

### Structured Logging
```python
logging.info(f"Event processed", extra={
    "event_id": event_id,
    "variant_id": variant_id,
    "revenue": payout,
    "status": "success"
})
```

---

## File Organization

```
/alpha-rooster
  /app
    /templates          # Jinja2 HTML templates
      base.html
      qualify.html
      game.html
      privacy.html
      terms.html
    /static
      /css
        style.css       # Single CSS file (no frameworks)
      /js
        wheel.js        # Spin wheel game logic
        fraud.js        # Fraud detection
        pixel.js        # Meta Pixel helpers
    /routers           # FastAPI route modules (if app grows)
      game.py
      postback.py
    main.py            # Main FastAPI app
    config.py          # Configuration loading
    bigquery_client.py # BigQuery operations
    meta_capi.py       # Meta CAPI operations
  /tests               # Test files & proof screenshots
  .env                 # Environment variables (gitignored)
  .gitignore
  Dockerfile
  requirements.txt
  README.md
```

---

## What NOT to Suggest

❌ Don't suggest: "Let's use React for the frontend"  
✅ This project uses Jinja2 templates (server-side rendering, simpler)

❌ Don't suggest: "Let's add a database like PostgreSQL"  
✅ This project uses BigQuery (already chosen, Part 2.1)

❌ Don't suggest: "Let's build an admin dashboard"  
✅ Out of scope for v10.0 (use Google Data Studio, Part 5.3.2)

❌ Don't suggest: "Let's add user authentication"  
✅ No user accounts in this project (anonymous game players)

❌ Don't suggest: "Let's containerize with Kubernetes"  
✅ Cloud Run already handles containers (Part 3.6)

---

## Copilot Chat Usage

### Good prompts:
- "Build the /qualify route according to Phase 3.2 spec. Include form validation, BigQuery logging, and redirect logic."
- "Add error handling to the postback endpoint for missing fbclid scenario."
- "Generate BigQuery schema for game_events table from Part 2.2 spec."

### Bad prompts:
- "Make it better" (too vague)
- "Add features" (what features?)
- "Optimize this" (optimize for what?)

### When stuck:
- "What's the next task in Phase [X] according to README.md?"
- "How do I verify that [feature] is working?"
- "What environment variables are needed for [component]?"

---

## Deployment Checklist

Before suggesting deployment:
- [ ] All environment variables documented in `.env.example`
- [ ] Dockerfile builds successfully: `docker build -t test .`
- [ ] Local container runs: `docker run -p 8080:8080 --env-file .env test`
- [ ] All routes return 200 status on test
- [ ] No hardcoded credentials in code
- [ ] `.gitignore` includes `.env`, `credentials.json`, `venv/`

---

## Summary

**Golden Rule:** If you can't immediately test and verify it, don't suggest it.

**Reference docs:**
- Full project spec: `README.md` Parts 1-6
- Current phase: User specifies in chat
- Build checklist: `README.md` Part 3

**When in doubt:**
1. Check README.md for existing spec
2. Ask user which phase they're on
3. Provide runnable code with test instructions
4. Include error handling and logging
5. Suggest verification command
