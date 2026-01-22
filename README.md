# Project Alpha Rooster: Social-to-CPA Game Engine
**Version:** 10.0 (Production-Ready Build)
**Core Concept:** Interactive Lead Generation Arbitrage via Gamification
**Target Infrastructure:** Google Cloud Platform (GCP) + Meta Ads
**Barrier to Entry:** Low (Open Affiliate Networks)
**Expected ROI:** 4-6x ROAS (Return on Ad Spend)

---

## Part 1: The Functional Abstract (The "What" and "Why")

### 1.1 The Business Thesis

**Project Alpha Rooster** is a "Social-to-CPA" arbitrage machine. It exploits the spread between low-cost social attention (Meta Ads) and high-value commercial leads (Affiliate Offers).

**The Core Problem We're Solving:**
- Social media users scroll for entertainment, not to buy things or fill out forms.
- If you send them directly to a signup page, 95% bounce immediately.
- You waste money on clicks that never convert.

**Our Solution:**
We insert a **10-second interactive game** between the ad click and the offer. This:
1. **Overcomes banner blindness** - People engage with games, not ads.
2. **Creates dopamine** - Winning a "prize" (even fake) triggers excitement.
3. **Builds commitment** - "I won this, so I should claim it" (psychological principle called the endowment effect).
4. **Increases time-on-page** - 10 seconds of engagement vs. 2 seconds of bouncing.

**The Money Flow (Simple Version):**
1. You pay Facebook **$0.30** per click.
2. User plays your game, "wins," and clicks through to an insurance quote form.
3. Insurance company pays you **$15** when the user submits the form.
4. **Profit:** $15 - $0.30 = $14.70 per conversion.
5. If 5% of your clicks convert, you're making **$0.74 per click** while spending **$0.30**.
6. That's a **2.5x return**. Scale it up.

### 1.2 The Production Line (The 6-Stage Loop)

This is a **closed-loop system**. Each stage feeds data into the next to optimize performance.

#### **Stage 1: Attract (Meta Ads)**
**What happens:** We run Facebook/Instagram ads targeting broad interests (e.g., "people interested in saving money").

**Why broad?** High-intent keywords (Google search) are expensive. Social traffic is cheap because users aren't actively looking to buy—we're interrupting them.

**Cost:** $0.20-$0.40 per click.

**Ad Creative Examples:**
- Video of someone spinning a wheel and "winning"
- "You've been selected! Spin to reveal your exclusive savings!"
- Curiosity-driven: "Can you unlock the mystery reward?"

---

#### **Stage 2: Qualify (Pre-Filter) [OPTIONAL - Saves 30-40% of Waste]**
**What happens:** Before showing the game, we ask 2 quick questions:
1. "What's your age range?" (21-30, 31-40, etc.)
2. "What state are you in?" (dropdown menu)

**Why?** If the insurance offer is only available to people 25+ in California, there's no point showing a game to an 18-year-old in Texas. We filter them out immediately.

**User Experience:**
- **Qualified users** → Proceed to game.
- **Unqualified users** → See: "Sorry, this offer isn't available in your area."

**Impact:** Reduces wasted spend by 30-40%. Only pay for qualified traffic.

---

#### **Stage 3: Engage (The Game)**
**What happens:** Qualified users see one of three game types:
1. **Spin Wheel** - Classic carnival wheel with segments like "Bronze," "Silver," "Gold."
2. **Scratch-off** - Mimics a lottery scratch ticket (mobile-friendly).
3. **Prize Box** - Click to "unlock" a mystery reward.

**The Game Flow (10 seconds total):**
1. User sees instructions: "Spin to reveal your savings eligibility!"
2. They tap "Spin Now."
3. Wheel spins (JavaScript animation).
4. It lands on "Gold Status" (predetermined - they always "win").
5. Celebration animation: "🎉 Congratulations! You unlocked GOLD STATUS!"

**Behind the Scenes (Technical):**
- We capture their Facebook Click ID (`fbclid`) - this is how we track them.
- We generate a unique Session ID (`event_id`) for this specific visit.
- We log to BigQuery: "User #12345 spun the wheel at 3:42pm and landed on Gold."
- We fire Meta Pixel events for retargeting (explained in Stage 6).
- We track fraud signals (mouse movement, time on page) to detect bots.

**Why This Works:**
- **Dopamine hit** - Even fake "wins" trigger reward centers in the brain.
- **Micro-commitment** - They invested 10 seconds. They're more likely to follow through.
- **Curiosity** - "What is Gold Status? I want to find out."

---

#### **Stage 4: Monetize (The Routing)**
**What happens:** After "winning," a big button appears:

> **"CLAIM YOUR GOLD REWARD →"**

**When they click:**
1. We construct a special tracking URL: `insurance-offer.com/quote?subId1=12345`
2. That `subId1=12345` is OUR tracking ID - so the insurance company knows this lead came from us.
3. The user is redirected to the insurance company's signup form.
4. The form is branded as their "Gold Status reward" (e.g., "Congratulations! Get your Gold-tier quote below.").

**Critical Technical Detail:**
We MUST pass our `event_id` into the affiliate link's `subId` parameter. This is how we get paid. Without it, we have no way to prove the conversion came from us.

---

#### **Stage 5: Signal (The Feedback Loop - The Secret Sauce)**
**What happens:** The user fills out the insurance form and submits it.

**On the affiliate's side:**
- Their system detects a new lead.
- They check the `subId1=12345` parameter.
- They send a "postback" (a ping) to our server:
  ```
  POST yoursite.com/postback?subId1=12345&payout=15.00
  ```

**On our side:**
1. Our server receives this notification.
2. We log it in BigQuery: "Event #12345 earned $15 at 3:47pm."
3. **CRITICAL STEP:** We look up the original Facebook Click ID (`fbclid`) for event #12345.
4. We call **Facebook's Conversions API** (CAPI) and say:
   - "The user with fbclid=ABC123 just converted."
   - "The conversion value was $15."
   - "Optimize my ads to find more people like this."

**Why This Matters (The Compounding Effect):**
- Most advertisers DON'T do this step. They run ads blindly.
- We're feeding Facebook REAL conversion data.
- Facebook's algorithm learns: "Oh, people who look like ABC123 convert. I'll show the ad to more people like them."
- Over 7-14 days, your Cost Per Click (CPC) drops and your Conversion Rate (CVR) goes up.
- **This is the secret sauce that turns a 2x ROAS into a 5x ROAS.**

---

#### **Stage 6: Retarget (The Recovery Loop - Capture Lost Revenue)**
**The Problem:** 80% of users will play the game but NOT click the "Claim Reward" button. They got distracted, had second thoughts, or closed the tab. You paid $0.30 for that click. They're gone forever... unless you retarget.

**The Solution:** We installed Meta Pixel (a tracking code) on our game page. It fires 3 events:

1. **ViewContent** - User landed on the game page.
2. **AddToCart** - User spun the wheel (interacted).
3. **InitiateCheckout** - User clicked "Claim Reward."

**Retargeting Strategy:**
- Create a second ad campaign targeting ONLY people who fired `InitiateCheckout` but have NO conversion signal (they clicked through but didn't submit the form).
- Show them a different ad:
  - "You're running out of time! Your Gold Status expires in 24 hours. Claim it now!"
  - Video testimonial: "I saved $400 with my Gold Status quote!"
- Budget: 20% of your total ad spend (if you're spending $100/day on cold traffic, spend $20/day on retargeting).

**Why This Works:**
- These people already know what you're offering. They're warm leads.
- Retargeting traffic converts at 3-5x the rate of cold traffic.
- You capture an extra 50-70% of potential conversions you would've lost.

---

### 1.3 The Competitive Advantages (Why This Beats Traditional Affiliate Marketing)

| **Traditional Affiliate Approach** | **Alpha Rooster Approach** |
|------------------------------------|----------------------------|
| Run ads → Send to static landing page → Hope they convert | Run ads → Interactive game → Psychological commitment → Higher conversions (2-5x) |
| No conversion feedback to Facebook | CAPI integration feeds conversion data back → Facebook optimizes → Better traffic over time |
| Pay for all clicks (including bots and unqualified users) | Pre-qualification filters waste + Fraud detection flags bots → 30-40% cost savings |
| Lost users are gone forever | Retargeting captures 50-70% more conversions from people who bounced |
| Manually test offers until something works | Systematic A/B testing framework → Find winners in 3-5 days instead of 3-5 weeks |
| Static creative gets "ad fatigue" after 7-14 days | Multiple game variants + rotating ad creative → Stays fresh longer |

**Bottom Line:** This isn't a "spray and pray" affiliate system. It's a **data-driven, self-optimizing arbitrage machine**.

---

### 1.4 Expected Economics (After Optimization)

These numbers assume you've found winning combinations (typically takes 2-4 weeks of testing):

**Daily Ad Spend:** $200  
**Clicks:** 500 @ $0.40 CPC  
**Pre-Qualification Pass Rate:** 60% → 300 qualified users  
**Game Engagement Rate:** 90% → 270 people play  
**Click-Through to Offer:** 50% → 135 people visit offer page  
**Conversion Rate on Offer:** 7% → 9-10 conversions  
**Average Payout:** $30 per conversion  
**Daily Revenue:** 10 × $30 = $300  
**Daily Profit:** $300 - $200 = **$100/day**  

**With Retargeting (adds 50% more conversions):**  
**Total Conversions:** 15/day  
**Daily Revenue:** 15 × $30 = $450  
**Daily Profit:** $450 - $200 = **$250/day**  
**Monthly Profit:** $250 × 30 = **$7,500/month**  

**Once scaled to $500/day ad spend:**  
**Monthly Profit:** $18,000 - $25,000/month (depending on offers)

---

### 1.5 The Risks (What Could Go Wrong?)

**Risk 1: Facebook Account Bans**
- **Why:** Misleading ads ("You won $500!" when they didn't) or policy violations.
- **Mitigation:** Use honest language. Add disclaimers. Follow Meta's ad policies religiously.

**Risk 2: Affiliate Networks Shave Conversions**
- **Why:** Some networks report fewer conversions than actually happened (fraud on their end).
- **Mitigation:** Work with reputable networks (Impact, ClickBank). Track discrepancies. Diversify across 2-3 networks.

**Risk 3: Burning Money on Bad Combinations**
- **Why:** Not every ad + game + offer combo will work.
- **Mitigation:** Start small ($100-150 test budget). Kill losers fast (after 100 clicks). Only scale winners.

**Risk 4: Legal/Compliance Issues**
- **Why:** No Privacy Policy, misleading claims, GDPR/CCPA violations.
- **Mitigation:** Use legal templates (Termly.io). Be transparent. Never promise guaranteed prizes unless true.

**Risk 5: Market Saturation**
- **Why:** If everyone does this, CPCs rise and conversion rates fall.
- **Mitigation:** Constantly test new offers, new verticals, new game mechanics. Stay ahead of the curve.

---

### 1.6 TL;DR (Executive Summary)

**What We're Building:**  
A social media arbitrage machine that connects Facebook users to affiliate offers using interactive games as a psychological bridge.

**The 6-Step Flow:**
1. Buy cheap clicks from Facebook ads ($0.20-0.40/click)
2. Filter out unqualified users with 2-question pre-screen (saves 30-40%)
3. Engage with interactive games (spin wheel, scratch-off) - they always "win"
4. Route to affiliate offers (insurance, software trials, etc.)
5. Get paid when they sign up ($15-30/conversion)
6. Feed conversion data back to Facebook (CAPI) so algorithm improves over time

**The Secret Weapons:**
- **Gamification** = 2-5x higher conversions vs. static landing pages
- **CAPI Feedback Loop** = Facebook learns who converts → sends better traffic → CPCs drop
- **Retargeting** = Captures 50-70% more conversions from users who bounced
- **Fraud Detection** = Eliminates bot traffic that wastes money
- **A/B Testing Framework** = Finds winning combinations in days, not weeks

**Expected Outcome (Realistic, Post-Optimization):**
- **Investment:** $200/day on ads
- **Revenue:** $450/day from conversions
- **Profit:** $250/day ($7,500/month)
- **ROAS:** 4-6x return on ad spend

**Timeline to Profitability:**
- **Week 1-2:** Build the system ($0 spent, just coding)
- **Week 3:** Test with $100-150 budget, find 1-2 winners
- **Week 4:** Scale winners to $50-100/day
- **Month 2+:** Scale to $200-500/day if profitable

**Who This Is For:**
- People with $500-1,000 to risk testing
- Those willing to spend 2-4 weeks optimizing before seeing profit
- Anyone who understands this is NOT passive income (requires testing, tweaking, monitoring)

**Who This Is NOT For:**
- People expecting guaranteed returns
- Those without capital to test and lose initially
- Anyone looking for "set and forget" passive income

**Bottom Line:**  
This is a **data-driven, systematic approach** to affiliate marketing. Not a get-rich-quick scheme. Realistic outcome: **$5k-25k/month profit** within 3-6 months if you execute properly and find winning combinations.

---

## Part 2: Atomic Technical Specification

### 2.1 Technology Stack (The "Interactive" Stack)
| Component | Technology | Constraint |
| :--- | :--- | :--- |
| **Compute** | Cloud Run | Python 3.11, FastAPI. Serverless, auto-scaling. |
| **Frontend** | Jinja2 + Vanilla JavaScript | Lightweight. No build tools. Mobile-first. |
| **Database** | BigQuery | Event logging, analytics, fraud detection. |
| **Ad Platform** | Meta Ads (FB/IG) | Conversions API (CAPI) for optimization. |
| **Retargeting** | Meta Pixel | Track user behavior for retargeting campaigns. |
| **Monetization** | Impact / ClickBank | Open-access affiliate networks. |
| **Compliance** | Termly.io Templates | Privacy Policy, Terms of Service. |

### 2.2 Data Architecture

#### Table A: `game_events` (The "Interaction" Log)
* `event_id` (UUID, REQUIRED): Unique session ID. Generated by us.
* `fbclid` (STRING): Facebook Click ID (Passed from Ad).
* `variant_id` (STRING): Which ad + game combo was shown (for A/B testing).
* `game_type` (STRING): e.g., 'spin_wheel', 'scratch_off', 'prize_box'.
* `interaction_result` (STRING): e.g., 'landed_on_gold'.
* `outcome_url` (STRING): The affiliate link we sent them to.
* `is_qualified` (BOOLEAN): Did they pass pre-filter questions?
* `fraud_score` (FLOAT): Bot detection score (0.0 = human, 1.0 = bot).
* `timestamp` (TIMESTAMP).

#### Table B: `conversion_signals` (The "Money" Log)
* `event_id` (UUID): Matches `game_events`.
* `payout` (FLOAT): Amount earned (from Affiliate Postback).
* `status` (STRING): 'sent_to_facebook'.
* `conversion_time` (TIMESTAMP).

#### View: `view_offer_performance` (The "Decision Engine")
```sql
SELECT
    game_type,
    variant_id,
    outcome_url,
    COUNT(event_id) as plays,
    COUNT(conversion_signals.event_id) as conversions,
    SUM(payout) as revenue,
    SAFE_DIVIDE(COUNT(conversion_signals.event_id), COUNT(event_id)) as cvr,
    SAFE_DIVIDE(SUM(payout), COUNT(event_id)) as epc
FROM game_events
LEFT JOIN conversion_signals USING(event_id)
WHERE is_qualified = TRUE AND fraud_score < 0.3
GROUP BY 1, 2, 3
HAVING plays > 100
ORDER BY epc DESC
```

### 2.3 Component Specs

#### Component 1: The Pre-Qualifier (`/qualify`)
* **Runtime:** Cloud Run (FastAPI).
* **Logic:**
    1.  User lands from Meta ad with `fbclid`.
    2.  Show 2-question micro-survey:
        * "What's your age range?" → Filters minors for financial offers.
        * "What state are you in?" → Filters states where offers aren't available.
    3.  **If Unqualified:** Show "Sorry, this offer isn't available in your area." Exit.
    4.  **If Qualified:** Set `is_qualified=TRUE`, proceed to game.
* **Why:** Eliminates 30-40% of wasted clicks. Improves CVR dramatically.

#### Component 2: The Game Engine (`/app`)
* **Runtime:** Cloud Run (FastAPI serving Jinja2 templates).
* **Logic:**
    1.  **Landing:** Capture `fbclid`, generate `event_id`, log to BigQuery.
    2.  **Meta Pixel Fire:** Send `ViewContent` event (for retargeting).
    3.  **Interaction Flow (Frontend JS):**
        * Present game mechanic (Spin Wheel / Scratch-off / Prize Box).
        * User interacts (clicks "Spin" or "Scratch").
        * JS handles animation. Result is predetermined/weighted.
        * **Fraud Detection (JS):**
            * Track mouse movement. Zero movement = bot.
            * Track time on page. <2 seconds = bot.
            * Calculate `fraud_score` (0.0-1.0).
    4.  **Handoff:**
        * Display "Claim Reward" button.
        * Link: `offer_url?subId1={event_id}`.
        * **Meta Pixel Fire:** Send `InitiateCheckout` event.
        * Log `interaction_result` + `fraud_score` to BigQuery.
        * Redirect to affiliate offer.

#### Component 3: The Signal Loop (`/postback`)
* **Role:** Receives conversion data from Affiliate Network.
* **Route:** `POST /postback?subId1={event_id}&payout={amt}`
* **Logic:**
    1.  Receive ping indicating a sale/lead.
    2.  Log to `conversion_signals`.
    3.  Look up original `fbclid` using `event_id`.
    4.  **Call Meta Conversions API (CAPI):**
        * Event: "Purchase" or "Lead".
        * Value: `{payout}`.
        * User Data: `{fbclid}`.
    5.  Mark `status='sent_to_facebook'`.

#### Component 4: The Retargeting Layer (Meta Pixel Events)
* **Events Fired:**
    * `ViewContent` → User landed on game.
    * `AddToCart` → User spun/scratched (interacted).
    * `InitiateCheckout` → User clicked "Claim Reward."
* **Retargeting Campaign:**
    * Target users who fired `InitiateCheckout` but have NO conversion signal.
    * Budget: 20% of total ad spend.
    * Creative: Different angle ("Still want your Gold Status? Claim now!").

---

## Part 3: Execution Checklist (The "Go" Plan)

### Phase 1: Foundation & Compliance (Days 1-2)
* [ ] **1.1 Accounts:** Sign up for **Impact.com** or **ClickBank**. Apply to 5-10 offers suitable for gamification (sweepstakes, insurance quotes, software trials, financial products).
* [ ] **1.2 Links:** Get unique tracking links. Identify the "SubID" parameter for each network.
* [ ] **1.3 GCP:** Create Project `rooster-social-game`. Enable Cloud Run & BigQuery APIs.
* [ ] **1.4 Legal Foundation:**
    * Create **Privacy Policy** using Termly.io (cover data collection, cookies, Meta Pixel, affiliate sharing).
    * Create **Terms of Service** stating: "This is a promotional game. Outcomes are predetermined. Clicking 'Claim' redirects to third-party offers."
    * Add **Disclaimers** to game page: "This is not a guaranteed prize. You must qualify for the offer."
* [ ] **1.5 Meta Business Setup:**
    * Create Meta Business Manager account.
    * Create Meta Pixel. Get Pixel ID.
    * Generate CAPI Access Token from Events Manager.

### Phase 2: Creative Arsenal (Days 2-4)
* [ ] **2.1 Ad Variants:** Create 5 ad concepts:
    * "You've been selected to spin for exclusive savings!"
    * "Can you beat the odds and unlock Gold Status?"
    * "Claim your mystery reward in 10 seconds!"
    * User-generated style (iPhone selfie video of someone playing).
    * High-production animated graphics.
* [ ] **2.2 Game Variants:** Build 3 game mechanics:
    * **Spin Wheel** (classic, high engagement).
    * **Scratch-off** (tactile, mobile-friendly).
    * **Prize Box** (mystery/curiosity angle).
* [ ] **2.3 Variant Tracking:** Assign each ad + game combo a unique `variant_id` (e.g., "ad1_wheel", "ad2_scratch").

### Phase 3: The Game App (Days 5-8)
* [ ] **3.1 Scaffold:** Initialize FastAPI app with Jinja2 templates. Set up local dev environment.
* [ ] **3.2 Pre-Qualifier:** Build `/qualify` route with 2-question form (age, state). Logic to pass/fail users.
* [ ] **3.3 Game Mechanics:**
    * Implement Spin Wheel using Canvas or lightweight JS library (e.g., Winwheel.js).
    * Implement Scratch-off using HTML5 Canvas.
    * Implement Prize Box using CSS animations.
* [ ] **3.4 Fraud Detection (Frontend):**
    * Track mouse movements. Flag zero-movement sessions.
    * Track time-on-page. Flag <2 second sessions.
    * Calculate `fraud_score` (0.0-1.0) and send to backend.
* [ ] **3.5 Meta Pixel Integration:**
    * Install Pixel code in templates.
    * Fire `ViewContent` on page load.
    * Fire `AddToCart` on game interaction.
    * Fire `InitiateCheckout` on "Claim Reward" click.
* [ ] **3.6 BigQuery Logging:** Create tables `game_events` and `conversion_signals`. Log all events from FastAPI.
* [ ] **3.7 Deploy:** Build Dockerfile. Deploy to Cloud Run. Test on mobile (iOS Safari, Chrome Android).

### Phase 4: The Signal Loop (Days 9-10)
* [ ] **4.1 Postback Endpoint:** Create `/postback` route to receive affiliate conversion pings.
* [ ] **4.2 Meta CAPI Integration:**
    * Install `facebook-business` Python SDK.
    * Write function to send conversion events to CAPI.
    * Include `fbclid`, event type, payout value.
* [ ] **4.3 Validation:** Use Meta Events Manager "Test Events" tool. Verify events appear in real-time.

### Phase 5: Analytics & Optimization (Days 11-12)
* [ ] **5.1 Performance Dashboard:** Create BigQuery view `view_offer_performance` (CVR, EPC by variant + offer).
* [ ] **5.2 Decision Rules:**
    * **Kill Rule:** If offer CVR < 2% after 500 plays → Pause offer, replace with new one.
    * **Scale Rule:** If offer EPC > $0.50 after 500 plays → Increase budget allocation.
* [ ] **5.3 Monitoring:** Set up email/Slack alerts for:
    * Daily spend exceeding budget.
    * Fraud score >30% of traffic.
    * Zero conversions for 24+ hours (dead signal).

### Phase 6: Launch (The $150 Test)
* [ ] **6.1 Primary Campaign (Cold Traffic):**
    * Objective: "Traffic" (first 3 days) → "Conversions" (once CAPI flowing).
    * Budget: $20/day for 5 days = $100 total.
    * Targeting: Broad interests (18-65, all genders, US/CA/UK).
    * Creative: Rotate all 5 ad variants.
* [ ] **6.2 Retargeting Campaign:**
    * Objective: "Conversions."
    * Budget: $10/day for 5 days = $50 total.
    * Audience: Custom Audience → Users who fired `InitiateCheckout` but no conversion signal.
    * Creative: "You spun Gold! Don't miss out—claim your reward now."
* [ ] **6.3 Monitoring:**
    * Check BigQuery hourly first day for `game_events`.
    * Check affiliate dashboard for conversion pings.
    * Verify CAPI events in Meta Events Manager.
* [ ] **6.4 Optimization (Day 3+):**
    * Kill ads with CTR <1%.
    * Kill game variants with CVR <3%.
    * Kill offers with EPC <$0.20.
    * Scale winners (2x budget on best-performing variant + offer combo).

---

## Part 4: Success Metrics & Scaling

### Key Performance Indicators (KPIs)
| Metric | Target | How to Calculate |
|--------|--------|------------------|
| **Click-Through Rate (CTR)** | >2% | (Ad Clicks / Ad Impressions) |
| **Cost Per Click (CPC)** | <$0.40 | (Ad Spend / Ad Clicks) |
| **Game Engagement Rate** | >80% | (Users Who Spun / Users Who Landed) |
| **Conversion Rate (CVR)** | 5-10% | (Conversions / Game Plays) |
| **Earnings Per Click (EPC)** | >$0.60 | (Total Revenue / Total Clicks) |
| **Return on Ad Spend (ROAS)** | 4-6x | (Total Revenue / Total Ad Spend) |

### Scaling Strategy
1. **Week 1-2:** Test phase. $150 budget. Find 1-2 winning variant + offer combos.
2. **Week 3-4:** Scale winners to $50/day. Kill losers. Add 3 new offers.
3. **Week 5-8:** Scale to $100-200/day. Diversify across 5+ offers. Build second game type.
4. **Month 3+:** Scale to $500+/day. Hire VA to manage creative testing. Explore new traffic sources (TikTok, native ads).

### Expected Economics (After Optimization)
* **Ad Spend:** $200/day
* **Clicks:** 500/day @ $0.40 CPC
* **Game Plays:** 400/day (80% engagement)
* **Conversions:** 30/day @ 7.5% CVR
* **Revenue:** $900/day @ $30 avg payout
* **Net Profit:** $700/day
* **ROAS:** 4.5x

---

## Part 5: Risk Mitigation

### Compliance Checklist
* [ ] Privacy Policy includes Meta Pixel disclosure.
* [ ] Terms state game outcomes are predetermined.
* [ ] Disclaimers on game page: "Not a guaranteed prize."
* [ ] Ad creative doesn't promise specific dollar amounts unless true.
* [ ] No before/after images without FTC disclaimers.
* [ ] No health claims or get-rich-quick language.

### Account Protection
* [ ] Use separate Meta ad account for this project (don't risk main business account).
* [ ] Run ads from Meta Business Manager (not personal account).
* [ ] Keep backup affiliate networks (if Impact bans you, switch to ClickBank).
* [ ] Never violate affiliate network TOS (no incentivized traffic, no fake leads).

### Technical Safeguards
* [ ] Rate limit `/postback` endpoint (prevent spam/fraud).
* [ ] Validate postback signatures (if network supports it).
* [ ] Cap daily spend with Meta campaign budget limits.
* [ ] Monitor fraud score daily. If >30%, pause and investigate.