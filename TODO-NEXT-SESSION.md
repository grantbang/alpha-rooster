# TODO - Pick Up Here Next Session
**Last updated:** February 18, 2026  
**Status:** Game page wired up correctly, need to deploy and launch

---

## ✅ What's Working RIGHT NOW
- Spinner game at `localhost:8080/game?fbclid=test`
- Correct Champion Auto offer URL in game.html (`o=22134`)
- `s1=event_id` + `s2=fbclid` tracking in the redirect URL
- Meta Pixel fires `Lead` event when user clicks "Claim My Reward"
- BigQuery logs `game_load` events
- Postback endpoint exists at `/postback`

---

## ❌ What's NOT Done (Blocking Launch)

### 1. Deploy to Cloud Run (30 min)
You need a public URL before anything else works.
```bash
gcloud run deploy rooster-game \
  --source . \
  --region us-central1 \
  --allow-unauthenticated
```
→ You'll get a URL like: `https://rooster-game-xxx-uc.a.run.app`

### 2. Configure MaxBounty Global Postback (5 min)
This is how MaxBounty tells you when someone converts (= when you get paid $3).
- Log into MaxBounty → Profile Settings → Global Postback URL
- Set it to:
```
https://YOUR-CLOUD-RUN-URL.run.app/postback?subId1={s1}&payout={payout}&secret=dca9f8aa24d495b96e42356c7621766dcb15d5682fcc4a153b0b71b9fa43a58c
```
- Replace `YOUR-CLOUD-RUN-URL` with the real URL from Step 1
- `{s1}` and `{payout}` are MaxBounty's variables — leave them exactly as-is

### 3. Create Facebook Ad Campaign (45 min)
- Objective: **Leads** (or Conversions → Lead event)
- Pixel: `2066263104107367`
- Landing page URL: `https://YOUR-CLOUD-RUN-URL.run.app/game?fbclid={{fbclid}}`
- Budget: Start with **$20/day**
- Targeting: US, ages 25-65, interests: auto insurance, car ownership
- Creative: Use the testimonials image + "Spin to see how much you could save"

---

## 🧠 Key Things to Remember

### How you get paid:
```
Ad click → Your game page → Spin wheel → "Claim" button → 
Champion form (MaxBounty) → User SUBMITS Champion form → You get $3.00
```
You do NOT get paid just for spins or clicks. Only when Champion form is submitted.

### The funnel logic (why it works):
- Your game page = engagement/pre-lander (NOT a bridge page - it adds value)
- Champion form = the actual lead collection (MaxBounty's page)
- You only collect event_id and fbclid — no duplicate questions

### Daily cap:
- MaxBounty cap is **15 conversions/day** = max $45/day revenue
- Keep ad spend under $30/day to start (need positive ROI)

---

## 📁 Key Files
| File | Purpose |
|------|---------|
| `app/templates/game.html` | The spinner game (your pre-lander) |
| `app/main.py` | Route `/game` serves the game |
| `app/offer_config.py` | Champion Auto offer config + URL builder |
| `.env` | All credentials (never commit this) |
| `Dockerfile` | For Cloud Run deployment |

---

## 🚨 One Security Thing
Rotate your Meta Access Token — it was visible in chat.
- Go to: Meta Business → System Users → Generate New Token
- Update `.env`: `META_ACCESS_TOKEN=new_token_here`
- Update Cloud Run secret after deploy

---

## Sequence When You're Back:
1. `gcloud run deploy ...` → get public URL
2. Set MaxBounty postback URL
3. Test postback: `curl "https://YOUR-URL/postback?subId1=test&payout=3.00&secret=dca9f8aa24d495b96e42356c7621766dcb15d5682fcc4a153b0b71b9fa43a58c"`
4. Create Facebook ad pointing to game page
5. Monitor: MaxBounty dashboard + BigQuery + Facebook Ads Manager
