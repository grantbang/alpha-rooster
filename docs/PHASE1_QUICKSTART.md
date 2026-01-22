# Phase 1 Quick Start Guide
## Domain + Email + Affiliate Networks (PoC Approach)

**📌 IMPORTANT:** This guide reflects the PoC/development phase strategy where you register domain + set up professional email FIRST, then use them to apply for affiliate networks.

---

## 🎯 Why Register Domain + Email First?

**The Chicken-and-Egg Problem:**
- Affiliate networks (Impact.com, ShareASale) require a website URL + professional contact
- Without domain/email, your approval rate is 30-50% ("in development" status)
- With live domain + professional email + coming soon page, approval rate is 95%+

**The Solution:**
- Register domain TODAY ($12, 10 minutes)
- Set up professional email (FREE, 5 minutes)
- Deploy simple "Coming Soon" HTML page (no backend needed)
- Apply to affiliate networks with real URL + business email
- Work on other Phase 1 tasks while waiting 1-3 days for approval

---

## ⏱️ Timeline (Day 1 of PoC)

### Hour 1: Domain + Email Setup (20 minutes total)

**Task 1.0.1 - Register Domain (10 minutes):**

1. **Go to Namecheap.com** (or Google Domains)
2. **Search for domain:**
   - `playtosave.com` (recommended)
   - `spintoclaim.com`
   - `mysteryrewards.io`
3. **Add to cart** → Checkout ($12)
4. **Enable WHOIS privacy** (free)
5. **Enable auto-renew**

**Task 1.0.2 - Configure Professional Email (10 minutes):**

1. **In Namecheap Dashboard:**
   - Go to "Email" → "Email Forwarding"
   - Click "Add Forwarder"
   - **From:** `info@yourdomain.com`
   - **To:** your personal Gmail address
   - Save
2. **Optional:** Add `support@yourdomain.com` (same forwarding destination)
3. **Test:** Send email to `info@yourdomain.com` from another account
4. **Verify:** Email arrives in your personal inbox

**Alternative (Google Workspace - 14-day free trial):**
- Full Gmail inbox at `info@yourdomain.com`
- Then $6/month after trial
- Overkill for PoC, but option exists

**Task 1.0.3 - Deploy Coming Soon Page (5 minutes):**

1. **Go to Namecheap.com** (or Google Domains)
2. **Search for domain:**
   - `playtosave.com` (recommended)
   - `spintoclaim.com`
   - `mysteryrewards.io`
3. **Add to cart** → Checkout ($12)
4. **Enable WHOIS privacy** (free)
5. **Enable auto-renew**
**Task 1.0.3 - Deploy Coming Soon Page (5 minutes):**

1. **In Namecheap Dashboard:**
   - Go to "Hosting" → "File Manager"
   - Upload `coming_soon.html` (file in project root)
   - Rename to `index.html`
2. **Optional:** Uncomment contact email section in HTML for higher approval rates
3. **Verify:** Visit your domain in browser
4. **Screenshot:** Save as `tests/domain_live.png`

✅ **Verification:** Domain is live + professional email working + coming soon page visible

---

### Hour 2: Affiliate Applications (30 minutes)

**Task 1.1.1 - Impact.com:**

1. **Go to:** https://impact.com/publishers/
2. **Click "Join Now"**
3. **Fill out application (use these exact details):**
   - **Email:** info@yourdomain.com ← YOUR PROFESSIONAL EMAIL!
   - **Website URL:** https://yourdomain.com ← YOUR LIVE DOMAIN!
   - **Business Name:** Play to Save (or your brand name)
   - **Legal Name:** Your real name
   - **Business Type:** Sole Proprietorship
   - **Phone:** Your cell number
   - **Address:** Your home address
   - **Tax ID Type:** SSN (select "Individual" not "Corporation")
   - **Description:** 
     ```
     Performance marketing platform connecting consumers with exclusive 
     offers through gamified experiences. Currently in beta development. 
     Focus on insurance, finance, and software verticals.
     ```
   - **Traffic sources:** Meta Ads, Google Ads
   - **Promotion methods:** Interactive game experiences, email marketing
   - **Monthly visitors:** 0-1,000 (honest, you're pre-launch)
4. **Submit application**
5. **Wait 1-3 business days** for approval email (check info@yourdomain.com inbox!)

**Task 1.1.2 - ClickBank (Backup - Instant Approval):**

1. **Go to:** https://clickbank.com
2. **Click "Sign Up" → "Affiliate"**
3. **Fill out form:**
   - **Email:** info@yourdomain.com
   - **No website required!**
4. **Instant approval** - get account nickname
5. **Browse marketplace** → Search "insurance" or "finance"
6. **Note:** ClickBank has lower-quality offers (weight loss, make money online) but useful as backup

✅ **Verification:** Applications submitted, confirmation emails received at info@yourdomain.com

---

### Hours 3-4: Parallel Work (While Waiting for Approval)

**Work on Task 1.2 - GCP Setup:**
- Create GCP project
- Enable APIs (BigQuery, Cloud Run)
- Set up billing + budget alerts
- Create service account
- Create BigQuery dataset + tables

**Rationale:** Affiliate approval takes 1-3 days. Don't wait idle—build infrastructure in parallel!

---

## 📋 Checklist for End of Day 1

- [x] Domain registered ($12 spent)
- [x] Professional email configured (info@yourdomain.com)
- [x] Email forwarding tested and working
- [x] Coming soon page live
- [x] Screenshot saved (`tests/domain_live.png`)
- [x] Impact.com application submitted (using professional email)
- [x] ClickBank account created (using professional email)
- [ ] GCP project created (optional, but recommended)
- [ ] Approval emails received (wait 1-3 days, check info@yourdomain.com)

**Status:** Domain live, professional email active, affiliate applications pending, ready to work on infrastructure

**💡 Pro Tip:** Set up email forwarding on your phone so you get instant notifications when Impact.com approves your account!

---

## 🎯 Day 2-3: While Waiting for Approval

**Continue Phase 1 tasks:**
- ✅ 1.2: GCP setup (can complete independently)
- ✅ 1.3: Meta Business Manager (can complete independently)
- ✅ 1.4: Legal docs (Privacy Policy, Terms - can complete independently)

**By Day 3, you should have:**
- ✅ Approved affiliate offers (check email!)
- ✅ GCP infrastructure ready
- ✅ Meta Pixel + CAPI configured
- ✅ Legal docs generated
- 🚀 **Ready to start Phase 2 (Creative Assets) and Phase 3 (Game Build)**

---

## 💡 Pro Tips

**Tip 1:** Use professional email for EVERYTHING going forward
- Impact.com, ClickBank: info@yourdomain.com
- Google Cloud Platform: info@yourdomain.com  
- Meta Business Manager: info@yourdomain.com
- Looks professional, centralizes all business notifications

**Tip 2:** Use your domain in Impact.com application even if it just shows "Coming Soon"
- Networks understand pre-launch sites
- Shows professionalism vs. "I don't have a site yet"

**Tip 2:** Apply to both Impact.com AND ClickBank
- ClickBank = instant approval, lower payouts ($10-30)
- Impact.com = 1-3 day approval, higher payouts ($30-200)
- Use ClickBank immediately, upgrade to Impact.com when approved

**Tip 3:** Don't wait for affiliate approval to start building
- You need GCP + Meta setup regardless of which offers you promote
- Build game mechanics in Phase 3 while waiting
- Swap in affiliate tracking links once approved

**Tip 4:** Keep coming soon page until game is ready
- Don't point domain to game app until Phase 3.6 (deployment)
- Replace coming soon page with game only when fully tested
- No harm in having simple page during PoC phase

---

## 📞 What If You Get Rejected?

**If Impact.com rejects (10% chance):**
1. Check rejection reason in email
2. Common fixes:
   - Add more content to coming soon page (add "About" section, contact form)
   - Wait 30 days, reapply with more developed site
3. Use ClickBank in the meantime (still profitable!)

**If ClickBank rejects (rare, <1% chance):**
- Check for duplicate accounts (they ban multiple accounts per person)
- Contact support@clickbank.com

---

## 🚀 Next Steps

**Once approved:**
1. Update `PHASE_TRACKER.md`:
   - Check off 1.0.1, 1.0.2, 1.1.1, 1.1.2
   - Add domain name to verification notes
   - Add screenshot filename
2. **Proceed to Task 1.1.3:** Apply to 5-10 offers in Impact.com marketplace
3. **Document tracking links** in spreadsheet (Task 1.1.4)
4. **Continue Phase 1** → Complete by end of Day 2

**Questions?** Check README.md Part 3 for detailed task breakdown.

---

**Last Updated:** January 22, 2026
