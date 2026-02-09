# Phase 1.3: Meta Business Manager Setup
**Goal:** Create Facebook Business Manager, verify domain, create page, warm account, get Pixel ID & CAPI token

**Time Required:** 3-4 hours (plus 3-day warming campaign)  
**Cost:** $15 (warming campaign)  
**Outcome:** Ready to launch Facebook ad campaigns

---

## ✅ Checklist Overview

- [ ] 1.3.1: Create Meta Business Manager account (15 min)
- [ ] 1.3.2: Verify playtosave.net domain (10 min)
- [ ] 1.3.3: Create Facebook Business Page (20 min)
- [ ] 1.3.4: Upload branding assets (15 min)
- [ ] 1.3.5: Publish 3 warming posts (30 min)
- [ ] 1.3.6: Run $15 warming campaign (15 min setup, 3 days runtime)
- [ ] 1.3.7: Create Meta Pixel (10 min)
- [ ] 1.3.8: Generate CAPI Access Token (10 min)
- [ ] 1.3.9: Update environment variables (5 min)
- [ ] 1.3.10: Deploy with real credentials (5 min)
- [ ] 1.3.11: Test CAPI integration (10 min)

**Total Active Time:** ~2.5 hours  
**Total Waiting Time:** 3 days (warming campaign)

---

## 📋 Task 1.3.1: Create Meta Business Manager Account

**Why:** Business Manager is required to run ads, create pixels, manage assets

### Steps:

1. **Go to:** https://business.facebook.com
2. **Click:** "Create Account" (top right)
3. **Business Name:** "Play To Save Marketing" (or your choice)
4. **Your Name:** [Your real name]
5. **Business Email:** [Your email - use real one, you'll verify it]
6. **Click:** "Next"
7. **Enter business details:**
   - Address: Your real address (required for verification)
   - Phone: Your real phone
   - Website: `https://playtosave.net`
8. **Verify email:** Check inbox, click verification link
9. **Add payment method:** Settings → Payments → Add Payment Method
   - Use credit/debit card (needed for ads)
   - Facebook may charge $1 test charge (refunded)

### Verification:
- ✅ You see Business Manager dashboard
- ✅ Email verified (green checkmark)
- ✅ Payment method added

---

## 📋 Task 1.3.2: Verify playtosave.net Domain

**Why:** Proves you own the domain, enables tracking, builds trust with Facebook

### Steps:

1. **In Business Manager:**
   - Click hamburger menu (☰) → "Business Settings"
   - Left sidebar → "Brand Safety" → "Domains"
   - Click "Add" button
2. **Enter domain:** `playtosave.net` (no https://, no www)
3. **Click:** "Add Domain"
4. **Choose verification method:** "Meta-tag verification" (easiest)
5. **Copy the meta tag** (looks like):
   ```html
   <meta name="facebook-domain-verification" content="abc123xyz456..." />
   ```
6. **Add to your base.html template:**
   - Open `app/templates/base.html`
   - Paste meta tag inside `<head>` section
   - Save file
7. **Deploy updated template to Cloud Run:**
   ```bash
   gcloud run deploy rooster-game \
     --source . \
     --region us-central1 \
     --allow-unauthenticated
   ```
8. **Wait 2-3 minutes for deployment**
9. **Back in Business Manager:** Click "Verify Domain"
10. **Refresh page** - Status should change to "Verified" (green checkmark)

### Verification:
- ✅ Domain shows "Verified" status
- ✅ Green checkmark next to playtosave.net

---

## 📋 Task 1.3.3: Create Facebook Business Page

**Why:** Required to run ads, builds social proof, needed for warming campaign

### Steps:

1. **In Business Manager:**
   - Business Settings → Accounts → Pages → "Add" → "Create a New Page"
2. **Page Name:** "PlayToSave" (or "Play To Save")
3. **Category:** "Financial Service" or "Website"
4. **Bio/Description (150 chars):**
   ```
   Win cash savings on insurance, utilities & more! Play our free game to unlock exclusive offers. Save money the fun way! 💰🎮
   ```
5. **Click:** "Create Page"
6. **Add to Business Manager:**
   - Business Settings → Accounts → Pages → "Add" → "Add a Page"
   - Search for your page name
   - Click "Add Page"

### Verification:
- ✅ Page created and visible
- ✅ Page added to Business Manager
- ✅ You see page in Business Settings → Pages

---

## 📋 Task 1.3.4: Upload Branding Assets

**Why:** Professional appearance, builds trust, required for ads

### Assets Needed:

**Profile Picture (400×400px):**
- Logo or icon representing PlayToSave
- Simple, recognizable design
- Use Canva template: "Facebook Profile Picture"
- Suggested: Rooster icon + $ symbol or game wheel

**Cover Photo (820×312px):**
- Banner image for page header
- Use Canva template: "Facebook Cover Photo"
- Suggested text: "Save Money by Playing Games!" + game wheel visual

### Steps:

1. **Create assets in Canva:**
   - Go to canva.com
   - Search "Facebook Profile Picture" template
   - Create rooster/savings themed icon (400×400)
   - Download as PNG
   - Search "Facebook Cover Photo" template
   - Create banner with game wheel + savings message (820×312)
   - Download as PNG

2. **Upload to Facebook Page:**
   - Go to your PlayToSave page
   - Click profile picture area → "Upload Photo" → Select file
   - Click cover photo area → "Upload Photo" → Select file
   - Crop/adjust as needed
   - Click "Save"

### Verification:
- ✅ Profile picture visible
- ✅ Cover photo visible
- ✅ Page looks professional

---

## 📋 Task 1.3.5: Publish 3 Warming Posts

**Why:** New pages with no activity look suspicious, warming builds legitimacy

**Strategy:** Educational content about saving money (NOT promotional yet)

### Post 1: Money-Saving Tip (Text + Image)
```
💡 Money-Saving Tip: Compare insurance quotes annually!

Most people overpay by $400+ per year by sticking with the same provider. 

Set a calendar reminder to compare rates every 12 months. Even 15 minutes of comparison shopping can save hundreds! 

What's your favorite money-saving hack? Drop it in the comments! 👇

#MoneySavingTips #PersonalFinance #InsuranceSavings
```
**Image:** Create in Canva - "$400 Average Savings" graphic

---

### Post 2: Gamification Hook (Text Only)
```
🎮 Fun Fact: Did you know gamification can help you save money?

Studies show people are 3x more likely to complete a task when it's presented as a game vs. a chore.

That's why we built PlayToSave - turning savings into rewards! 

What's one financial goal you'd like to "gamify"? Let us know! 

#Gamification #FinancialGoals #SaveMoney
```

---

### Post 3: Value Proposition Soft Launch (Text + Image)
```
🎁 Introducing PlayToSave!

We're on a mission to make saving money FUN. 

Here's how it works:
✅ Play a quick game (30 seconds)
✅ Unlock exclusive savings offers
✅ Save hundreds on insurance, utilities & more

No tricks, no gimmicks - just real savings through trusted partners.

Ready to play? Link in bio! 👆

#PlayToSave #SaveMoney #InsuranceDeals
```
**Image:** Screenshot of your game wheel or homepage

---

### Steps to Publish:

1. Go to your Facebook Page
2. Click "Create Post"
3. Paste Post 1 text
4. Click "Add Photo/Video" → Upload Post 1 image
5. Click "Publish"
6. **Wait 1 hour** (don't spam)
7. Repeat for Post 2 (no image)
8. **Wait 1 hour**
9. Repeat for Post 3 with image

### Verification:
- ✅ 3 posts published
- ✅ Posts are public (visible to everyone)
- ✅ No spammy/promotional language

---

## 📋 Task 1.3.6: Run $15 Warming Campaign

**Why:** Facebook trusts accounts that spend money successfully before scaling

**Strategy:** Page Likes campaign, $5/day for 3 days, broad targeting

### Steps:

1. **In Business Manager:**
   - Ads Manager → "Create" button
2. **Campaign Objective:** "Engagement" → "Page Likes"
3. **Campaign Name:** "Page Warming - Feb 2026"
4. **Budget:** 
   - Daily budget: $5.00
   - Campaign duration: 3 days
   - Total spend: $15.00
5. **Ad Set Settings:**
   - **Location:** United States
   - **Age:** 25-65
   - **Gender:** All
   - **Detailed Targeting:** Leave blank (broad)
   - **Placements:** Automatic Placements
6. **Ad Creative:**
   - **Format:** Single Image
   - **Image:** Use your cover photo
   - **Primary Text:** "Follow PlayToSave for money-saving tips and exclusive offers! 💰"
   - **Headline:** "Free Money-Saving Resources"
   - **Call to Action:** "Like Page"
7. **Click:** "Publish"
8. **Wait for review:** Usually 15 minutes - 2 hours
9. **Let it run:** Don't touch it for 3 days

### Expected Results:
- 30-60 page likes
- $0.25-$0.50 cost per like
- Account now "warmed" for conversion campaigns

### Verification:
- ✅ Campaign status: "Active"
- ✅ Campaign runs for 3 days
- ✅ No disapprovals or policy violations

---

## 📋 Task 1.3.7: Create Meta Pixel

**Why:** Tracks conversions, enables CAPI, powers Facebook optimization

### Steps:

1. **In Business Manager:**
   - Events Manager (left menu)
   - Click "Connect Data Sources" → "Web" → "Get Started"
2. **Select:** "Meta Pixel"
3. **Pixel Name:** "PlayToSave Pixel"
4. **Website URL:** `https://playtosave.net`
5. **Click:** "Continue"
6. **Setup Method:** "Manually Install Code" (we'll add it ourselves)
7. **Copy Pixel ID:** (16-digit number like `1234567890123456`)
   - **SAVE THIS** - You need it for .env file
8. **Don't close the window yet** - We'll install code in next step

### Install Pixel Code:

1. **Copy the pixel base code** (looks like):
   ```html
   <!-- Meta Pixel Code -->
   <script>
     !function(f,b,e,v,n,t,s)
     {if(f.fbq)return;n=f.fbq=function(){n.callMethod?
     n.callMethod.apply(n,arguments):n.queue.push(arguments)};
     if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
     n.queue=[];t=b.createElement(e);t.async=!0;
     t.src=v;s=b.getElementsByTagName(e)[0];
     s.parentNode.insertBefore(t,s)}(window, document,'script',
     'https://connect.facebook.net/en_US/fbevents.js');
     fbq('init', 'YOUR_PIXEL_ID');
     fbq('track', 'PageView');
   </script>
   ```

2. **Update base.html:**
   - File: `app/templates/base.html`
   - Paste pixel code in `<head>` section (below meta tags)
   - Replace `YOUR_PIXEL_ID` with actual Pixel ID

3. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy rooster-game --source . --region us-central1
   ```

4. **Test pixel:**
   - Go to https://playtosave.net
   - Open browser DevTools (F12) → Network tab
   - Reload page
   - Search for "fbevents" - should see requests
   - In Events Manager → Test Events → Enter your URL → Click "Test"
   - You should see "PageView" event

### Verification:
- ✅ Pixel ID saved (write it down!)
- ✅ Pixel code installed in base.html
- ✅ Test Events shows "PageView" firing
- ✅ Events Manager shows "Active" status

---

## 📋 Task 1.3.8: Generate CAPI Access Token

**Why:** Allows server-side events (Phase 4.2 CAPI integration)

### Steps:

1. **In Events Manager:**
   - Click your pixel name ("PlayToSave Pixel")
   - Go to "Settings" tab
   - Scroll to "Conversions API" section
   - Click "Generate Access Token"
2. **Token Details:**
   - Name: "PlayToSave Server Token"
   - Description: "Server-side conversion tracking"
   - Click "Generate Token"
3. **Copy Token:** (long string starting with `EAA...`)
   - **SAVE THIS IMMEDIATELY** - You can't see it again!
   - Store in password manager or secure note
4. **Click:** "Done"

### Verification:
- ✅ Access token saved securely
- ✅ Token shows in Conversions API settings
- ✅ Status: "Active"

---

## 📋 Task 1.3.9: Update Environment Variables

**Why:** Activate CAPI integration with real credentials

### Steps:

1. **Open `.env` file:**
   ```bash
   code /Applications/alphaRooster/.env
   ```

2. **Update these lines:**
   ```env
   # Replace placeholders with REAL values from Phase 1.3:
   META_PIXEL_ID=1234567890123456          # From Task 1.3.7
   META_ACCESS_TOKEN=EAAxxxYourTokenxxx    # From Task 1.3.8
   ```

3. **Save file**

4. **NEVER commit .env to git** - Verify:
   ```bash
   cat .gitignore | grep .env
   # Should show: .env
   ```

### Verification:
- ✅ META_PIXEL_ID has real 16-digit number
- ✅ META_ACCESS_TOKEN has real EAA token
- ✅ .env file saved
- ✅ .env NOT in git (run: `git status` - should not appear)

---

## 📋 Task 1.3.10: Deploy with Real Credentials

**Why:** Activate CAPI in production

### Steps:

**Option A: Use Secret Manager (RECOMMENDED for production):**

1. **Create secrets in Google Cloud:**
   ```bash
   echo -n "YOUR_PIXEL_ID" | gcloud secrets create meta-pixel-id --data-file=-
   echo -n "YOUR_ACCESS_TOKEN" | gcloud secrets create meta-access-token --data-file=-
   ```

2. **Deploy with secrets:**
   ```bash
   gcloud run deploy rooster-game \
     --source . \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars GCP_PROJECT_ID=rooster-486417,BIGQUERY_DATASET=rooster_data \
     --set-secrets META_PIXEL_ID=meta-pixel-id:latest,META_ACCESS_TOKEN=meta-access-token:latest,AFFILIATE_SECRET=affiliate-secret:latest
   ```

**Option B: Use env vars directly (SIMPLER for testing):**
```bash
gcloud run deploy rooster-game \
  --source . \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars GCP_PROJECT_ID=rooster-486417,BIGQUERY_DATASET=rooster_data,META_PIXEL_ID=YOUR_PIXEL_ID,META_ACCESS_TOKEN=YOUR_TOKEN,AFFILIATE_SECRET=dca9f8aa24d495b96e42356c7621766dcb15d5682fcc4a153b0b71b9fa43a58c
```

### Verification:
- ✅ Deployment succeeds
- ✅ No errors about missing env vars
- ✅ Server logs show: "✅ Facebook Ads API initialized"

---

## 📋 Task 1.3.11: Test CAPI Integration

**Why:** Verify Facebook receives conversion events

### Steps:

1. **Send test postback:**
   ```bash
   curl "https://playtosave.net/postback?subId1=capi-test-$(date +%s)&payout=6.75&secret=dca9f8aa24d495b96e42356c7621766dcb15d5682fcc4a153b0b71b9fa43a58c"
   ```

2. **Check Cloud Run logs:**
   ```bash
   gcloud run services logs read rooster-game --region us-central1 --limit 20
   ```
   - Look for: "📡 Sending CAPI event"
   - Look for: "✅ CAPI event sent successfully"

3. **Check Meta Events Manager:**
   - Go to Events Manager → Test Events
   - Click "Test Server Events" tab
   - Enter your access token
   - Click "Test"
   - Should see "Purchase" event appear!

4. **Verify in BigQuery:**
   ```bash
   bq query --use_legacy_sql=false 'SELECT event_id, payout FROM `rooster-486417.rooster_data.conversion_signals` ORDER BY conversion_time DESC LIMIT 3'
   ```

### Verification:
- ✅ Cloud Run logs show CAPI event sent
- ✅ Meta Events Manager shows "Purchase" event
- ✅ BigQuery shows conversion logged
- ✅ No errors in logs

---

## ✅ Phase 1.3 Complete Checklist

When you can check all these boxes, you're ready to launch campaigns:

- [ ] Business Manager account created & verified
- [ ] playtosave.net domain verified
- [ ] Facebook Page created with branding
- [ ] 3 warming posts published
- [ ] $15 warming campaign running (3 days)
- [ ] Meta Pixel created & firing
- [ ] CAPI Access Token generated
- [ ] Environment variables updated
- [ ] Cloud Run deployed with real credentials
- [ ] CAPI test event successful in Events Manager
- [ ] BigQuery receiving conversions

---

## 🚀 What Unlocks After Phase 1.3

**You can now:**
- ✅ Create Facebook ad campaigns
- ✅ Track conversions with Pixel + CAPI
- ✅ See real ROAS data
- ✅ Let Facebook optimize targeting
- ✅ Scale profitable campaigns

**Next Phases:**
- **Phase 2:** Create 3:2:2 Dynamic Creative assets
- **Phase 6:** Launch first $20/day campaign
- **Phase 5:** Monitor with operating rules (Hold/Kill/Scale)

---

## 💰 Cost Breakdown

- Business Manager: **$0**
- Domain verification: **$0** (already own domain)
- Facebook Page: **$0**
- Warming campaign: **$15** (one-time)
- Meta Pixel: **$0**
- CAPI: **$0**

**Total Phase 1.3 Cost: $15**

---

## ⏰ Timeline

- **Day 1:** Tasks 1.3.1 - 1.3.8 (3 hours active work)
- **Days 1-3:** Warming campaign runs (passive)
- **Day 4:** Tasks 1.3.9 - 1.3.11 (1 hour)
- **Day 4+:** Ready to launch campaigns!

**Total Time to Revenue: 4 days from today**
