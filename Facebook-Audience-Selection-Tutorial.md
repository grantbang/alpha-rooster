# Facebook Ads Manager - Audience Selection Tutorial
## Step-by-Step Guide to Targeting

---

## Prerequisites

1. **Facebook Business Manager account** (business.facebook.com)
2. **Ad Account created** (linked to payment method)
3. **Facebook Page** (for running ads)
4. **Meta Pixel installed** on playtosave.net (for later retargeting)

---

## Step 1: Create Your First Campaign

### Navigate to Ads Manager

1. Go to **business.facebook.com** → Click **Ads Manager**
2. Click green **"+ Create"** button (top left)
3. Choose campaign objective

### Choose Objective (Important!)

**For Day 1-30 (Cold Traffic):**
```
Select: "Traffic"
Goal: Send people to your website
Why: You want clicks to playtosave.net, not conversions yet
```

**For Day 31+ (When you have conversion data):**
```
Select: "Sales" or "Leads"
Goal: Optimize for conversions
Why: Facebook will find people who convert, not just click
```

**Click "Continue"**

---

## Step 2: Campaign Settings

### Campaign Name
```
Name: Auto Insurance - Cold Traffic - Jan 2026
```

### Budget
**Choose: Campaign Budget Optimization (CBO)**
```
Daily Budget: $50.00
Why: Facebook automatically distributes budget to best-performing ad sets
```

**Click "Next"**

---

## Step 3: Ad Set Settings (THE TARGETING PART)

This is where you select your audience!

### Ad Set Name
```
Name: Age 30-55 | GEICO Interest | USA
Tip: Name it by the targeting so you remember later
```

### Conversion Location
```
Select: Website
Your website: https://www.playtosave.net
```

### Budget & Schedule

**Ad Set Budget** (if not using CBO):
```
Daily Budget: $20.00
Start Date: Today
End Date: Ongoing
```

**Scheduling:**
```
All day (for now)
Later you can optimize: 9 AM - 9 PM performs best for insurance
```

---

## Step 4: AUDIENCE SECTION (This is what you asked about!)

### Location

**Click the "Edit" button next to Location**

#### Option 1: United States (Broad)
```
☑ United States
Type: "United States" in the search box
People living in this location: Everyone in this location
```

#### Option 2: Specific States (Better for insurance)
```
☑ California
☑ Texas  
☑ Florida
☑ New York
Type each state name, click to add
People living in this location: Everyone in this location
```

#### Option 3: Exclude Expensive States (Advanced)
```
Include: United States
Exclude: 
  - Alaska
  - Hawaii
  - Wyoming
Why: Lower payouts in these states
```

**What it looks like in the interface:**
```
┌─────────────────────────────────────┐
│ Location                            │
├─────────────────────────────────────┤
│ ⊕ United States              [Edit] │
│                                     │
│ ○ People living in this location   │
│ ○ People recently in this location │
│ ○ People traveling in this location│
└─────────────────────────────────────┘
```

---

### Age

**Scroll down to "Age"**

```
Minimum: 25
Maximum: 65

Why: 
- Under 25: Usually don't own cars/homes, low insurance intent
- 25-65: Prime insurance buying age
- Over 65: Often on fixed income, harder to convert
```

**What it looks like:**
```
┌─────────────────────────────────────┐
│ Age                                 │
├─────────────────────────────────────┤
│ [18] ──●═════════●── [65+]         │
│      25          65                 │
└─────────────────────────────────────┘
```

---

### Gender

```
Select: All genders

Why: No reason to exclude either gender for insurance
Exception: If specific offer is gender-focused (e.g., life insurance for women)
```

---

### Detailed Targeting (THE MAGIC HAPPENS HERE!)

**Click in the "Detailed Targeting" box**

This is where you select **interests**, **behaviors**, and **demographics**.

#### Method 1: Interest Targeting (Start Here)

**Type in the search box:**

**For Auto Insurance:**
```
Search: "GEICO"
☑ GEICO (Interest category)

Search: "Progressive"  
☑ Progressive Corporation (Interest category)

Search: "State Farm"
☑ State Farm (Interest category)

Search: "car ownership"
☑ Car Ownership (Behavior)

Search: "vehicle purchase"
☑ New vehicle shoppers (Behavior)
```

**What it looks like:**
```
┌─────────────────────────────────────────────────┐
│ Detailed Targeting                              │
├─────────────────────────────────────────────────┤
│ [Search interests, behaviors...]                │
│                                                 │
│ Include people who match:                       │
│ ☑ GEICO (Interest)                    ✖        │
│ ☑ Progressive Corporation (Interest)  ✖        │
│ ☑ Car Ownership (Behavior)            ✖        │
│                                                 │
│ Suggestions:                                    │
│ • Allstate                                      │
│ • Insurance                                     │
│ • Vehicle insurance                             │
└─────────────────────────────────────────────────┘
```

#### Method 2: Stacking Interests (AND vs. OR)

**AND (Narrow Audience - More Qualified)**

Click **"Narrow Audience"** button below your selections:

```
Include people who match:
☑ GEICO (Interest)
☑ Progressive Corporation (Interest)

AND must also match:
☑ Age 30-50 (Demographic)
☑ Homeowners (Behavior)

Result: People interested in GEICO AND age 30-50 AND homeowners
Audience size: 200,000 (small but qualified)
```

**OR (Broad Audience - More Reach)**

Just add multiple interests WITHOUT clicking "Narrow":

```
Include people who match:
☑ GEICO (Interest)
☑ Progressive Corporation (Interest)  
☑ State Farm (Interest)
☑ Car Ownership (Behavior)

Result: People interested in GEICO OR Progressive OR State Farm OR car ownership
Audience size: 5,000,000 (larger, less qualified)
```

**Which to use?**
- **Day 1-14**: OR (broad, let Facebook learn)
- **Day 15+**: AND (narrow, optimize for quality)

---

### Languages

```
Leave blank (default: English)

Or specify:
☑ English (All)
```

---

## Step 5: Additional Targeting Options

### Connections (Usually Skip)

```
Select: No connection restrictions

Exception: Exclude people who like your page (they already know you)
```

### Custom Audiences (Important After Day 7!)

**This appears ABOVE "Detailed Targeting"**

#### After Day 7 - Exclude Converters

```
Exclude: 
☑ Converters (Custom Audience from Pixel)

Why: Don't waste money showing ads to people who already converted
```

#### After Day 14 - Create Lookalike

```
Include:
☑ 1% Lookalike - Converters

Why: Facebook finds people similar to your converters
```

**What it looks like:**
```
┌─────────────────────────────────────────────────┐
│ Custom Audiences                                │
├─────────────────────────────────────────────────┤
│ Include people who are in:                      │
│ ☐ Website Visitors (Past 30 days)              │
│ ☑ 1% Lookalike - Converters              ✖     │
│                                                 │
│ Exclude people who are in:                      │
│ ☑ Converters                              ✖     │
│ ☑ Game Players - No Convert (7 days)     ✖     │
└─────────────────────────────────────────────────┘
```

---

## Step 6: Review Your Audience Size

**Right side panel - "Audience Definition"**

```
┌─────────────────────────────────────┐
│ Audience Definition                 │
├─────────────────────────────────────┤
│ Specific ━━━●━━━━━ Broad           │
│                                     │
│ Potential Reach:                    │
│ 2,800,000 - 3,300,000 people       │
│                                     │
│ Daily Results:                      │
│ Estimated: 140 - 400 Reach         │
│ For $20.00/day                      │
└─────────────────────────────────────┘
```

### Good Audience Size:

```
✅ 500,000 - 5,000,000: Perfect (broad enough to scale, specific enough to convert)
⚠️ 50,000 - 500,000: Okay (might get expensive, limited scale)
❌ Under 50,000: Too narrow (will burn out fast, high CPM)
❌ Over 20,000,000: Too broad (wasting money on irrelevant people)
```

---

## Example Ad Set Configurations

### Ad Set 1: Broad Interest (Day 1)

```
Name: Auto Insurance | Broad Interest | USA
Location: United States
Age: 25-65
Gender: All
Detailed Targeting:
  ☑ GEICO (Interest)
  ☑ Progressive Corporation (Interest)
  ☑ State Farm (Interest)
  ☑ Allstate (Interest)
Audience Size: 4,200,000
Budget: $20/day
```

### Ad Set 2: Behavior-Based (Day 1)

```
Name: Auto Insurance | Recent Car Buyers | USA
Location: United States
Age: 25-55
Gender: All
Detailed Targeting:
  ☑ New vehicle shoppers (Behavior)
  ☑ Car Ownership (Behavior)
Audience Size: 2,100,000
Budget: $15/day
```

### Ad Set 3: Demographic + Interest (Day 1)

```
Name: Auto Insurance | Homeowners + GEICO | CA+TX+FL
Location: California, Texas, Florida
Age: 30-55
Gender: All
Detailed Targeting:
  ☑ GEICO (Interest)
  AND (click "Narrow Audience")
  ☑ Homeowners (Behavior)
Audience Size: 850,000
Budget: $15/day
```

### Ad Set 4: Lookalike (Day 30+)

```
Name: Auto Insurance | LAL 1% Converters | USA
Location: United States
Age: 25-65
Gender: All
Custom Audiences:
  Include: 1% Lookalike - Converters
  Exclude: Converters
Detailed Targeting: (leave blank, lookalike is enough)
Audience Size: 2,100,000
Budget: $50/day
```

### Ad Set 5: Retargeting (Day 14+)

```
Name: Auto Insurance | Retarget Game Players | USA
Location: United States
Age: 25-65
Gender: All
Custom Audiences:
  Include: Game Players - No Convert (Past 14 days)
  Exclude: Converters
Detailed Targeting: (leave blank)
Audience Size: 15,000 (small, that's okay!)
Budget: $10/day
```

---

## Finding Good Interests (Discovery Methods)

### Method 1: Audience Insights Tool

1. Go to **Meta Business Suite** → **Insights** → **Audience Insights**
2. Select your current audience
3. See what else they're interested in
4. Add those interests to new ad sets

### Method 2: Suggestions in Ads Manager

When you type an interest, Facebook shows **"Suggestions"** below:

```
You typed: "GEICO"

Suggestions:
• Allstate
• Liberty Mutual
• Vehicle insurance
• Auto insurance
• Car
```

Click these to add them!

### Method 3: Competitor Research

**Interests related to insurance competitors:**
```
- GEICO
- Progressive Corporation  
- State Farm
- Allstate
- Liberty Mutual
- Farmers Insurance
- USAA
- Nationwide Mutual Insurance Company
```

**Interests related to finance (for loan offers):**
```
- Personal finance
- Debt
- Credit card
- SoFi
- LendingClub
- Marcus by Goldman Sachs
- Credit Karma
- NerdWallet
```

### Method 4: Browse Interest Categories

In Detailed Targeting, click **"Browse"** instead of search:

```
Demographics:
  → Financial → Income → $50,000 - $74,999
  → Financial → Net worth → $50,000 - $99,999
  → Home → Homeowners
  → Life events → Recently moved

Interests:
  → Business and industry → Finance
  → Hobbies and activities → Cars
  → Shopping and fashion → Car buying
  
Behaviors:
  → Automotive → Car owners
  → Financial → Banking (online)
  → Purchase behavior → Recent car buyers
```

---

## Common Mistakes to Avoid

### ❌ Mistake 1: Too Specific
```
Age 35-37, California only, Interested in GEICO AND Progressive AND owns a Tesla
Audience: 2,000 people
Result: Runs out in 2 days, super expensive
```

### ❌ Mistake 2: Too Broad  
```
Age 18-65+, Worldwide, No interests
Audience: 2 billion people
Result: $2.00 CPC, 0.5% conversion, bankruptcy
```

### ❌ Mistake 3: Overlapping Ad Sets
```
Ad Set 1: GEICO interest
Ad Set 2: Progressive interest
Ad Set 3: GEICO + Progressive interest

Result: Your own ad sets compete against each other, driving up your costs
```

### ❌ Mistake 4: Not Using Exclusions
```
Include: Website Visitors
Exclude: (nothing)

Result: Showing ads to people who already converted, wasting money
```

---

## Testing Framework (First 2 Weeks)

### Week 1: Broad Testing

```
Ad Set 1: GEICO + Progressive + State Farm ($15/day)
Ad Set 2: Car ownership behavior ($15/day)
Ad Set 3: Recent car buyers ($10/day)
Ad Set 4: Homeowners + financial interest ($10/day)

Total: $50/day
Goal: See which converts best
```

### Week 2: Kill & Scale

```
Kill: Anything with cost-per-conversion over $30
Keep: Ad sets with cost-per-conversion under $20
Scale: Best performing ad set to $30/day
Add: 2 new test ad sets at $10/day each

Total: $50-75/day
Goal: Find winners, kill losers fast
```

---

## Quick Reference Cheat Sheet

### Day 1-7: Cold Traffic (Broad Interests)
- **Location**: United States or top 4 states
- **Age**: 25-65
- **Interests**: 3-5 insurance/finance related
- **Audience Size**: 1M - 5M
- **Budget per Ad Set**: $10-20/day

### Day 8-30: Optimization (Custom Audiences)
- **Location**: Best performing states only
- **Age**: Narrow to best converting age range
- **Custom Audience**: Exclude converters
- **Retargeting**: Site visitors, game players
- **Budget**: $50-100/day total

### Day 31+: Scaling (Lookalikes)
- **Location**: Expand to all profitable states
- **Age**: Winning age range
- **Lookalike**: 1% of converters
- **Retargeting**: Multiple campaigns
- **Budget**: $100-500/day total

---

## Bottom Line

**To select your audience from Facebook:**

1. **Create campaign** → Choose "Traffic" objective
2. **At Ad Set level** → Scroll to "Audience" section
3. **Set Location** → United States (or specific states)
4. **Set Age** → 25-65 (insurance buyers)
5. **Click "Detailed Targeting"** → Type interests like "GEICO", "Progressive"
6. **Check Audience Size** → Should be 500K - 5M
7. **Repeat** for 3-5 different ad sets with different interests
8. **Launch** with $50/day total budget
9. **Wait 3-7 days** for Facebook to learn
10. **Kill losers**, **scale winners**

The interface is intuitive once you're in there. Start broad, let Facebook learn, then narrow based on data. 

Want me to walk you through creating custom audiences and lookalikes once you have pixel data?
