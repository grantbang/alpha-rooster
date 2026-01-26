# Facebook Targeting Strategy
## How to "Buy the Right Real Estate" (Audience Targeting)

---

## The Concept: Facebook Ads as Digital Real Estate

When you "buy real estate" from Facebook, you're buying **access to specific people's attention**. The better you target, the cheaper your clicks and higher your conversions.

---

## Phase 1: Cold Traffic (Days 1-7) - Finding Your Audience

### **Interest Targeting** (Broad but Relevant)

Instead of targeting "everyone," you target people who've shown interest in related topics:

#### For Insurance Offers:
```
Interests to Target:
- GEICO
- Progressive Insurance
- State Farm
- Allstate
- Compare insurance quotes
- Car ownership
- Homeownership
- Financial planning
- Dave Ramsey
- Suze Orman
```

#### For Personal Loan Offers:
```
Interests to Target:
- Debt consolidation
- Personal finance
- Credit repair
- SoFi
- LendingClub
- Marcus by Goldman Sachs
- Credit Karma
```

### **Demographic Targeting**

Facebook lets you narrow by:
- **Age**: 25-65 (insurance buyers)
- **Location**: United States (or specific states)
- **Income**: $50k+ (can afford insurance)
- **Life Events**: Recently moved, bought car, got married

### **Example Campaign Setup**

```
Campaign: Auto Insurance - Cold Traffic
Objective: Traffic (to website)
Budget: $50/day

Ad Set 1: "Car Owners - Finance Interest"
  Age: 25-55
  Location: United States
  Interests: GEICO, Progressive, Car ownership
  Budget: $20/day
  
Ad Set 2: "Financial Planners"
  Age: 30-60
  Location: United States  
  Interests: Financial planning, Dave Ramsey
  Budget: $15/day
  
Ad Set 3: "Recent Car Buyers"
  Age: 25-50
  Location: United States
  Life Event: Purchased vehicle (past 6 months)
  Budget: $15/day
```

---

## Phase 2: Warm Traffic (Days 8-30) - Pixel Data

### **How Facebook Pixel Works**

When someone visits your site, Facebook "tags" them. You can then:

1. **Track actions**: Did they play the game? Did they convert?
2. **Create audiences**: People who played but didn't convert
3. **Build lookalikes**: Find people similar to converters

### **Custom Audiences You'll Build**

```
Audience 1: "Site Visitors - All"
  → Anyone who visited playtosave.net
  → Use for: Retargeting with different offer

Audience 2: "Game Players - No Convert"
  → Played spin wheel but didn't submit form
  → Use for: Retargeting (they're warm, just need nudge)

Audience 3: "Form Starters - No Submit"
  → Clicked through to offer but didn't complete
  → Use for: High-intent retargeting

Audience 4: "Converters"
  → Completed the insurance quote/loan application
  → Use for: Building lookalike audiences
```

### **Retargeting Campaign Example**

```
Campaign: Retargeting - Engaged Users
Objective: Conversions
Budget: $30/day

Ad Set: "Game Players - Different Offer"
  Audience: Custom - Played game, no convert (past 7 days)
  Budget: $15/day
  CPC: $0.10-0.15 (cheap! they know you)
  
Ad Set: "Form Starters - Reminder"
  Audience: Custom - Started form, didn't submit (past 3 days)
  Budget: $15/day
  CPC: $0.08-0.12 (very warm)
```

---

## Phase 3: Hot Traffic (Days 31+) - Lookalike Audiences

### **The Magic: Facebook Finds Your Customers**

Once you have 50-100 conversions, Facebook's AI can find people who **look like your converters**.

#### **How Lookalikes Work**

Facebook analyzes your converters:
- What pages they like
- What they click on
- Demographics
- Browsing behavior
- Purchase history
- 1000+ data points

Then finds people with similar patterns.

### **Lookalike Audience Setup**

```
Source Audience: "Converters" (100+ people)

Lookalike 1%: 
  → 2.1 million people in USA
  → Most similar to your converters
  → CPC: $0.25-0.35
  → Conversion rate: 8-12%
  
Lookalike 2-3%:
  → 4.2 million people
  → Similar but broader
  → CPC: $0.20-0.30
  → Conversion rate: 5-8%
  
Lookalike 4-5%:
  → Broadest, for scaling
  → CPC: $0.18-0.25
  → Conversion rate: 3-5%
```

### **Scaling Campaign (Month 2+)**

```
Campaign: Lookalike - Auto Insurance
Objective: Conversions (optimized for leads)
Budget: $200/day

Ad Set 1: "LAL 1% - Converters"
  Audience: 1% Lookalike of Converters
  Age: 25-55
  Budget: $100/day
  
Ad Set 2: "LAL 2-3% - Converters"  
  Audience: 2-3% Lookalike
  Age: 25-55
  Budget: $75/day
  
Ad Set 3: "LAL 1% + Interest Stack"
  Audience: 1% Lookalike AND Interested in GEICO
  Age: 30-50
  Budget: $25/day
```

---

## The Conversions API Secret Weapon

### **Why Most Affiliates Fail**

Normal flow:
```
Facebook Ad → Affiliate Link → Advertiser Site → Convert
                                    ↑
                          Facebook loses tracking here
```

Facebook doesn't know who converted, so it can't optimize.

### **Your Advantage**

Your flow:
```
Facebook Ad → Your Site (game) → Advertiser Site → Convert
                  ↑                                    ↓
            Pixel tracks                        Postback URL
                  ↑___________________________________|
                  
            Conversions API sends data back to Facebook
```

**You tell Facebook who converted**, so it learns:
- Which interests work best
- Which ages convert most
- Which states are profitable
- Which ad creative performs

### **How Conversions API Works**

1. **User converts** on advertiser site
2. **Advertiser sends postback** to your server: `https://playtosave.net/postback?fbclid=ABC123&payout=25`
3. **Your server fires CAPI** with event data:
   ```json
   {
     "event_name": "Purchase",
     "event_time": 1706140800,
     "event_id": "ABC123",
     "user_data": {
       "fbc": "fb.1.ABC123"
     },
     "custom_data": {
       "value": 25,
       "currency": "USD"
     }
   }
   ```
4. **Facebook receives conversion** and attributes it to the ad
5. **Facebook optimizes** future delivery to similar people

---

## The Cost Per Click Journey

### **Month 1: Learning Phase**
- Broad interests
- Facebook testing
- CPC: $0.40-0.60
- Conversion rate: 2-4%
- **Cost per conversion**: $20-30

### **Month 2: Optimization**
- Pixel data accumulating
- Custom audiences active
- Lookalike 1% launching
- CPC: $0.25-0.35
- Conversion rate: 6-8%
- **Cost per conversion**: $8-15

### **Month 3: Scaling**
- 500+ conversions tracked
- Lookalikes 2-5% performing
- Retargeting profitable
- CPC: $0.18-0.25
- Conversion rate: 8-12%
- **Cost per conversion**: $3-8

### **Month 6: Optimized**
- 2,000+ conversions
- Facebook AI fully trained
- Multiple lookalikes stacked
- CPC: $0.12-0.20
- Conversion rate: 10-15%
- **Cost per conversion**: $2-5

---

## Budget Allocation Strategy

### **Starting Budget: $100/day**

```
Week 1-2: Testing ($100/day)
  $40 - Interest targeting (5 ad sets @ $8 each)
  $30 - Broad demographic (3 ad sets @ $10 each)
  $20 - Life event targeting (2 ad sets @ $10 each)
  $10 - Creative testing
  
Week 3-4: Early Optimization ($100/day)
  $50 - Best performing interests (scaled)
  $30 - Retargeting site visitors
  $20 - Lookalike 1% (if 50+ conversions)
  
Month 2: Scaling ($300/day)
  $150 - Lookalike 1-2%
  $80 - Best interest stacks
  $50 - Retargeting (game players, form starters)
  $20 - Testing new creative
  
Month 3+: Full Scale ($500-2000/day)
  $60% - Lookalike audiences (1-5%)
  $25% - Retargeting campaigns
  $10% - Interest targeting (evergreen)
  $5% - Testing/expansion
```

---

## Geographic Targeting (State-Level)

### **Why State Matters for Insurance**

Insurance offers pay different amounts by state:
- California auto quote: $35
- Texas auto quote: $28
- Wyoming auto quote: $12

### **Tier System**

```
Tier 1 States (Highest Payout):
  California, Florida, Texas, New York
  Budget: 40% of spend
  
Tier 2 States (Good Payout):
  Illinois, Pennsylvania, Ohio, Georgia
  Budget: 30% of spend
  
Tier 3 States (Lower Payout):
  All others
  Budget: 30% of spend (testing only)
```

### **Campaign Structure by State**

```
Campaign: Auto Insurance - California
  Ad Set 1: LAL 1% - CA only
  Ad Set 2: Interest: GEICO - CA only
  Ad Set 3: Retargeting - CA visitors
  Budget: $80/day
  
Campaign: Auto Insurance - Texas  
  Ad Set 1: LAL 1% - TX only
  Ad Set 2: Interest: Progressive - TX only
  Budget: $50/day
```

---

## The Real Estate Analogy

### **Bad Real Estate (Wasted Money)**
```
Everyone age 18-65 in USA
  = 200 million people
  = CPC: $0.80
  = Conversion: 0.5%
  = Burning money
```

### **Good Real Estate (Targeted)**
```
Age 30-55, interested in GEICO, California
  = 800,000 people  
  = CPC: $0.35
  = Conversion: 4%
  = Profitable
```

### **Prime Real Estate (Optimized)**
```
1% Lookalike of converters, retargeting engaged
  = 50,000 highly qualified people
  = CPC: $0.15
  = Conversion: 12%
  = Gold mine
```

---

## Common Mistakes to Avoid

### ❌ **Targeting Too Broad**
- "Everyone in USA interested in saving money"
- Result: $0.80 CPC, 1% conversion, bankruptcy

### ❌ **Targeting Too Narrow**  
- "45-year-old males in zip code 90210 who like GEICO and visited your site"
- Result: 200 people, can't scale, ad fatigue in 2 days

### ❌ **No Pixel Tracking**
- Can't build custom audiences
- Can't create lookalikes
- CPC stays high forever

### ❌ **Not Using Conversions API**
- Facebook doesn't know who converts
- Optimizes for clicks, not conversions
- You get traffic but no money

---

## The Winning Formula

```
1. Start broad (interests) to gather data
2. Install pixel on day 1 (tracking everything)
3. Build custom audiences (site visitors, game players)
4. Create lookalikes after 50+ conversions
5. Implement Conversions API (postback integration)
6. Let Facebook optimize (it's smarter than you)
7. Retarget engaged users (80% didn't convert yet)
8. Scale winning ad sets (kill losers fast)
```

---

## Real Example: Month 1 to Month 3

### **Day 1**
- Launch 5 interest-based ad sets
- Budget: $100/day total
- CPC: $0.55
- Conversions: 3/day
- Loss: $25/day (learning phase)

### **Day 15**
- Kill 3 losing ad sets
- Scale 2 winners
- Launch retargeting
- CPC: $0.42
- Conversions: 8/day
- Break even

### **Day 30**
- 240 total conversions
- Launch 1% lookalike
- Retargeting profitable
- CPC: $0.32
- Conversions: 18/day
- Profit: $180/day

### **Day 60**
- 900 total conversions
- Lookalikes 1-3% running
- Interest stacking working
- CPC: $0.24
- Conversions: 45/day
- Profit: $650/day

### **Day 90**
- 2,400 total conversions
- Fully optimized
- Multiple campaigns
- CPC: $0.19
- Conversions: 85/day
- Profit: $1,800/day

---

## Key Metrics to Watch

### **Week 1: Learning**
- CPC (should drop daily as Facebook learns)
- CTR (click-through rate - want 1%+)
- Frequency (how often same person sees ad - keep under 3)

### **Week 2-4: Optimizing**
- Cost per conversion (should drop as you kill losers)
- ROAS (return on ad spend - want 1.5x minimum)
- Pixel events (are people playing the game?)

### **Month 2+: Scaling**  
- Lookalike performance (which % converts best?)
- Retargeting ROAS (should be 3-5x)
- Geographic performance (which states are profitable?)

---

## Bottom Line

**"Buying the right real estate"** means:

1. **Start with interests** (broad targeting of relevant people)
2. **Track everything** (Pixel + Conversions API)
3. **Build custom audiences** (people who engaged)
4. **Create lookalikes** (Facebook finds similar people)
5. **Retarget engaged users** (they're warm, cheaper, convert better)
6. **Let Facebook optimize** (it has more data than you)
7. **Scale winners, kill losers** (fast iteration)

The "real estate" gets cheaper and better as Facebook learns. Month 1 you're paying $0.50/click for random people. Month 6 you're paying $0.15/click for people who **Facebook knows will convert**.

That's the magic. 🎯
