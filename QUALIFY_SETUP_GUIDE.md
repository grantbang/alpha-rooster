# Quick Setup Guide: /qualify Routes

## What We Built

You now have a **dynamic multi-offer qualification system**:
- `/qualify/champion-auto` → Auto insurance offer
- `/qualify/champion-home` → Home insurance offer
- Add more offers easily by updating `offer_config.py`

---

## Files Created

### 1. `/Applications/alphaRooster/app/offer_config.py`
Centralized offer configuration. Each offer has:
- `name`: Display name
- `maxbounty_id`: Offer ID from MaxBounty
- `payout`: Commission per lead
- `redirect_url`: Your MaxBounty tracking link
- `prepop_format`: How to format prepop params
- `fields_required`: Form fields to capture
- `active`: Enable/disable offer

### 2. `/Applications/alphaRooster/app/templates/qualify_offer.html`
Beautiful, mobile-responsive qualification form with:
- Client-side validation
- Error handling
- Meta Pixel tracking
- Trust badges
- Clean UX

### 3. Updated `/Applications/alphaRooster/app/main.py`
New routes:
- `GET /qualify/{offer_slug}` → Display form
- `POST /qualify/{offer_slug}/submit` → Process + redirect

---

## How to Configure Your MaxBounty Link

### Step 1: Get Your Tracking Link
1. Log into MaxBounty
2. Go to **Offer Details** for Champion Auto Insurance (#29678)
3. Copy your **Tracking Link**
   - Example: `https://track.maxbounty.com/visit/?bta=37191&nci=5493`

### Step 2: Update offer_config.py
Open `/Applications/alphaRooster/app/offer_config.py` and replace:

```python
"redirect_url": "https://track.maxbounty.com/visit/?bta=37191&nci=5493",  # Replace with YOUR link
```

With your actual tracking link.

---

## How the Flow Works

1. **User clicks Facebook ad**
   ```
   https://playtosave.net/qualify/champion-auto?fbclid={{fbclid}}
   ```

2. **Server generates event_id** and logs page view to BigQuery

3. **User fills form:**
   - First Name
   - Last Name
   - Email
   - Zip Code

4. **User submits → Server processes:**
   - Validates all fields
   - Stores in BigQuery with `event_id` + `fbclid`
   - Builds MaxBounty URL with prepop

5. **Redirect to MaxBounty:**
   ```
   https://track.maxbounty.com/visit/?bta=37191&nci=5493
     &subId1=abc-123-event-id
     &x=firstName%3DJohn%26lastName%3DDoe%26email%3Djohn@example.com%26zipCode%3D90210
   ```

6. **User completes insurance quote** on MaxBounty's page

7. **MaxBounty fires postback:**
   ```
   https://playtosave.net/postback?subId1=abc-123-event-id&payout=6.00&secret=YOUR_SECRET
   ```

8. **Your postback handler:**
   - Matches `event_id` → finds original `fbclid`
   - Sends CAPI conversion event to Facebook
   - Facebook attributes conversion to correct ad

---

## Testing Locally

### Start the server:
```bash
cd /Applications/alphaRooster
source venv/bin/activate
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

### Test the auto insurance flow:
```bash
# Visit in browser:
http://localhost:8080/qualify/champion-auto?fbclid=test_12345

# Fill form with test data
# Click submit
# Check console for redirect URL
```

### What to verify:
- [ ] Page loads without errors
- [ ] Form displays correctly on mobile (test in dev tools)
- [ ] Validation works (try submitting empty form)
- [ ] Redirect URL contains `subId1=` and `&x=` parameters
- [ ] Prepop data is URL-encoded correctly (`%3D` for `=`, `%26` for `&`)

---

## Adding New Offers

When you get approved for more offers, just update `offer_config.py`:

```python
OFFERS = {
    "champion-auto": {
        "name": "Champion Auto Insurance",
        "maxbounty_id": "29678",
        "payout": 6.00,
        "redirect_url": "https://track.maxbounty.com/visit/?bta=37191&nci=5493",
        "prepop_format": "x",
        "fields_required": ["firstName", "lastName", "email", "zipCode"],
        "active": True
    },
    "champion-home": {
        "name": "Champion Home Insurance",
        "maxbounty_id": "29676",
        "payout": 6.00,
        "redirect_url": "https://track.maxbounty.com/visit/?bta=37191&nci=5491",
        "prepop_format": "x",
        "fields_required": ["firstName", "lastName", "email", "zipCode"],
        "active": True
    },
    "solar-quotes": {  # NEW OFFER
        "name": "Solar Panel Quotes",
        "maxbounty_id": "12345",
        "payout": 15.00,
        "redirect_url": "https://track.maxbounty.com/visit/?bta=37191&nci=9999",
        "prepop_format": "x",
        "fields_required": ["firstName", "lastName", "email", "zipCode"],
        "active": True
    }
}
```

Then create Facebook ads pointing to:
```
https://playtosave.net/qualify/solar-quotes
```

---

## Common Issues & Fixes

### Issue: Form submission returns 404
**Fix:** Check `offer_slug` matches exactly what's in `OFFERS` dict (case-sensitive, use hyphens not underscores)

### Issue: Prepop data not appearing in MaxBounty form
**Fix:** 
1. Check MaxBounty offer supports prepop (see Campaign Description)
2. Verify field names match MaxBounty's expected params
3. Test prepop URL manually by pasting in browser

### Issue: BigQuery insert fails
**Fix:** 
1. Check `.env` has `GCP_PROJECT_ID` and `BIGQUERY_DATASET`
2. Run `python -c "from app.bigquery_client import validate_connection; validate_connection()"`
3. Form will still work even if BigQuery fails (won't block user)

### Issue: Postback not tracking conversions
**Fix:**
1. Verify postback URL in MaxBounty has correct domain
2. Check `AFFILIATE_SECRET` in `.env` matches postback URL
3. Test postback manually: `curl "https://playtosave.net/postback?subId1=test&payout=6.00&secret=YOUR_SECRET"`

---

## Security Notes

- ✅ **Never hardcode affiliate links in templates** - always use `offer_config.py`
- ✅ **Validate all form inputs** - already implemented
- ✅ **Use HTTPS in production** - Cloud Run handles this automatically
- ✅ **Keep AFFILIATE_SECRET secret** - never commit to git

---

## Next: Facebook Ad Setup

Once you've:
1. Updated `redirect_url` in `offer_config.py`
2. Tested locally
3. Deployed to Cloud Run

Then update your Facebook ad URL to:
```
https://playtosave.net/qualify/champion-auto
```

And add URL parameters:
```
utm_source=facebook&utm_medium=cpc&utm_campaign=autoins_feb2026&fbclid={{fbclid}}
```

---

**You're now ready to launch!** 🚀
