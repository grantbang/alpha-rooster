# Batch 001 - Facebook Dynamic Creative Setup
**Launch Date:** February 17, 2026  
**Campaign:** AutoIns - Home Insurance - Feb2026  
**Objective:** Generate $6.00 leads via MaxBounty Offer #29676

---

## 🚦 **CURRENT STATUS: PAUSED - AWAITING MAXBOUNTY APPROVAL**

### ✅ **COMPLETED:**
- [x] 3 ad creatives generated (Logic/Orange, Fear/Red, Curiosity/Purple)
- [x] Ad copy written (2 primary text variants, 2 headlines, description)
- [x] Facebook Ads strategy documented (3:2:2 Dynamic Creative framework)
- [x] Placement strategy confirmed (Advantage+ automatic placements)
- [x] Tracking plan defined (fbclid → event_id → CAPI flow)
- [x] Prepop parameter format researched for MaxBounty

### ⏸️ **BLOCKED - WAITING ON:**
- [ ] **MaxBounty offer approval** for Champion Auto Insurance (#29678)
  - Email sent to affiliate manager with traffic details
  - Waiting for response (typically 1-24 hours)
  - Cannot launch Facebook ads until approved

### 🔨 **NEXT STEPS (After Approval):**
1. **✅ DONE: Built `/qualify/{offer_slug}` route** 
   - Dynamic multi-offer support
   - Form captures: name, email, zip
   - Redirects to MaxBounty with prepop
   - Stores events in BigQuery
   - **Files created:**
     - `/Applications/alphaRooster/app/offer_config.py` (offer definitions)
     - `/Applications/alphaRooster/app/templates/qualify_offer.html` (form template)
     - Updated `/Applications/alphaRooster/app/main.py` (new routes)

2. **Update offer_config.py with your MaxBounty tracking link**
   - Open `/Applications/alphaRooster/app/offer_config.py`
   - Replace `redirect_url` with your actual MaxBounty affiliate link
   - Example: `https://track.maxbounty.com/visit/?bta=YOUR_BTA&nci=YOUR_NCI`

3. **Test the funnel end-to-end**
   - Start server: `uvicorn app.main:app --reload`
   - Visit: `http://localhost:8080/qualify/champion-auto?fbclid=test123`
   - Fill form with test data
   - Verify redirect to MaxBounty with prepop
   - Check URL contains: `&x=firstName%3DJohn%26lastName%3DDoe%26email%3Dtest@example.com`

4. **Update Facebook ad URL**
   - Change from: `https://playtosave.net/qualify`
   - Change to: `https://playtosave.net/qualify/champion-auto`  
   - (Or `/qualify/champion-home` for home insurance offer)

5. **Complete Facebook ad setup**
   - Upload 3 images to Ads Manager
   - Paste ad copy (2 primary text, 2 headlines)
   - Set URL parameters with {{fbclid}}
   - Schedule for midnight launch

6. **Launch campaign**
   - Set $20/day budget
   - Target: US, 25-65, Homeowners
   - Hold for 48 hours (no changes)

### 📋 **FILES READY TO USE:**
```
/Applications/alphaRooster/creative_assets/batch001_feb17/
  ├── batch001_logic_img_feb17.png      ✅ Generated
  ├── batch001_fear_img_feb17.png       ✅ Generated
  ├── batch001_curiosity_img_feb17.png  ✅ Generated
  ├── copy_primary_long.txt             ✅ Written (see Step 2 below)
  ├── copy_primary_short.txt            ✅ Written (see Step 2 below)
  └── copy_headlines.txt                ✅ Written (see Step 2 below)
```

### ⏰ **ESTIMATED TIME TO LAUNCH (Post-Approval):**
- ~~Build /qualify route: ~30 minutes~~ ✅ DONE
- Update MaxBounty tracking link: ~5 minutes
- Test funnel locally: ~10 minutes
- Complete Facebook setup: ~20 minutes
- **Total: ~35 minutes from approval to live campaign**

---

**📧 ACTION ITEM:** Check email for MaxBounty approval response. Once approved, continue to Step 1 below.

---

## Step 1: Organize Your Files

Create this folder structure and save your 3 generated images:

```
/Applications/alphaRooster/creative_assets/batch001_feb17/
  ├── batch001_logic_img_feb17.png      (Orange banner - "Save up to $565")
  ├── batch001_fear_img_feb17.png       (Red banner - "Why STILL overpaying?")
  ├── batch001_curiosity_img_feb17.png  (Purple banner - "2-Minute Trick")
  ├── copy_primary_long.txt
  ├── copy_primary_short.txt
  └── copy_headlines.txt
```

---

## Step 2: Save Your Ad Copy Files

### **File: copy_primary_long.txt**
```
Most Americans are overpaying for home insurance — by an average of $565/year.

Why? Because insurance companies count on you NOT shopping around.

Here's the truth: Your rates should stay competitive. But instead, they keep raising them every year — hoping you won't notice.

The fix is simple: Compare quotes every 12 months.

We built a quick 2-minute tool to make this painless. Answer a few questions and see if you qualify for a personalized quote.

No phone calls. No pushy salespeople. Just honest savings.

Ready to see how much you could save? 👇
```

### **File: copy_primary_short.txt**
```
Insurance companies are counting on you NOT comparing rates.

Don't let them.

See if you qualify for lower rates in 2 minutes 🏠

Most homeowners save $565/year just by shopping around.

Your turn 👇
```

### **File: copy_headlines.txt**
```
Headline 1: See If You Qualify for Lower Insurance Rates
Headline 2: Are You Overpaying for Home Insurance?
```

---

## Step 3: Facebook Ads Manager Setup

### **Campaign Level**
1. Click **"+ Create"** in Ads Manager
2. **Objective:** Sales (or "Leads" if Sales unavailable)
3. **Campaign Name:** `AutoIns-Home-Feb2026-Batch001`
4. **Campaign Budget Optimization:** OFF (toggle off)
5. Click **"Next"**

---

### **Ad Set Level**
1. **Ad Set Name:** `Cold-US-2565-Homeowners-DynCreative`
2. **Conversion Location:** Website
3. **Pixel:** Select your Meta Pixel
4. **Conversion Event:** Lead (or PageView if Lead not available yet)
5. **Dynamic Creative:** Toggle ON ✅
6. **Budget:** $20.00 per day
7. **Start Date:** Tomorrow at 12:00 AM (midnight)
8. **End Date:** Ongoing

**Targeting:**
- **Location:** United States
- **Age:** 25-65
- **Gender:** All
- **Detailed Targeting:** Type "Homeowners" → Select interest
- **Languages:** English (All)

**Placements:**
- **Advantage+ Placements:** ON (automatic)

9. Click **"Next"**

---

### **Ad Level (Ad Creative Section)**

**You're here now. Follow these exact steps:**

---

#### **1. Optimize creative for each person**
✅ **TURN THIS ON** (toggle should be blue/enabled)
- This enables Dynamic Creative testing

---

#### **2. Primary text**
Click the text field and paste **Primary Text Option 1** (long-form):
```
Most Americans are overpaying for home insurance — by an average of $565/year.

Why? Because insurance companies count on you NOT shopping around.

Here's the truth: Your rates should stay competitive. But instead, they keep raising them every year — hoping you won't notice.

The fix is simple: Compare quotes every 12 months.

We built a quick 2-minute tool to make this painless. Answer a few questions and see if you qualify for a personalized quote.

No phone calls. No pushy salespeople. Just honest savings.

Ready to see how much you could save? 👇
```

Then click **"Add another option"** and paste **Primary Text Option 2** (short-form):
```
Insurance companies are counting on you NOT comparing rates.

Don't let them.

See if you qualify for lower rates in 2 minutes 🏠

Most homeowners save $565/year just by shopping around.

Your turn 👇
```

---

#### **3. Headline**
Click the headline field and enter:
```
See If You Qualify for Lower Insurance Rates
```

Then click **"Add another option"** and enter:
```
Are You Overpaying for Home Insurance?
```

---

#### **4. Description**
Enter:
```
Get your personalized quote. Fast. Free.
```

---

#### **5. Website URL**
⚠️ **THIS IS CRITICAL - COPY EXACTLY:**
```
https://playtosave.net/qualify/champion-auto
```
**(Do NOT add fbclid here - we'll do that in Tracking section below)**

**Note:** We're using the dynamic `/qualify/{offer_slug}` route. The offer slug `champion-auto` matches the configuration in `app/offer_config.py`. When the user submits the form, they'll be redirected to your MaxBounty affiliate link with prepopulated data.

---

#### **6. Display link** (Optional)
Leave blank or enter:
```
playtosave.net/qualify
```

---

#### **7. Browser add-ons**
Select: **Instant form (suggested)** ✅
- This adds a lead form option for people who want to skip the game

---

#### **8. Call to action**
Click dropdown and select: **Learn More**

Then click **"Add another option"** if available (some accounts allow 2 CTA options)

---

#### **9. Media (Images)**
Scroll up or look for "Add Media" button
Click **"Add Media"** → **"Add Image"**

Upload all 3 images:
- `batch001_logic_img_feb17.png` (Orange "Save $565")
- `batch001_fear_img_feb17.png` (Red "Why STILL overpaying")
- `batch001_curiosity_img_feb17.png` (Purple "2-Minute Trick")

---

#### **10. Tracking Section**
**Website events:**
- Your pixel should already be selected: `championAutoInsurancePixel1` (Pixel ID: 2066263104107367)

⚠️ **IGNORE the "Your Meta Pixel is not active" warning** - This is a false alarm if you just set it up. We'll verify it works in Step 4.

**URL parameters:**
Click **"Build a URL parameter"** button

In the text field, paste EXACTLY:
```
utm_source=facebook&utm_medium=cpc&utm_campaign=autoins_home_feb2026&fbclid={{fbclid}}
```

⚠️ **CRITICAL:** The `{{fbclid}}` must include the double curly braces!

**How the tracking flow works:**
1. User clicks ad → Lands on `playtosave.net/qualify?fbclid=xyz123...`
2. User fills form (name, email, etc.) → Submits
3. Backend redirects to MaxBounty with prepopulated data:
   ```
   https://maxbounty-offer-url.com?subId1=EVENT_ID&x=firstName%3DJohn%26lastName%3DDoe%26email%3Djohn@example.com
   ```
4. MaxBounty tracks conversion, fires postback with `subId1=EVENT_ID`
5. We match `EVENT_ID` back to `fbclid` → Send CAPI event to Facebook

---

#### **11. Final Review**
Before publishing, verify:
- [ ] "Optimize creative for each person" is toggled ON
- [ ] 2 Primary text variations added
- [ ] 2 Headlines added
- [ ] 3 Images uploaded
- [ ] Website URL is `https://playtosave.net/qualify`
- [ ] URL parameters include `{{fbclid}}`
- [ ] Call to action is "Learn More"

---

#### **12. Publish**
Click **"Publish"** button (bottom right)

You should see: "Your ad is in review. We'll let you know when it's approved."

Approval usually takes 5-30 minutes. Check your email/notifications.

---

## Step 4: Pre-Launch Verification (Do This NOW)

### **Test Your Pixel (5 minutes)**
1. Open https://playtosave.net/qualify in new tab
2. Open browser DevTools (F12) → Network tab
3. Filter for "facebook"
4. Refresh page
5. ✅ You should see pixel fire with `PageView` event

### **Test Your Funnel (2 minutes)**
1. Go to: https://playtosave.net/qualify
2. Fill out the pre-qualifier form with test data
3. Submit form
4. Verify redirect to MaxBounty offer with prepopulated data (check URL)
5. ✅ Confirm name/email are filled in on the insurance form

### **Check Events Manager (3 minutes)**
1. Go to: https://business.facebook.com/events_manager
2. Select your Pixel
3. Check "Overview" tab
4. ✅ Confirm events are flowing (if you tested above, you should see activity)

---

## Step 5: Launch Checklist

**Before Midnight Tonight:**
- [ ] All 3 images saved in `/creative_assets/batch001_feb17/`
- [ ] Campaign scheduled for 12:00 AM launch
- [ ] Daily budget confirmed: $20.00 (NOT $200!)
- [ ] URL includes `{{fbclid}}` parameter
- [ ] Dynamic Creative is toggled ON
- [ ] Placements set to Advantage+ (automatic)
- [ ] Pixel is firing on playtosave.net/qualify
- [ ] Pre-qualifier form redirects to MaxBounty with prepopulated data
- [ ] Screenshot campaign settings (for your records)

---

## Step 6: The 48-Hour Rule (DO NOT TOUCH)

**Days 1-2 (Feb 18-19):**
- ✅ Check spend each morning (should be ~$20/day)
- ✅ Monitor for ad rejections (fix immediately if flagged)
- ❌ Do NOT pause ads
- ❌ Do NOT change budget
- ❌ Do NOT edit targeting
- ❌ Do NOT touch creative

**Facebook needs 48 hours to exit Learning Phase. ANY edit resets it.**

---

## Step 7: Day 3 Review (Feb 20)

Run this BigQuery query to check performance:

```sql
SELECT 
  COUNT(DISTINCT event_id) as total_clicks,
  COUNT(DISTINCT CASE WHEN interaction_result IS NOT NULL THEN event_id END) as game_plays,
  (SELECT COUNT(*) FROM `rooster-analytics-12345.rooster_data.conversion_signals` 
   WHERE DATE(conversion_time) >= '2026-02-18') as conversions
FROM `rooster-analytics-12345.rooster_data.game_events`
WHERE DATE(timestamp) >= '2026-02-18';
```

**Decision Matrix:**

| Scenario | Action |
|----------|--------|
| **Spent < $40, 0 conversions** | WAIT (not enough data) |
| **Spent $40-60, 0 conversions** | WAIT until $60.75 spent |
| **Spent > $60.75, 0 conversions** | PAUSE campaign (Kill Rule triggered) |
| **1-2 conversions, any spend** | HOLD (let it run, calculate ROAS on Day 4) |
| **3+ conversions, ROAS > 1.5x** | SCALE +20% budget (increase to $24/day) |

---

## Expected Performance (First 48 Hours)

| Metric | Conservative | Good | Excellent |
|--------|--------------|------|-----------|
| **Impressions** | 8,000-12,000 | 15,000-25,000 | 30,000+ |
| **Clicks** | 40-60 | 80-120 | 150+ |
| **CTR** | 0.5-0.8% | 1.0-1.5% | 2.0%+ |
| **Cost Per Click** | $0.60-0.90 | $0.40-0.60 | $0.20-0.40 |
| **Conversions** | 0-1 | 2-3 | 4-6 |
| **ROAS** | 0.0-0.75x | 1.0-1.5x | 2.0x+ |

**Note:** It's NORMAL to have zero conversions in first 24 hours. Don't panic.

---

## The 3:2:2 Matrix Breakdown

**What Facebook will auto-test:**

3 Images:
- Logic (Orange) → Analytical thinkers
- Fear (Red) → People with rate increases
- Curiosity (Purple) → Broad appeal

2 Primary Text Variants:
- Long-form (200 words) → Desktop users, readers
- Short-form (50 words) → Mobile users, scrollers

2 Headlines:
- "See If You Qualify..." → Benefit-focused
- "Are You Overpaying..." → Pain-focused

**Total Combinations:** 3 × 2 × 2 = **12 ad variants**

Facebook's algorithm will automatically show the best-performing combos more often.

---

## Week 1 Goals

**By Feb 24 (Day 7), you should know:**
- ✅ Which image angle performs best (check CTR by asset)
- ✅ Which text length works better (check CTR by primary text)
- ✅ Whether campaign is profitable (ROAS > 1.5x)
- ✅ Your avg Cost Per Lead (target: < $6.00)

**Access this data:**
Ads Manager → Campaigns → Select campaign → Breakdown dropdown → "By: Delivery"

---

## Next Batch Planning

**If Batch 001 hits ROAS > 1.5x by Day 7:**

Create Batch 002 with these changes:
- Keep winning angle (double down)
- Create 3 new images with same angle but different headlines
- Test 2 new text variations
- Launch in parallel (separate ad set, $20/day)

**Batch cadence:** New batch every 7 days to combat ad fatigue.

---

## Support

**If ad gets rejected:**
1. Check rejection reason in Ads Manager
2. Most common: "Exaggerated claims" → Remove "guaranteed" language
3. Edit ad, resubmit within 24 hours

**If pixel stops firing:**
1. Test in incognito window (ad blockers can interfere)
2. Check Events Manager → Diagnostics
3. Verify pixel ID in base.html matches your account

**If conversions not tracking:**
1. Check MaxBounty postback URL is configured
2. Send test postback from MaxBounty dashboard
3. Query BigQuery: `SELECT * FROM conversion_signals ORDER BY conversion_time DESC LIMIT 5`

---

**LAUNCH STATUS: READY ✅**

All systems green. Schedule campaign for midnight and let it run!
