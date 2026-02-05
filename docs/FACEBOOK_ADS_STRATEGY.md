# Facebook Ads to MaxBounty: Mechanical Arbitrage Strategy

**Last Updated:** February 5, 2026  
**Status:** Pre-Launch Phase  
**Capital Allocation:** $20,000 (Float)  
**Risk Tolerance:** Low (White Hat Only)

---

## Abstract

This document presents a complete mechanical arbitrage system for generating profitable leads through Facebook advertising and CPA affiliate networks. The strategy eliminates guesswork by establishing clear operating rules: Hold campaigns for 48 hours minimum, Kill at 3× payout with zero conversions ($20.25 for $6.75 offers), and Scale winners by 20% every 48 hours. Revenue flows through a gamified bridge page (spin-to-win wheel) that converts cold traffic into affiliate leads while maintaining Facebook policy compliance. The 3:2:2 Dynamic Creative framework (3 image angles × 2 text variants × 2 headlines = 12 ad combinations) allows Meta's algorithm to optimize performance without manual A/B testing. With proper infrastructure (CAPI event deduplication, postback conversion tracking, BigQuery analytics), account seasoning ($15 warming campaign), and disciplined execution of operating rules, this system targets 1.5× ROAS in month one, scaling to 2.0×–3.0× ROAS by month three, ultimately reaching $20,000/month topline revenue through offer diversification and creative volume. Success depends 40% on creative iteration speed, 30% on offer diversification, 20% on data optimization (CAPI + postbacks), and 10% on campaign velocity—making this a repeatable, scalable playbook for social-to-CPA arbitrage.

---

## Key Terminology

**For newcomers to performance marketing—here's what the jargon means:**

### Revenue & Profitability Terms
- **CPA (Cost Per Acquisition):** You earn a fixed amount ($6.75) each time someone completes an action (fills out insurance quote). Unlike ads that pay per click, you only earn when the user converts.
- **ROAS (Return on Ad Spend):** If you spend $100 on ads and earn $150 in commissions, your ROAS is 1.5× (or 150%). Target: 1.5× minimum, 3.0× at scale.
- **Arbitrage:** Buying traffic cheap (Facebook ads at $0.50/click) and selling it expensive (MaxBounty pays $6.75/conversion). Profit = difference between what you pay and what you earn.
- **Payout:** The amount the affiliate network pays you per conversion ($6.75 for our insurance offer).
- **EPC (Earnings Per Click):** Average revenue per click. If 100 clicks generate 3 conversions at $6.75 each, EPC = $20.25 ÷ 100 = $0.20/click.

### Facebook Ads Terms
- **CPC (Cost Per Click):** What you pay Facebook each time someone clicks your ad. Target: $0.50–$0.75.
- **CTR (Click-Through Rate):** Percentage of people who see your ad and click it. Target: >1.0% (1 in 100 people click).
- **CVR (Conversion Rate):** Percentage of clicks that become paid conversions. Target: >3% (3 in 100 clicks convert).
- **Dynamic Creative:** Facebook tests all combinations of your images, headlines, and text to find the best-performing combo automatically.
- **CBO (Campaign Budget Optimization):** Facebook controls budget distribution across ad sets (we turn this OFF initially for manual control).
- **Advantage+ Placements:** Facebook chooses where to show ads (Feed, Stories, Reels) based on performance (we use this).

### Technical Infrastructure Terms
- **CAPI (Conversions API):** Server-to-server connection that tells Facebook when conversions happen. Improves ad targeting accuracy and bypasses ad blockers.
- **Postback:** Affiliate network sends you a notification when someone converts, so you can track revenue in real-time.
- **Event Deduplication:** Prevents counting the same conversion twice (browser pixel + server CAPI both fire, but use same `event_id` to merge).
- **fbclid:** Facebook Click ID—unique tracking parameter in URLs that identifies which ad click generated a conversion.
- **Pixel:** JavaScript code on your website that tracks user actions (page views, button clicks, purchases) and sends data to Facebook.

### Campaign Management Terms
- **Bridge Page:** Intermediate page between ad and offer (our wheel game). Filters traffic, increases engagement, maintains policy compliance.
- **Creative:** The visual/written content in your ad (image, headline, body text). Not the same as "creativity"—it's the actual ad asset.
- **Ad Set:** Group of ads targeting the same audience with the same budget. One campaign can have multiple ad sets.
- **Account Seasoning:** Running low-budget, safe campaigns ($15 total) to build trust with Facebook before launching aggressive CPA campaigns.
- **Warming Campaign:** The $15 Page Likes campaign that seasons your ad account (shows Facebook you're a legitimate advertiser).

### Operating Rules Terms
- **Hold:** Wait 48 hours before making any decisions. Prevents killing winners too early.
- **Kill:** Turn off ad sets that spend 3× payout ($20.25) with zero conversions. They're statistically unlikely to be profitable.
- **Scale:** Increase budget by 20% every 48 hours on winning ad sets (those hitting ROAS targets).
- **Refresh:** Replace underperforming creatives weekly to maintain ad fatigue resistance.

### Offer & Network Terms
- **MaxBounty:** CPA affiliate network connecting advertisers (insurance companies) with marketers (you). They handle payments, tracking, compliance.
- **Lead:** Person who completes the desired action (submits insurance quote with valid contact info). This is what you get paid for.
- **Offer Cap:** Maximum conversions allowed per day (our offer caps at 25 leads/day). Prevents affiliate network from being overwhelmed.
- **Sub ID:** Tracking parameter you add to links (e.g., `subId1={{fbclid}}`) to match conversions back to specific ad clicks.

### Analytics Terms
- **BigQuery:** Google's data warehouse where we store all events (clicks, game plays, conversions) for analysis.
- **Event ID:** Unique identifier for each user interaction (e.g., `evt_1234`). Used for deduplication and matching browser events to server events.
- **Conversion Signal:** Data sent to Facebook via CAPI indicating a conversion happened (includes value, timestamp, user data).

---

## Table of Contents
1. [Strategic Overview](#strategic-overview)
2. [Phase 1: Infrastructure Build](#phase-1-infrastructure-build-days-1-3)
3. [Phase 2: Account Seasoning](#phase-2-account-seasoning-days-4-7)
4. [Phase 3: Creative Development](#phase-3-creative-development-days-8-10)
5. [Phase 4: Campaign Launch](#phase-4-campaign-launch-days-11-14)
6. [Phase 5: Operating Rules](#phase-5-operating-rules-daily-routine)
7. [Master Checklist](#master-checklist)
8. [Performance Benchmarks](#performance-benchmarks)
9. [Risk Management](#risk-management)

---

## Strategic Overview

### Objective
Generate profitable leads through Facebook advertising and monetize via MaxBounty CPA offers using a gamified bridge page (Alpha Rooster wheel game).

### Business Model
```
User clicks Facebook ad 
  → Lands on playtosave.net/game
  → Plays wheel game (engagement)
  → Redirects to MaxBounty offer
  → Completes insurance quote
  → We earn $6.75/lead
```

### Success Criteria
- **Phase 1 Goal:** ROAS ≥ 1.5x (earn $1.50 for every $1.00 spent)
- **Phase 2 Goal:** ROAS ≥ 2.0x (earn $2.00 for every $1.00 spent)
- **Phase 3 Goal:** ROAS ≥ 3.0x (scale to $200+/day profitably)

### Key Principles
1. **Mechanical, Not Emotional:** Follow rules systematically, avoid impulse changes
2. **Data Before Optimization:** Minimum 48 hours before making decisions
3. **White Hat Only:** No policy violations, no shortcuts, sustainable long-term
4. **Kill Fast, Scale Slow:** Cut losers immediately, scale winners gradually

---

## Phase 1: Infrastructure Build (Days 1-3)

**Objective:** Build the technical foundation before spending a dollar on ads.

### 1.1 Server-Side Tracking (CAPI) with Deduplication

**Why it matters:** Facebook needs accurate conversion data to optimize ads. Without CAPI, you're flying blind.

**Implementation:**

#### Browser-Side (Meta Pixel)
```html
<!-- Meta Pixel Base Code -->
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

#### Event Tracking with Deduplication
```javascript
// Generate unique event ID (UUID v4)
const eventId = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
  const r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
  return v.toString(16);
});

// Fire browser event with event_id
fbq('track', 'Lead', {
  content_name: 'Auto Insurance Quote',
  content_category: 'Insurance',
  value: 6.75,
  currency: 'USD'
}, {
  eventID: eventId  // Critical: This must match server event
});

// Also send event_id to your backend
fetch('/api/track-conversion', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    event_id: eventId,
    event_name: 'Lead',
    fbclid: new URLSearchParams(window.location.search).get('fbclid')
  })
});
```

#### Server-Side (CAPI)
```python
# Backend endpoint receives conversion
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.user_data import UserData

def send_capi_event(event_id, fbclid, user_ip, user_agent):
    """Send conversion event to Facebook CAPI"""
    
    # Initialize API
    FacebookAdsApi.init(access_token=META_ACCESS_TOKEN)
    
    # Build user data
    user_data = UserData(
        client_ip_address=user_ip,
        client_user_agent=user_agent,
        fbc=f'fb.1.{int(time.time())}.{fbclid}'  # Facebook Click ID
    )
    
    # Build event
    event = Event(
        event_name='Lead',
        event_time=int(time.time()),
        event_id=event_id,  # MUST match browser event_id
        user_data=user_data,
        custom_data={
            'content_name': 'Auto Insurance Quote',
            'content_category': 'Insurance',
            'value': 6.75,
            'currency': 'USD'
        },
        event_source_url=f'https://playtosave.net/game',
        action_source='website'
    )
    
    # Send to Facebook
    event_request = EventRequest(
        events=[event],
        pixel_id=META_PIXEL_ID
    )
    
    response = event_request.execute()
    return response
```

**Verification:**
- Go to Meta Events Manager → Test Events
- Trigger a test conversion on your site
- You should see **one event** with two sources: Browser + Server
- Match rate should be > 80%

---

### 1.2 Bridge Page Construction

**Current Status:** ✅ Built (playtosave.net running on Cloud Run)

**Requirements:**
- [x] Fast load speed (< 2 seconds)
- [x] Mobile responsive
- [x] Engaging pre-qualifier + game
- [x] Clear value proposition
- [ ] Legal footer with required links

**The "Safe" Footer:**

Add to `app/templates/base.html`:

```html
<footer class="legal-footer">
  <div class="footer-links">
    <a href="/privacy">Privacy Policy</a> | 
    <a href="/terms">Terms of Service</a> | 
    <a href="/contact">Contact Us</a> | 
    <a href="/dmca">DMCA</a>
  </div>
  <div class="disclaimer">
    <p>
      <strong>Affiliate Disclosure:</strong> We may earn a commission if you complete an offer through our links.
      Your participation is completely free.
    </p>
    <p class="copyright">
      © 2026 PlayToSave. All rights reserved.
    </p>
  </div>
</footer>

<style>
.legal-footer {
  background: #f8f9fa;
  padding: 40px 20px;
  margin-top: 60px;
  border-top: 1px solid #dee2e6;
  text-align: center;
  font-size: 14px;
  color: #6c757d;
}

.footer-links {
  margin-bottom: 20px;
}

.footer-links a {
  color: #007bff;
  text-decoration: none;
  margin: 0 10px;
}

.disclaimer {
  max-width: 800px;
  margin: 0 auto;
  line-height: 1.6;
}

.disclaimer strong {
  color: #495057;
}
</style>
```

**Note:** The old "This site is not affiliated with Facebook" disclaimer is **no longer required** as of 2019 and actually makes you look suspicious. Focus on clear affiliate disclosure instead.

---

### 1.3 Domain Validation

**Tasks:**
- [ ] Verify domain in Facebook Business Manager
  - Go to Business Manager → Business Settings → Brand Safety → Domains
  - Add playtosave.net
  - Add DNS TXT record to Namecheap: `facebook-domain-verification=xxxxx`
  - Wait 24-48 hours for verification

- [ ] Create support email
  - Email: support@playtosave.net
  - Setup: Email forwarding in Namecheap
  - Test: Send test email and verify receipt

- [ ] Test page load speed
  - Tool: https://pagespeed.web.dev/
  - Target: Mobile score > 80, Desktop score > 90
  - Fix: Optimize images, enable compression, minify JS/CSS

---

### 1.4 Postback Endpoint (CRITICAL)

**Why it matters:** MaxBounty sends a webhook when someone completes the offer. Without this, you can't calculate ROAS.

**Implementation:**

```python
# app/main.py - Add this route
@app.get("/postback")
async def maxbounty_postback(
    request: Request,
    subId1: str = Query(..., alias="subId1"),  # This is the event_id
    payout: float = Query(...),
    secret: str = Query(...)
):
    """
    MaxBounty fires this URL when user completes insurance quote:
    https://playtosave.net/postback?subId1=EVENT_ID&payout=6.75&secret=YOUR_SECRET
    """
    
    # Security: Verify secret token
    if secret != AFFILIATE_SECRET:
        raise HTTPException(status_code=401, detail="Invalid secret")
    
    # Log conversion to BigQuery
    event_id = subId1
    conversion_time = datetime.utcnow()
    
    bq_client.insert_rows_json(
        'rooster_data.conversion_signals',
        [{
            'event_id': event_id,
            'payout': payout,
            'status': 'approved',
            'conversion_time': conversion_time.isoformat()
        }]
    )
    
    # Send conversion event to Facebook CAPI
    # (Use the event_id to match with browser event)
    send_capi_conversion(event_id, payout)
    
    return {"status": "success", "event_id": event_id}
```

**MaxBounty Setup:**
1. Go to MaxBounty → Offer Details → Postback URL
2. Enter: `https://playtosave.net/postback?subId1=[s1]&payout=[payout]&secret=YOUR_SECRET_TOKEN`
3. Click "Send Test Postback" to verify
4. Check BigQuery for test conversion record

---

## Phase 2: Account Seasoning (Days 4-7)

**Objective:** Make your Facebook ad account look legitimate before spending big money.

**Why it matters:** New accounts that immediately spend $100+/day get flagged as fraud. The $15 "burn-in" period builds trust.

### 2.1 Facebook Business Page Setup

**Tasks:**
- [ ] Create Business Page
  - Name: "PlayToSave" (matches domain)
  - Category: "Financial Service"
  - Description: "Helping Americans save money on insurance and essential services."

- [ ] Upload branding assets
  - Profile picture: 400x400px logo (use Canva)
  - Cover photo: 820x312px banner with tagline
  - Call-to-action button: "Learn More" → https://playtosave.net

- [ ] Create 3 generic posts (no selling)

**Post 1 - Educational Tip:**
```
💡 Insurance Savings Tip:

Did you know that 70% of drivers are overpaying for auto insurance?

Here's why: Most people haven't shopped around in 3+ years. Insurance companies count on this.

The average driver saves $416/year just by comparing quotes.

When was the last time you compared rates? 🤔
```

**Post 2 - Engagement Question:**
```
Quick poll: What's the HARDEST part about managing your insurance?

A) Finding the time to shop around
B) Understanding what coverage you actually need
C) Dealing with pushy salespeople
D) Comparing dozens of confusing quotes

Drop your answer below 👇
```

**Post 3 - Helpful Fact:**
```
📊 Insurance Fact of the Day:

Your credit score affects your insurance rates in 47 states.

Improving your credit from "Fair" to "Good" can save you $1,000+/year on premiums.

Not sure what your credit score is? Check for free at AnnualCreditReport.com

#InsuranceTips #MoneyMatters
```

---

### 2.2 The "Burn" Spend Campaign

**Objective:** Spend $15 over 3 days to authorize your payment method and prove you're not a bot.

**Campaign Setup:**

| Setting | Value |
|---------|-------|
| **Campaign Objective** | Engagement |
| **Campaign Name** | "Page Warming - Feb 2026" |
| **Budget Type** | Daily Budget |
| **Daily Budget** | $5.00 |
| **Duration** | 3 days |
| **Total Spend** | $15.00 |

**Ad Set Settings:**

| Setting | Value |
|---------|-------|
| **Conversion Location** | Facebook Page |
| **Audience** | United States, Age 25-65 |
| **Placements** | Advantage+ (Automatic) |

**Ad Creative:**

- **Format:** Single image post
- **Image:** Your best Facebook post (the insurance tip one)
- **Primary Text:** "Follow PlayToSave for money-saving tips on insurance, utilities, and more! 💰"
- **Headline:** "Get Smart About Insurance"
- **Call-to-Action:** "Like Page"

**Success Metrics:**
- ✅ $15 spent over 3 days
- ✅ 50-200 page likes (doesn't matter, just warming the account)
- ✅ No ad rejections or account warnings

**What to avoid:**
- ❌ Don't promote your game during warming
- ❌ Don't ask for clicks to your website
- ❌ Don't mention MaxBounty or affiliate offers
- ❌ Don't increase budget above $5/day

---

## Phase 3: Creative Development (Days 8-10)

**Objective:** Build the 3:2:2 creative matrix for Dynamic Creative testing.

### 3.1 The 3 Angles Framework

Every winning ad follows one of three psychological patterns:

#### Angle 1: Logic (Rational Savings)
**Hook:** Appeals to smart financial decisions  
**Target:** Analytical thinkers, budget-conscious families

**Example Headlines:**
- "Compare 10+ Insurance Providers in Under 2 Minutes"
- "See How Much You Could Save on Auto Insurance"
- "Americans Are Saving an Average of $416/Year"

**Example Body Copy:**
```
Most drivers are overpaying for auto insurance — simply because they haven't compared rates in years.

Get personalized quotes from 10+ top-rated providers in minutes. No phone calls. No pushy salespeople.

Tap below to see if you qualify for lower rates 👇
```

**Imagery:**
- Calculator or savings graphic
- Side-by-side rate comparison
- Happy family with car
- Blue/green color scheme (trust, stability)

---

#### Angle 2: Fear/Pain (Rising Costs)
**Hook:** Triggers urgency around increasing rates  
**Target:** People who recently saw rate increases

**Example Headlines:**
- "Why Did My Insurance Rate Just Go Up?"
- "Your Auto Insurance Might Be Costing You $100/Month Too Much"
- "Don't Get Stuck Overpaying for Coverage You Don't Need"

**Example Body Copy:**
```
Insurance companies are raising rates at record levels — up 20% since 2023.

But here's what they don't tell you: You're not stuck with those higher rates.

Compare quotes in 2 minutes and see how much you could save. Most drivers save $400+/year.

See your rate now 👇
```

**Imagery:**
- Trending upward price chart
- Frustrated driver looking at bill
- "Before/After" rate comparison
- Red/orange color scheme (urgency, alert)

---

#### Angle 3: Curiosity (Weird Trick)
**Hook:** Pattern interrupt, makes people stop scrolling  
**Target:** Everyone (broad appeal)

**Example Headlines:**
- "This 2-Minute Trick Could Save You $500/Year on Auto Insurance"
- "Why Smart Drivers Are Using This Simple Tool"
- "The Insurance Industry Doesn't Want You to Know This"

**Example Body Copy:**
```
There's a little-known way to slash your auto insurance costs — and it only takes 2 minutes.

Insurance companies count on you NOT comparing rates. That's how they keep charging you more every year.

Play our quick game to see if you qualify for lower rates 🎡

(Spoiler: Most people save $400+/year)
```

**Imagery:**
- Wheel game screenshot (our actual game!)
- "Secret" or lightbulb imagery
- Surprising statistic graphic
- Purple/yellow color scheme (intrigue, energy)

---

### 3.2 Image/Video Generation

**Option 1: Canva (Recommended for Speed)**
1. Go to Canva.com → "Facebook Ad" template
2. Search template: "Insurance" or "Finance"
3. Customize with your headline
4. Export 3 variations (one per angle)
5. Dimensions: 1080x1080px (square)

**Option 2: Midjourney (Better Quality)**
Prompts:
```
Angle 1 (Logic):
"professional clean minimal insurance comparison chart, happy family with car, calculator interface, blue and white color scheme, modern financial app screenshot style --ar 1:1 --v 6"

Angle 2 (Fear):
"frustrated person looking at rising bills, red warning graph trending upward, insurance rate increase alert, concerned expression, documentary photography style --ar 1:1 --v 6"

Angle 3 (Curiosity):
"colorful prize wheel game interface, insurance savings theme, golden coins, excited winners, gamified app design, vibrant purple and yellow colors --ar 1:1 --v 6"
```

**Option 3: Video (Highest CTR)**
- Record 15-second screen recording of wheel game
- Add text overlay: "Spin to see if you qualify for savings"
- Export as MP4 (1080x1080px)
- Tools: OBS Studio (free) + CapCut (free editing)

---

### 3.3 The 3:2:2 Creative Matrix

**What to create:**

| Element | Quantity | Examples |
|---------|----------|----------|
| **Images/Videos** | 3 | Logic image, Fear image, Curiosity video |
| **Primary Text** | 2 | Long-form story (200 words), Short-form hook (50 words) |
| **Headlines** | 2 | Benefit-focused ("Save $500/Year"), Question-focused ("Are You Overpaying?") |

**Total combinations:** 3 × 2 × 2 = **12 ad variations** tested automatically by Facebook

---

### 3.4 Ad Copy Templates

**Primary Text Option 1 (Long-Form):**
```
Most Americans are overpaying for auto insurance — by an average of $416/year.

Why? Because insurance companies count on you NOT shopping around.

Here's the truth: Your rates should go DOWN over time (as your car depreciates). But instead, they keep raising them every year.

The fix is simple: Compare quotes every 12 months.

We built a quick game to make this fun instead of boring. Play the wheel, answer a few questions, and see personalized quotes from 10+ top-rated providers.

It takes 2 minutes. No phone calls. No pushy salespeople.

Ready to see how much you could save? Tap below 👇
```

**Primary Text Option 2 (Short-Form):**
```
Insurance companies are counting on you NOT comparing rates.

Don't let them.

Play our 2-minute game and see if you qualify for lower rates 🎡

Most drivers save $400+/year just by shopping around.

Your turn 👇
```

**Headline Option 1:**
"See If You Qualify for Lower Insurance Rates"

**Headline Option 2:**
"Are You Overpaying for Auto Insurance?"

---

### 3.5 Asset Organization

**Folder structure:**
```
/creative_assets/
  /batch_001_feb_2026/
    logic_image.png
    fear_image.png
    curiosity_video.mp4
    primary_text_long.txt
    primary_text_short.txt
    headlines.txt
    performance_log.xlsx  (track which combos win)
```

**Naming convention:**
- `[angle]_[format]_[date].png`
- Examples: `logic_image_feb05.png`, `curiosity_video_feb05.mp4`

---

## Phase 4: Campaign Launch (Days 11-14)

**Objective:** Launch first test campaign with strict operating rules.

### 4.1 Campaign Structure

**Campaign Level:**

| Setting | Value | Reasoning |
|---------|-------|-----------|
| **Campaign Objective** | Sales (or Leads if Sales unavailable) | We want conversions, not clicks |
| **Campaign Name** | "AutoIns - Broad - Feb2026 - Test" | Clear naming for tracking |
| **Campaign Budget Optimization** | OFF | Manual control allows faster kill decisions |
| **Buying Type** | Auction | Standard delivery, not Reach & Frequency |

---

**Ad Set Level:**

| Setting | Value | Reasoning |
|---------|-------|-----------|
| **Ad Set Name** | "Cold - US - 25-65 - Homeowners" | Describes audience |
| **Conversion Location** | Website | Our bridge page (playtosave.net) |
| **Pixel Event** | Lead | Fires when wheel game completes |
| **Dynamic Creative** | ON | Enables 3:2:2 auto-testing |
| **Daily Budget** | $20.00 | Conservative starting point |
| **Start Date** | [Tomorrow at 12:00 AM] | Launch overnight for fresh day |
| **End Date** | Ongoing | Will manually pause if needed |

**Targeting:**

| Setting | Value | Reasoning |
|---------|-------|-----------|
| **Location** | United States | MaxBounty offer is US-only |
| **Age** | 25-65 | Car insurance target demo |
| **Gender** | All | Don't exclude anyone |
| **Detailed Targeting** | Homeowners (Interest) | Narrows to financially stable audience |
| **Exclude** | Current customers of client | (Not applicable for CPA) |
| **Languages** | English (All) | Match offer language |

**Placements:**

| Setting | Value | Reasoning |
|---------|-------|-----------|
| **Placement** | Advantage+ Placements | Let Meta optimize across Facebook, Instagram, Audience Network |
| **Manual Placements** | Do NOT use | Advantage+ performs better in 2024+ |

---

**Ad Level (Dynamic Creative Settings):**

| Setting | Value |
|---------|-------|
| **Ad Name** | "DynamicCreative_AutoIns_Batch001" |
| **Format** | Dynamic Creative |
| **Primary Text** | [Upload 2 variants from Section 3.4] |
| **Headline** | [Upload 2 variants from Section 3.4] |
| **Description** | "Compare 10+ providers. Fast. Free." |
| **Media** | [Upload 3 images/videos from Section 3.2] |
| **Call-to-Action** | "Learn More" (not "Sign Up" - less pushy) |
| **Destination** | https://playtosave.net/game |

**URL Parameters (Critical for Tracking):**
```
https://playtosave.net/game?utm_source=facebook&utm_medium=cpc&utm_campaign=autoins_feb2026&fbclid={{fbclid}}
```

**Why important:**
- `fbclid` parameter connects ad click → game play → conversion
- Without this, CAPI attribution breaks

---

### 4.2 Pre-Launch Checklist

**24 Hours Before Launch:**
- [ ] Meta Pixel firing correctly on /game page (test in Events Manager)
- [ ] CAPI endpoint tested and working (send test event)
- [ ] MaxBounty postback URL configured (send test postback)
- [ ] BigQuery tables ready to receive data
- [ ] All 3 images + 2 text variants uploaded to ad
- [ ] URL parameters include `{{fbclid}}`
- [ ] Daily budget set to $20 (NOT $200)
- [ ] Campaign scheduled to start at 12:00 AM tomorrow

**6 Hours Before Launch:**
- [ ] Double-check: Pixel ID is correct (not a dummy ID)
- [ ] Double-check: Postback secret token matches your .env file
- [ ] Double-check: Credit card has sufficient funds ($500+ available)
- [ ] Screenshot campaign settings for documentation

**1 Hour Before Launch:**
- [ ] Review ad copy for policy violations (no guarantees, no exaggerated claims)
- [ ] Test funnel one more time: Click ad → Play game → Redirect to offer
- [ ] Notify MaxBounty affiliate manager you're launching (optional but courteous)

---

### 4.3 The Launch Rule

**Timing matters:**

✅ **DO:**
- Create campaigns in the evening (6-10 PM)
- Schedule them to go live at 12:00 AM (midnight) in ad account timezone
- Let them run from 12:00 AM on Day 1

❌ **DON'T:**
- Launch mid-day (wastes learning time)
- Launch on Friday (weekend traffic behaves differently)
- Launch multiple campaigns same day (can't isolate variables)

**Why midnight?**
- Gives Facebook a full 24-hour day to optimize
- Avoids partial day data (harder to analyze)
- Aligns with daily budget reset

---

## Phase 5: Operating Rules (Daily Routine)

**Objective:** Systematic decision-making to maximize profit and minimize waste.

### 5.1 The "Hold" Rule (Days 1-2)

**Rule:** For the first 48 hours after launch, DO NOTHING.

**Actions allowed:**
- ✅ Check dashboard to see spend/impressions
- ✅ Monitor for policy violations or ad rejections
- ✅ Verify pixel events are firing in Events Manager

**Actions FORBIDDEN:**
- ❌ Pausing ad sets
- ❌ Adjusting budgets
- ❌ Changing targeting
- ❌ Editing ad copy or images
- ❌ Adding new ads to the campaign

**Why?**
- Facebook's algorithm needs 24-48 hours to exit "Learning Phase"
- Any edit resets the learning period
- You'll kill good ads before they have a chance to perform

**What if it's clearly terrible after 6 hours?**
- Still wait. CTR looks bad in first 6 hours for EVERY campaign.
- Exception: If you get policy violation warning, fix immediately.

---

### 5.2 The "Kill" Rule (Day 3+)

**Rule:** Turn off ad sets that fail to convert after hitting spend threshold.

**Formula:**
```
IF ad_set_spend > (3 × payout) AND conversions = 0
THEN pause ad set
```

**For your offer ($6.75 payout):**
- Payout: $6.75
- Kill threshold: $20.25 (3× payout)
- Decision: If you've spent $20.25 and gotten 0 leads, turn it off

**Why 3x instead of 2x?**
- 2x doesn't give enough data (only ~40 clicks at $0.50 CPC)
- Industry conversion rates for insurance are 2-5%
- At 3% CVR, you need 33 clicks to expect 1 conversion
- 3x payout = ~40 clicks = statistically significant sample

**How to execute:**
1. Every morning, pull report: Ad Set Performance → Last 3 Days
2. Filter: Conversions = 0
3. Check spend column
4. Pause any ad sets over $20.25 with no conversions
5. Log in spreadsheet: Date, Ad Set Name, Spend, Reason

**DO NOT:**
- Kill an ad set with 1 conversion but negative ROAS yet (give it time)
- Kill entire campaign if only 1 ad set is failing (isolate the problem)

---

### 5.3 The "Scale" Rule (Day 4+)

**Rule:** Increase budget on profitable ad sets, but SLOWLY.

**Formula:**
```
IF roas ≥ 1.5 AND ad_set_has_run > 48_hours
THEN increase_budget_by_20_percent
WAIT 48 hours
REPEAT
```

**Example:**
| Day | Budget | Spend | Revenue | ROAS | Action |
|-----|--------|-------|---------|------|--------|
| 1-2 | $20 | $40 | $27 | 0.68x | Wait (learning phase) |
| 3-4 | $20 | $40 | $60.75 | 1.52x | ✅ Increase to $24 |
| 5-6 | $24 | $48 | $81 | 1.69x | ✅ Increase to $28.80 |
| 7-8 | $28.80 | $57.60 | $94.50 | 1.64x | ✅ Increase to $34.56 |

**Why 20% increments?**
- Larger increases (50%+) shock the algorithm and reset learning
- Smaller increases (10%) scale too slowly
- 20% is the sweet spot Facebook recommends

**When to stop scaling:**
- ROAS drops below 1.3x for 3+ days in a row
- Daily cap on MaxBounty offer is hit (25 leads/day = $168 revenue max)
- You've reached your comfortable daily budget limit

**Advanced:** Once you hit $100/day profitably, switch to Campaign Budget Optimization (CBO) and let Facebook distribute budget across multiple ad sets automatically.

---

### 5.4 Daily Routine Checklist

**Every morning (9:00 AM):**
- [ ] Check overnight spend (should be ~$20 if one campaign running)
- [ ] Check conversions in BigQuery: `SELECT COUNT(*) FROM conversion_signals WHERE DATE(conversion_time) = CURRENT_DATE()`
- [ ] Check ROAS: Total Revenue ÷ Total Spend
- [ ] Apply Kill Rule: Pause ad sets over $20.25 with 0 conversions
- [ ] Check for policy violations in Ads Manager

**Every other day (Wednesday, Friday, Sunday):**
- [ ] Apply Scale Rule: Increase profitable ad sets by 20%
- [ ] Review top-performing creative combos in Breakdown view
- [ ] Screenshot top ads for pattern analysis

**Weekly (Sunday evening):**
- [ ] Export full week performance data
- [ ] Identify winning creative patterns (which images/copy performed best)
- [ ] Create 3 new creative variants based on winners
- [ ] Plan next week's tests

---

### 5.5 The "Refresh" Rule (Weekly)

**Rule:** Rotate in new creative variations every 7 days to combat ad fatigue.

**Ad fatigue symptoms:**
- CTR drops by 30%+ compared to Day 1-3
- CPM (cost per 1000 impressions) increases by 50%+
- Frequency metric rises above 3.0 (same people seeing ad too often)

**How to combat:**
1. Create 3 new images/videos using winning angle
2. Duplicate best-performing ad set
3. Swap in new creative
4. Run head-to-head test for 48 hours
5. Keep winner, pause loser

**Creative refresh pipeline:**
- Week 1: Test 12 variants (3:2:2 matrix)
- Week 2: Double down on winning angle, create 6 new variants
- Week 3: Test new angle entirely (switch from Logic to Curiosity)
- Week 4: Introduce video ads, test 3 variants
- Repeat cycle

---

## Master Checklist

### Infrastructure
- [ ] Domain purchased and DNS configured
- [ ] Domain verified in Facebook Business Manager
- [ ] Bridge page deployed (playtosave.net live on Cloud Run)
- [ ] Page load speed optimized (< 2 seconds)
- [ ] Meta Pixel installed on all pages
- [ ] CAPI endpoint built and tested
- [ ] Event deduplication implemented (event_id matching)
- [ ] Footer with Privacy Policy, Terms, Contact links
- [ ] Support email created and forwarding
- [ ] MaxBounty postback URL configured
- [ ] BigQuery tables created (game_events, conversion_signals)

### Account Warm-Up
- [ ] Facebook Business Page created
- [ ] Page branding uploaded (logo, cover photo)
- [ ] 3 generic posts published (no selling)
- [ ] Credit card added to Ad Account
- [ ] $15 "burn spend" campaign run for 3 days
- [ ] No policy violations or warnings received

### Creative Assets
- [ ] Offer selected (EPC > $0.30, CPL type, white-hat traffic)
- [ ] 3 ad angles defined (Logic, Fear, Curiosity)
- [ ] 3 images/videos generated (one per angle)
- [ ] 2 primary text variations written
- [ ] 2 headline variations written
- [ ] All assets organized in /creative_assets/ folder
- [ ] Dynamic Creative enabled in ad setup

### Campaign Launch
- [ ] Campaign objective set to "Sales" or "Leads"
- [ ] CBO turned OFF (manual ad set budgets)
- [ ] Targeting: US, Age 25-65, Interest: Homeowners
- [ ] Placements: Advantage+ (automatic)
- [ ] Daily budget: $20/day
- [ ] URL parameters include {{fbclid}}
- [ ] Campaign scheduled for 12:00 AM launch
- [ ] Pre-launch tests: Pixel firing, CAPI working, Postback tested

### Daily Operations
- [ ] Day 1-2: Monitor only, no changes (Hold Rule)
- [ ] Day 3+: Apply Kill Rule (pause ad sets with $20.25 spend, 0 conversions)
- [ ] Day 4+: Apply Scale Rule (increase winners by 20% every 48h)
- [ ] Weekly: Create and test 3 new creative variants
- [ ] Daily: Check ROAS in BigQuery performance dashboard

---

## Performance Benchmarks

### Phase 1: Validation (Days 1-14)
**Goal:** Achieve breakeven or better

| Metric | Target | Good | Excellent |
|--------|--------|------|-----------|
| **CTR** | > 1.0% | > 2.0% | > 3.5% |
| **CPC** | < $0.75 | < $0.50 | < $0.30 |
| **Landing Page CVR** | > 3% | > 5% | > 8% |
| **Cost Per Lead** | < $6.75 | < $4.50 | < $3.00 |
| **ROAS** | > 1.0x | > 1.5x | > 2.0x |
| **Daily Conversions** | 3-5 leads | 8-12 leads | 15-20 leads |

### Phase 2: Optimization (Days 15-30)
**Goal:** Consistent profitability

| Metric | Target |
|--------|--------|
| **ROAS** | > 2.0x |
| **Daily Budget** | $40-60/day |
| **Daily Revenue** | $80-120/day |
| **Daily Profit** | $40-60/day |
| **Winning Ad Sets** | 2-3 active |

### Phase 3: Scale (Days 31-60)
**Goal:** Maximize revenue within daily cap constraints

| Metric | Target |
|--------|--------|
| **ROAS** | > 2.5x |
| **Daily Budget** | $100-150/day |
| **Daily Revenue** | $168/day (25 leads × $6.75 = cap limit) |
| **Daily Profit** | $68-118/day |
| **Active Offers** | 3-5 offers (diversification) |

---

## Risk Management

### Daily Cap Risk
**Problem:** Offer #29678 caps at 25 leads/day ($168 max revenue)

**Solutions:**
1. Apply to 3-5 additional insurance offers NOW
2. Set spend limit at $120/day (leaves buffer before cap)
3. Build automated alert: "20 conversions reached today, reduce budget"
4. Diversify into other verticals (finance, credit, solar)

### Account Ban Risk
**Problem:** Facebook can ban your ad account without warning

**Prevention:**
- ✅ Never make exaggerated claims ("guaranteed savings")
- ✅ Include clear affiliate disclosure
- ✅ Don't use "before/after" imagery without disclaimers
- ✅ Respond to policy violation warnings within 24 hours
- ✅ Keep backup ad account ready (separate Business Manager)

### Offer Pause Risk
**Problem:** MaxBounty can pause offers without notice

**Prevention:**
- ✅ Maintain good communication with affiliate manager
- ✅ Don't send trash traffic (bots, fraud clicks)
- ✅ Stay within daily cap limits
- ✅ Have 2-3 backup offers ready in same vertical

### Overspend Risk
**Problem:** Algorithm spends more than expected, eats profit

**Prevention:**
- ✅ Set account spending limit: $150/day in Facebook Business Settings
- ✅ Enable budget alerts at $100/day
- ✅ Check spend every morning before 10 AM
- ✅ Use manual budgets (not CBO) until proven profitable

---

## Appendix A: CAPI Event Matching Quality

**Target Match Rate:** > 80%

**How to check:**
1. Go to Events Manager → Data Sources → Your Pixel
2. Click "Overview" tab
3. Look for "Event Match Quality" score

**If score < 70%:**
- Check that `fbclid` is being captured correctly
- Verify `event_id` matches between browser and server events
- Add `fbc` cookie parameter to CAPI events
- Test with Events Manager Test Events tool

---

## Appendix B: MaxBounty Postback URL Format

**Template:**
```
https://playtosave.net/postback?subId1=[s1]&payout=[payout]&secret=YOUR_SECRET_TOKEN
```

**Variables MaxBounty replaces:**
- `[s1]` → Your SubID1 value (the event_id from click)
- `[payout]` → Actual payout amount (usually $6.75)

**Security:**
- Generate random secret: `openssl rand -hex 32`
- Store in .env file: `AFFILIATE_SECRET=abc123...`
- Never commit secret to git

---

## Appendix C: BigQuery Performance Queries

**Daily ROAS calculation:**
```sql
WITH spend AS (
  SELECT SUM(cost) as total_spend
  FROM `rooster_data.ad_performance`
  WHERE DATE(date) = CURRENT_DATE()
),
revenue AS (
  SELECT SUM(payout) as total_revenue
  FROM `rooster_data.conversion_signals`
  WHERE DATE(conversion_time) = CURRENT_DATE()
)
SELECT 
  spend.total_spend,
  revenue.total_revenue,
  ROUND(revenue.total_revenue / spend.total_spend, 2) as roas
FROM spend, revenue;
```

**Top performing ad creatives:**
```sql
SELECT
  ad_name,
  SUM(impressions) as impressions,
  SUM(clicks) as clicks,
  ROUND(SUM(clicks) / SUM(impressions) * 100, 2) as ctr,
  SUM(conversions) as conversions,
  ROUND(SUM(cost) / SUM(conversions), 2) as cost_per_lead
FROM `rooster_data.ad_performance`
WHERE DATE(date) >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
GROUP BY ad_name
ORDER BY conversions DESC
LIMIT 10;
```

---

**END OF STRATEGY DOCUMENT**

*Last updated: February 5, 2026*  
*Version: 1.0*  
*Next review: After first 30 days of ad spend*
