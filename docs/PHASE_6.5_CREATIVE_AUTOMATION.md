# Phase 6.5: Creative Testing Automation

## Goal
Generate and test 50+ ad creatives per month with minimal manual work.

---

## Components

### 1. Creative Generation Pipeline
**Script:** `scripts/generate_creatives.py`

**What it does:**
- Takes 1 base template + list of variants
- Generates 50 image combinations automatically
- Uses Pillow (Python image library) to overlay text on base image

**Example:**
```python
# Input: 1 wheel image + 10 headlines + 5 color schemes = 50 variants
base_image = "wheel_base.png"
headlines = [
    "Save up to $500/year",
    "Compare 10+ providers",
    "You may qualify for savings",
    # ... 7 more
]
colors = ["#FF6B6B", "#4ECDC4", "#FFE66D", "#A8DADC", "#457B9D"]

# Output: 50 unique ad images in /creatives/batch_001/
```

---

### 2. Ad Copy Generator
**Script:** `scripts/generate_ad_copy.py`

**What it does:**
- Uses GPT-4 API to generate ad copy variants
- Based on winning templates + new angles

**Example:**
```python
# Input: 1 winning ad + prompt
winning_ad = "Drivers are saving $500/year with this trick"

prompt = f"""
Generate 10 variants of this winning Facebook ad headline:
"{winning_ad}"

Requirements:
- Insurance theme
- Savings-focused
- Curiosity-driven
- Under 40 characters
"""

# Output: 10 new headlines
```

---

### 3. Batch Upload to Meta Ads API
**Script:** `scripts/upload_ads_to_facebook.py`

**What it does:**
- Takes folder of images + copy variants
- Uploads all to Facebook Ads Manager via API
- Creates ad campaigns automatically

**Example:**
```bash
python3 scripts/upload_ads_to_facebook.py \
  --images creatives/batch_001/*.png \
  --copy creatives/batch_001/copy.json \
  --budget 5 \
  --audience cold-traffic-25-55
```

---

### 4. Performance Monitoring & Auto-Kill
**Script:** `scripts/monitor_and_kill.py`

**What it does:**
- Runs every 6 hours (cron job)
- Checks CTR, CPC, ROAS for all active ads
- Auto-pauses losers, auto-scales winners

**Kill criteria:**
```python
# After 100 impressions (6-12 hours):
if ctr < 0.015:  # < 1.5% CTR
    pause_ad(ad_id)
    
# After $20 spend:
if roas < 1.2:  # < 1.2x return
    pause_ad(ad_id)

# After 48 hours:
if ctr > 0.03:  # > 3% CTR
    increase_budget(ad_id, multiplier=2)
```

---

### 5. Winner Analysis Dashboard
**Script:** `scripts/analyze_winners.py`

**What it does:**
- Queries Facebook Ads API for performance data
- Identifies patterns in winning creatives
- Generates report: "Best headlines", "Best colors", "Best CTAs"

**Output:**
```
📊 Creative Performance Report (Week 3)

Top 5 Headlines:
1. "Save up to $500/year" - 3.2% CTR, $0.45 CPC
2. "Compare 10+ providers" - 2.8% CTR, $0.52 CPC
3. "You may qualify" - 2.5% CTR, $0.58 CPC

Best Colors:
- Red (#FF6B6B): 2.9% avg CTR
- Blue (#457B9D): 2.1% avg CTR

Best CTA:
- "See If You Qualify" - 2.8% avg CTR
- "Check Eligibility" - 2.3% avg CTR
```

---

## Implementation Timeline

### Week 1-2 (After Phase 6 proves ROI):
- [ ] Build `generate_creatives.py` (image generation)
- [ ] Build `generate_ad_copy.py` (GPT-4 integration)
- [ ] Test: Generate 50 creatives locally

### Week 3-4:
- [ ] Build `upload_ads_to_facebook.py` (Meta Ads API)
- [ ] Test: Upload batch of 10 ads manually
- [ ] Verify ads appear in Ads Manager

### Week 5-6:
- [ ] Build `monitor_and_kill.py` (auto-optimization)
- [ ] Set up cron job to run every 6 hours
- [ ] Test: Let system run for 1 week unsupervised

### Week 7-8:
- [ ] Build `analyze_winners.py` (pattern recognition)
- [ ] Create weekly report automation
- [ ] Full end-to-end test: 50 creatives, auto-kill, scale winners

---

## Cost Breakdown

| Item | Cost | Notes |
|------|------|-------|
| **GPT-4 API** | $20-50/month | 500-1,000 ad copy generations |
| **Facebook Ads API** | Free | Built into Business Manager |
| **Image hosting** | $5/month | Cloudinary or S3 for creative storage |
| **Total** | ~$30-60/month | Automation cost |

**ROI:** If this saves 10 hours/month of manual work → Worth $500+ in time saved

---

## Manual Fallback (No Automation)

If you want to test 50+ creatives WITHOUT automation:

### Batch Creation Workflow (3 hours/week):

**Monday (1 hour):**
- Canva: Duplicate base template 20 times
- Change headline on each (pre-written list)
- Export all as PNG

**Tuesday (1 hour):**
- Facebook Ads Manager: "Duplicate Ad" 20 times
- Upload new images
- Adjust copy for each

**Wednesday (1 hour):**
- Check performance
- Pause ads with CTR < 1.5%
- Increase budget on ads with CTR > 3%

**Repeat weekly** = 200+ creatives tested per month

---

## Recommended Tools (No Coding)

If you don't want to build automation yet:

1. **Canva Bulk Create** ($13/month)
   - Upload CSV with 50 headlines
   - Auto-generates 50 images from 1 template
   
2. **AdEspresso** ($49/month)
   - Split testing tool for Facebook ads
   - Auto-pauses losers, scales winners
   
3. **Madgicx** ($55/month)
   - AI creative insights
   - Shows which elements (colors, headlines, CTAs) perform best

---

## Should You Build This Now?

**No - Not yet.** Here's why:

### Build automation AFTER you have:
- ✅ 1 profitable offer (ROAS > 1.5x)
- ✅ Spent $1,000+ on ads (learned what works manually)
- ✅ Found 2-3 winning creative patterns

### Why wait?
- Early stage = need to learn manually first
- Automation is expensive (time + money) if you don't know what works
- Manual testing for Month 1-2 gives you the data to automate intelligently

### Timeline:
- **Month 1-2:** Manual testing (10-20 creatives)
- **Month 3-4:** Build automation (if profitable)
- **Month 5+:** Scale with automation (50+ creatives/month)

---

## What IS in Your Current Plan?

**Yes - Phase 6.5 (AI Creative Scaling) already exists!**

Let me check what's documented:
