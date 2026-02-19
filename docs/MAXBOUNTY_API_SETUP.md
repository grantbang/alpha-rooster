# MaxBounty Offer Details Extractor

## What This Solves
**Problem:** Manually copying offer details is slow and error-prone.  
**Solution:** Semi-automated extraction using browser console + Python parser.

**Note:** MaxBounty doesn't have a public API, so we use a browser-based extraction method.

---

## Setup (One-Time, 30 Seconds Per Offer)

### Step 1: Copy Offer Page Text
1. Login to MaxBounty: https://affiliates.maxbounty.com
2. Navigate to your offer (e.g., `https://affiliates.maxbounty.com/campaign/29678`)
3. Press **F12** (or **Cmd+Option+I** on Mac)
4. Click the **Console** tab
5. Paste this command and press Enter:
   ```javascript
   copy(document.body.innerText)
   ```
6. This copies all visible text to your clipboard

### Step 2: Save to Text File
```bash
# Create the raw text file
code /Applications/alphaRooster/app/offers/offer-29678-raw.txt

# Paste (Cmd+V) and save
```

### Step 3: Run the Parser
```bash
cd /Applications/alphaRooster
python3 scripts/fetch_maxbounty_offer.py 29678
```

**Expected output:**
```
📖 Reading offer #29678 from: /Applications/alphaRooster/app/offers/offer-29678-raw.txt
✅ Saved offer details to: /Applications/alphaRooster/app/offers/offer-29678.json

📊 Extracted Offer Details:
   Name: YourInsurancePath Auto Insurance
   Payout: $6.75
   Countries: US
   Description: Auto insurance quote offer...
   Restrictions: 3 items
```

---

## Usage

### Fetch Any Offer Details
```python
from scripts.fetch_maxbounty_offer import fetch_offer_details

# Get offer data
offer = fetch_offer_details("29678")

# Access details
print(offer["campaigns"][0]["name"])  # Offer name
print(offer["campaigns"][0]["payout"])  # Payout amount
print(offer["campaigns"][0]["description"])  # Full description
print(offer["campaigns"][0]["restrictions"])  # Geographic/age restrictions
```

### Fetch Multiple Offers
```bash
# Fetch all approved offers
python3 scripts/fetch_maxbounty_offer.py --all-approved

# Fetch specific category
python3 scripts/fetch_maxbounty_offer.py --category insurance
```

---

## API Endpoints (Reference)

| Endpoint | Purpose | Example |
|----------|---------|---------|
| `/api/campaigns` | Get offer details | `?campaign_id=29678` |
| `/api/campaigns/approved` | List your approved offers | - |
| `/api/stats` | Get performance data | `?campaign_id=29678&date_start=2026-02-01` |
| `/api/tracking_link` | Generate tracking link | `?campaign_id=29678&sub_id=test123` |

**Full API Docs:** https://www.maxbounty.com/api/documentation

---

## Benefits

✅ **Repeatable:** One command fetches all offer details  
✅ **Accurate:** No copy/paste errors  
✅ **Automated:** Can integrate into CI/CD pipeline  
✅ **Scalable:** Fetch 10 offers as easily as 1

---

## Next Steps

1. **Get API key** (2 minutes)
2. **Add to .env** (30 seconds)
3. **Run fetch script** (5 seconds)
4. **Customize funnel** based on offer data

No more manual web page saving!
