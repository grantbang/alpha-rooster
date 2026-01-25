# Alpha Rooster Build Progress Tracker

> **Instructions:** Check off tasks as you complete them. Add verification proof (screenshot filename, query result, etc.) in notes.

**Started:** January 22, 2026  
**Current Phase:** Phase 3.2 (Pre-Qualifier - In Progress)  
**Target Completion:** February 3, 2026

---

## 📊 Overall Progress Summary

**Phase 1: Foundation** - 25% Complete (4/16 tasks)
- ✅ Domain & email setup complete
- ✅ Coming soon page live
- ✅ MaxBounty application submitted
- ⏳ Awaiting phone interview
- ❌ GCP setup not started
- ❌ Meta Business Manager not started
- ❌ Legal docs not started

**Phase 2: Creative Arsenal** - 0% Complete (0/13 tasks)
- ❌ Ad creatives not started (Reference: CONTENT-CREATION-GUIDE.md)
- ❌ Game variants not started
- ❌ A/B testing framework not started

**Phase 3: Game App** - 17% Complete (5/30 tasks)
- ✅ Local development complete (Phase 3.1)
- ⏳ Pre-qualifier in progress (Phase 3.2)
- ❌ Game engine not built
- ❌ Tracking not integrated
- ❌ Deployment not done

**Phase 4-6** - 0% Complete
- Phases 4, 5, 6 pending Phase 3 completion

**Next Steps:**
1. Complete MaxBounty phone interview (Week 1-2)
2. Build Phase 3.1-3.3 local prototype (Week 1-2)
3. Create first ad creatives Phase 2.1 (Week 2)
4. Launch first test campaign (Week 3)

---

## ✅ Phase 1: Foundation & Compliance (Days 1-2)

### 1.0 Domain & Email Setup (PREREQUISITE - Do First!)
- [x] **1.0.1** Domain registered
  - Domain name: playtosave.net
  - Registrar: Namecheap
  - Cost: $12.98/year
  - WHOIS privacy enabled: ✓
  - Notes: ✅ COMPLETED - Domain purchased January 22, 2026
- [x] **1.0.2** Professional email configured
  - Method: Email forwarding (Namecheap)
  - Email created: info@playtosave.net
  - Forwarding to: Personal Gmail
  - Test sent and received: ✓
  - Cost: $0 (email forwarding included with domain)
  - Notes: ✅ COMPLETED - Email forwarding working January 22, 2026
- [x] **1.0.3** Coming Soon page deployed
  - File: `index.html` uploaded (from `coming_soon.html`)
  - Live URL verified: https://playtosave.net ✓
  - Hosting: GitHub Pages (free)
  - DNS: Fully propagated, SSL certificate active
  - Screenshot: `tests/domain_live.png`
  - Contact email visible: ✓ (optional, uncomment in HTML)
  - Notes: ✅ COMPLETED - Site live with HTTPS January 23, 2026

### 1.1 Affiliate Network Setup
- [x] **1.1.1** MaxBounty account created and submitted
  - Email used: info@playtosave.net
  - Application ID: 784915
  - Affiliate Manager: Taylor Fleming (ext 244)
  - Application submitted with domain URL: ✓
  - Status: Awaiting phone interview (1-3 days)
  - Notes: ✅ SUBMITTED January 24, 2026 - Interview pending
- [ ] **1.1.2** MaxBounty phone interview completed
  - Interview date: [Pending]
  - Approval status: [Pending]
  - Notes: Will complete after building Phase 3.1-3.3 prototype
- [ ] **1.1.3** Applied to first 3 CPA offers
  - Target offers: Auto Insurance, Personal Loan, Life Insurance
  - Approval status: [Pending MaxBounty approval first]
  - Notes: Will apply after interview approval
- [ ] **1.1.4** Tracking links documented
  - Spreadsheet created: [Pending]
  - Notes: Will create after offer approval

### 1.2 Google Cloud Platform Setup
- [ ] **1.2.1** GCP Project created: `rooster-social-game`
  - Verification: Project ID = 
  - Screenshot: `tests/gcp_project.png`
- [ ] **1.2.2** APIs enabled (Cloud Run, BigQuery, Secret Manager)
  - Verification: Can see APIs in console
  - Screenshot: `tests/gcp_apis.png`
- [ ] **1.2.3** Billing account linked
  - Budget alerts set: $50 warning, $100 limit
  - Notes:
- [ ] **1.2.4** Service account created
  - Name: `rooster-app`
  - JSON key downloaded and stored securely
- [ ] **1.2.5** BigQuery dataset and tables created
  - Dataset: `rooster_data`
  - Tables: `game_events`, `conversion_signals`
  - View: `view_offer_performance`
  - Verification query result:
    ```sql
    SELECT COUNT(*) FROM `rooster_data.game_events`
    -- Result: [0 or number]
    ```

### 1.3 Meta Business Manager Setup
- [ ] **1.3.1** Business Manager account created
  - Business name: 
  - Business email: info@[yourdomain].com
  - URL: https://business.facebook.com/
  - Notes:
- [ ] **1.3.2** Payment method added
  - Card added: ✓
  - Spending limit set: $500/month
- [ ] **1.3.3** Meta Pixel created
  - Pixel ID: 
  - Pixel name: RoosterGamePixel
- [ ] **1.3.4** CAPI setup complete
  - Access token generated: ✓
  - Test event sent successfully: [Timestamp]
  - Screenshot: `tests/meta_test_event.png`
- [ ] **1.3.5** Custom conversions created
  - "Game Engagement" conversion: ✓
  - "Offer Click" conversion: ✓

### 1.4 Legal Foundation
- [ ] **1.4.1** Privacy Policy created
  - Method used: [TermsFeed / Termly.io / Custom]
  - File location: `app/templates/privacy.html`
- [ ] **1.4.2** Terms of Service created
  - File location: `app/templates/terms.html`
- [ ] **1.4.3** Affiliate disclosure created
  - Snippet saved: ✓
- [ ] **1.4.4** On-page disclaimers created
  - Game disclaimer: ✓
  - Claim button disclaimer: ✓
  - Footer links: ✓
- [ ] **1.4.5** Cookie consent banner implemented
  - Tool used: [Osano / Termly / Custom]
  - Tested: ✓

### 1.5 Domain & Hosting
- [x] **1.5.1** Domain registered (moved to 1.0.1 - COMPLETED FIRST)
  - Domain name: [See 1.0.1]
  - Registrar: [See 1.0.1]
  - WHOIS privacy enabled: ✓
- [x] **1.5.2** Professional email configured (moved to 1.0.2 - COMPLETED FIRST)
  - Email: info@[yourdomain].com
  - Notes: Use this email for all service signups
- [x] **1.5.3** Coming Soon page deployed (moved to 1.0.3 - COMPLETED FIRST)
  - Notes: These tasks moved to top of Phase 1 as prerequisite for affiliate applications
- [ ] **1.5.4** SSL certificate
  - Handled by Cloud Run: ✓
  - Notes: Will be configured during Phase 3 deployment

**Phase 1 Complete:** [ ] All tasks checked, all verifications documented

---

## 🎨 Phase 2: Creative Arsenal (Days 2-4)

### 2.1 Ad Creative Production
- [ ] **2.1.1** Ad Set A created (5 curiosity-driven ads)
  - A1: Spin wheel image (1080x1080) - Use Canva template
  - A2: Spin wheel video (15 sec) - Use CapCut
  - A3: Mystery box carousel - Use Canva
  - A4: UGC-style selfie video - iPhone screen recording
  - A5: High-production animation - Optional/Week 2
  - Folder: `creative_assets/ad_set_a/`
  - Notes: Reference CONTENT-CREATION-GUIDE.md for step-by-step
- [ ] **2.1.2** Ad Set B created (3 benefit-focused ads)
  - B1: Social proof ad (testimonial style)
  - B2: Urgency ad (limited spots)
  - B3: Direct benefit ad (savings calculator)
  - Folder: `creative_assets/ad_set_b/`
- [ ] **2.1.3** Asset organization complete
  - Naming convention followed: ✓
  - Thumbnails for tracking: ✓
- [ ] **2.1.4** Ad copy templates created
  - Primary text variants: 5 versions (see DECISION-MAKING-GUIDE.md)
  - Headlines: 5 versions
  - Descriptions: 3 versions
  - Location: Google Doc or creative_assets/copy.txt
- [ ] **2.1.5** Compliance check passed
  - No guaranteed money claims: ✓
  - No fake urgency: ✓
  - Matches landing page: ✓

### 2.2 Game Variants
- [ ] **2.2.1** Spin wheel built
  - Visual design complete: ✓
  - JavaScript working: ✓
  - Mobile tested: ✓
- [ ] **2.2.2** Scratch-off built
  - [Will build in Week 2]
- [ ] **2.2.3** Prize box built
  - [Will build in Week 3]
- [ ] **2.2.4** Variant tracking logic implemented
  - `variant_id` naming convention: ✓

### 2.3 A/B Testing Framework
- [ ] **2.3.1** Tracking spreadsheet created
  - Columns: variant_id, clicks, plays, conversions, CVR, EPC
  - Location: [Google Sheets URL or filename]
- [ ] **2.3.2** Test matrix planned
  - Week 1 plan documented: ✓
  - Week 2 plan documented: ✓
- [ ] **2.3.3** Creative refresh plan
  - Cadence: 2 new ads/week
  - Process documented: ✓

**Phase 2 Complete:** [ ] All tasks checked

---

## 💻 Phase 3: The Game App (Days 5-8)

### 3.1 Local Development Setup
- [x] **3.1.1** Project initialized
  - Folder structure created: ✓ (app/, tests/, docs/ organized)
  - Git initialized: ✓
  - Notes: ✅ COMPLETED January 25, 2026 - Clean workspace structure
- [x] **3.1.2** Dependencies installed
  - `requirements.txt` created: ✓ (with detailed explanations)
  - Virtual environment activated: ✓ (venv/)
  - All packages installed: ✓ (FastAPI, Jinja2, BigQuery, Meta SDK)
  - Notes: ✅ COMPLETED January 25, 2026
- [x] **3.1.3** Project structure created
  - All folders from spec exist: ✓ (app/templates, app/static/css, app/static/js)
  - Notes: ✅ COMPLETED January 25, 2026
- [x] **3.1.4** `.env` file created
  - All required vars present: ✓ (placeholders for GCP, Meta, Affiliate)
  - Validation test passed: ✓
  - Notes: ✅ COMPLETED January 25, 2026
- [x] **3.1.5** `.gitignore` created
  - .env excluded: ✓
  - venv excluded: ✓
  - Notes: ✅ VERIFIED January 25, 2026 - Already configured correctly
- [x] **3.1.6** Server running and tested
  - Uvicorn starts without errors: ✓
  - Root endpoint (/) shows success page: ✓
  - Health endpoint (/health) returns JSON: ✓
  - Auto-reload working: ✓
  - Verification: Screenshot shows green success page at http://localhost:8080
  - Notes: ✅ COMPLETED January 25, 2026

### 3.2 Pre-Qualifier
- [ ] **3.2.1** `templates/qualify.html` created
  - Form fields: age, state, fbclid
  - Styling complete: ✓
- [ ] **3.2.2** Logic implemented in `main.py`
  - GET route works: ✓
  - POST route works: ✓
  - Redirect logic works: ✓
- [ ] **3.2.3** Qualification rules configured
  - Rules in `config.py`: ✓
  - Customizable per offer: ✓
- [ ] **3.2.4** Tested
  - Qualified user test: ✓
  - Unqualified user test: ✓
  - fbclid preserved: ✓
  - Verification: [Screenshot or description]

### 3.3 Game Engine
- [ ] **3.3.1** `templates/game.html` created
  - Pixel code included: ✓
  - Disclaimers visible: ✓
  - Wheel canvas present: ✓
- [ ] **3.3.2** `static/js/wheel.js` implemented
  - Wheel spins: ✓
  - Lands on Gold: ✓
  - Confetti shows: ✓
  - Verification: Screen recording saved
- [ ] **3.3.3** `static/js/fraud.js` implemented
  - Mouse tracking works: ✓
  - Time tracking works: ✓
  - Score calculated: ✓
- [ ] **3.3.4** Backend route (`/app`) implemented
  - event_id generated: ✓
  - BigQuery logging works: ✓
  - Meta Pixel fires: ✓
- [ ] **3.3.5** Claim redirect implemented
  - Tracking URL constructed: ✓
  - InitiateCheckout fires: ✓
  - Redirect works: ✓

### 3.4 Meta Pixel Integration
- [ ] **3.4.1** Base code added to `base.html`
  - Pixel initialized: ✓
  - PageView fires: ✓
- [ ] **3.4.2** Custom events firing
  - ViewContent: ✓
  - AddToCart: ✓
  - InitiateCheckout: ✓
- [ ] **3.4.3** Tested with Pixel Helper
  - All events verified: ✓
  - Screenshot: `tests/pixel_helper.png`

### 3.5 BigQuery Integration
- [ ] **3.5.1** `bigquery_client.py` created
  - Connection works: ✓
  - Insert function works: ✓
  - Update function works: ✓
- [ ] **3.5.2** Tested writes
  - Query result shows event: ✓
  - Screenshot: `tests/bigquery_event.png`

### 3.6 Deployment
- [ ] **3.6.1** Dockerfile created
  - Builds successfully: ✓
- [ ] **3.6.2** Local Docker test
  - Container runs: ✓
  - App accessible at localhost:8080: ✓
- [ ] **3.6.3** Deployed to Cloud Run
  - Service URL: 
  - Accessible publicly: ✓
- [ ] **3.6.4** Custom domain mapped (optional)
  - Domain: 
  - DNS configured: ✓

### 3.7 Mobile Testing
- [ ] iPhone Safari tested
  - Wheel works: ✓
  - Animations smooth: ✓
  - Pixel fires: ✓
- [ ] Chrome Android tested
  - Responsive: ✓
  - No errors: ✓
- [ ] Edge cases tested
  - Missing fbclid handled: ✓
  - Slow internet handled: ✓

**Phase 3 Complete:** [ ] All tasks checked, app deployed and working

---

## 🔄 Phase 4: The Signal Loop (Days 9-10)

### 4.1 Postback Endpoint
- [ ] **4.1.1** Affiliate postback URLs configured
  - Impact.com: ✓
  - ClickBank: ✓
  - Test postback sent: ✓
- [ ] **4.1.2** `/postback` route created
  - Handles GET and POST: ✓
  - Validates secret: ✓
  - Returns 200: ✓
- [ ] **4.1.3** Conversion logging implemented
  - BigQuery insert works: ✓
  - fbclid lookup works: ✓
- [ ] **4.1.4** Validation added
  - Duplicate detection: ✓
  - Raw postback logging: ✓

### 4.2 Meta CAPI Integration
- [ ] **4.2.1** SDK installed
  - `facebook-business` added to requirements: ✓
- [ ] **4.2.2** `meta_capi.py` created
  - Event construction works: ✓
  - API call succeeds: ✓
- [ ] **4.2.3** Response handling
  - Success logged: ✓
  - Errors logged: ✓
- [ ] **4.2.4** Retry logic added
  - Retries on failure: ✓

### 4.3 Testing & Validation
- [ ] **4.3.1** Local postback test
  - curl command works: ✓
  - Response correct: ✓
- [ ] **4.3.2** Test Events verification
  - Event appears in Meta: ✓
  - Match quality >5.0: ✓
  - Screenshot: `tests/capi_test_event.png`
- [ ] **4.3.3** Real affiliate test
  - Test postback from network: ✓
  - Full flow verified: ✓
- [ ] **4.3.4** Error monitoring set up
  - Cloud Logging alerts: ✓
- [ ] **4.3.5** Match quality monitored
  - Score: [Number]

### 4.4 Edge Cases
- [ ] Duplicate postbacks handled: ✓
- [ ] Missing fbclid handled: ✓
- [ ] Delayed postbacks handled: ✓

**Phase 4 Complete:** [ ] Signal loop working end-to-end

---

## 📊 Phase 5: Analytics & Optimization (Days 11-12)

### 5.1 BigQuery Analytics
- [ ] **5.1.1** `view_offer_performance` created
  - Query returns results: ✓
- [ ] **5.1.2** `daily_performance` view created
- [ ] **5.1.3** `fraud_analysis` view created
- [ ] **5.1.4** `conversion_funnel` view created

### 5.2 Optimization Scripts
- [ ] **5.2.1** Kill script created
  - Identifies losers: ✓
  - Pauses variants: ✓
- [ ] **5.2.2** Scale script created
  - Identifies winners: ✓
  - Increases budgets: ✓
- [ ] **5.2.3** Decision rules table documented
- [ ] **5.2.4** Daily optimization routine scheduled

### 5.3 Monitoring & Alerts
- [ ] **5.3.1** Cloud Monitoring alerts set up
  - Zero conversions alert: ✓
  - High fraud alert: ✓
  - CAPI error alert: ✓
  - Postback volume alert: ✓
- [ ] **5.3.2** Data Studio dashboard created
  - URL: 
  - 5 panels configured: ✓
- [ ] **5.3.3** Daily email report set up
  - Recipient: 
  - Test email received: ✓
- [ ] **5.3.4** Slack integration (optional)
  - Webhook configured: ✓
  - Test alert sent: ✓

### 5.4 Weekly Review
- [ ] Process documented: ✓
- [ ] Template created: ✓

### 5.5 A/B Testing Framework
- [ ] **5.5.1** Significance calculator created
- [ ] **5.5.2** Test schedule documented

**Phase 5 Complete:** [ ] Analytics fully operational

---

## 🚀 Phase 6: Launch (Days 13+)

### 6.1 Primary Campaign
- [ ] **6.1.1** Campaign created in Meta Ads
  - Name: AlphaRooster_Cold_Test_[Month][Year]
  - Budget: $20/day, $100 limit
- [ ] **6.1.2** Ad set created
  - Targeting configured: ✓
  - Placements selected: ✓
- [ ] **6.1.3** Ads created (5 variants)
  - All ads uploaded: ✓
  - fbclid parameter in URLs: ✓
- [ ] **6.1.4** Launch checklist completed
  - All items checked: ✓
- [ ] **Campaign launched:** [Date & Time]

### 6.2 Retargeting Campaign
- [ ] **6.2.1** Custom audience created
  - Name: GamePlayers_NoConversion_7d
  - Size: [Number after 48h]
- [ ] **6.2.2** Retargeting campaign created
  - Budget: $10/day, $50 limit
- [ ] **6.2.3** Retargeting ads created
  - 3 variants created: ✓
- [ ] **Campaign launched:** [Date & Time - after 48h]

### 6.3 Hour-by-Hour Monitoring (Days 1-3)
- [ ] **Day 1 - Hour 1**
  - Ads approved: ✓
  - Clicks arriving: ✓
  - BigQuery logging: ✓
- [ ] **Day 1 - Hour 2**
  - Game engagement >60%: ✓
- [ ] **Day 1 - Hour 3**
  - Claim rate >30%: ✓
- [ ] **Day 1 - Hour 6**
  - Pixel events firing: ✓
  - Fraud score <0.3: ✓
- [ ] **Day 1 - End of day results:**
  - Clicks: 
  - Plays: 
  - Claims: 
  - Conversions: 
- [ ] **Day 2 - Monitoring**
  - First postback received: [Time]
  - CAPI events verified: ✓
- [ ] **Day 3 - First optimization**
  - Worst ad paused: [Ad ID]
  - Switched to Conversion objective: ✓

### 6.4 Optimization (Days 4-7)
- [ ] **Day 4:** CTR analysis, budget adjustments
- [ ] **Day 5:** Retargeting launched, funnel analysis
- [ ] **Day 6-7:** ROAS calculation
  - Spent: $
  - Revenue: $
  - ROAS: x
  - Decision: [Scale / Pause / Adjust]

### 6.5 Common Problems (if encountered)
- [ ] Zero conversions: [Resolution steps taken]
- [ ] High fraud: [Resolution steps taken]
- [ ] High CPC: [Resolution steps taken]
- [ ] Low engagement: [Resolution steps taken]

### 6.6 Week 1 Success Criteria
- [ ] $150 spent
- [ ] 300-500 clicks
- [ ] 10-20 conversions
- [ ] $150-400 revenue
- [ ] 1.0-2.5x ROAS
- [ ] 1-2 winning combos identified

**Phase 6 Complete:** [ ] Week 1 test finished, scaling decision made

---

## 🎯 Next Steps (Post-Launch)

Based on Week 1 results:
- [ ] **If successful (ROAS >2x):** Scale winning variants to $50/day
- [ ] **If break-even (ROAS 1-2x):** Test new offers, continue optimizing
- [ ] **If unprofitable (ROAS <1x):** Pause, analyze, pivot strategy

**Scaling Plan:** [To be determined based on results]

---

## 📝 Notes & Learnings

### What Worked:
- 

### What Didn't Work:
- 

### Key Insights:
- 

### Changes to Plan:
- 

---

**Last Updated:** [Date]
