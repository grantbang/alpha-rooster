# Domain Connection Guide: playtosave.net → Cloud Run

**Status:** In Progress  
**Service URL:** https://rooster-game-3fxj4ejfra-uc.a.run.app  
**Target Domain:** playtosave.net  
**Estimated Time:** 30 minutes + 5-15 min DNS propagation

---

## Step 1: Add Domain in Cloud Run Console

**Via Web Interface (Recommended):**

1. Go to: https://console.cloud.google.com/run
2. Click on service: **rooster-game**
3. Click "**MANAGE CUSTOM DOMAINS**" tab at top
4. Click "**ADD MAPPING**"
5. Select:
   - Service: **rooster-game**
   - Domain: Enter **playtosave.net**
6. Click "**CONTINUE**"

You'll see DNS records you need to add. **DO NOT CLOSE THIS WINDOW.**

---

## Step 2: Update DNS Records at Namecheap

Google will show you records like this:

```
Type: A
Name: @
Value: 216.239.32.21  (example - yours will be different)

Type: A
Name: @
Value: 216.239.34.21  (example)

Type: A
Name: @
Value: 216.239.36.21  (example)

Type: A
Name: @
Value: 216.239.38.21  (example)

Type: AAAA
Name: @
Value: 2001:4860:4802:32::15  (example)

Type: AAAA
Name: @
Value: 2001:4860:4802:34::15  (example)

Type: AAAA
Name: @
Value: 2001:4860:4802:36::15  (example)

Type: AAAA
Name: @
Value: 2001:4860:4802:38::15  (example)
```

**Add these to Namecheap:**

1. Login to Namecheap: https://www.namecheap.com/myaccount/login/
2. Dashboard → Domain List → **playtosave.net** → Manage
3. Click "**Advanced DNS**" tab
4. **REMOVE** existing A record pointing to GitHub Pages (if any)
5. **ADD** each A record shown by Google:
   - Click "ADD NEW RECORD"
   - Type: **A Record**
   - Host: **@**
   - Value: *[First IP from Google]*
   - TTL: **Automatic**
   - Repeat for all 4 A records
6. **ADD** each AAAA record (IPv6):
   - Type: **AAAA Record**
   - Host: **@**
   - Value: *[First IPv6 from Google]*
   - TTL: **Automatic**
   - Repeat for all 4 AAAA records
7. Click "**SAVE ALL CHANGES**"

---

## Step 3: Add www Subdomain (Optional but Recommended)

If you want **www.playtosave.net** to also work:

**In Cloud Run Console:**
1. Click "ADD MAPPING" again
2. This time enter: **www.playtosave.net**
3. Get the CNAME record value

**In Namecheap:**
1. ADD NEW RECORD
2. Type: **CNAME Record**
3. Host: **www**
4. Value: **ghs.googlehosted.com** (or value Google provides)
5. TTL: **Automatic**
6. Save

---

## Step 4: Wait for DNS Propagation

**Timeline:**
- Namecheap updates: Immediate
- DNS propagation: 5-15 minutes (sometimes up to 48 hours)
- SSL certificate generation: 5-15 minutes after DNS propagates

**Check progress:**

```bash
# Check if DNS updated (run every 2 minutes)
nslookup playtosave.net

# Should show Google Cloud IPs, not GitHub Pages
```

---

## Step 5: Verify Domain is Working

**Test URLs:**

```bash
# Test root domain
curl -I https://playtosave.net

# Should return: HTTP/2 200 (not 404 or certificate error)

# Test funnel
open https://playtosave.net/game
```

**Expected result:**
- ✅ Browser shows your wheel game
- ✅ HTTPS padlock is green (valid SSL)
- ✅ No certificate warnings
- ✅ Pixel events fire correctly

---

## Step 6: Update Environment Variables (If Needed)

Check if any hardcoded URLs need updating:

```bash
# Search for old Cloud Run URL
cd /Applications/alphaRooster
grep -r "rooster-game.*run.app" app/
```

If found, update to `https://playtosave.net`

---

## Step 7: Update Meta Pixel Domain

**In Facebook Events Manager:**
1. Go to: https://business.facebook.com/events_manager
2. Click your Pixel
3. Settings → Domains
4. Add: **playtosave.net**
5. Verify ownership (DNS TXT record or HTML file)

---

## Troubleshooting

### DNS Not Propagating After 1 Hour

```bash
# Check current DNS
dig playtosave.net

# If still showing old IP, clear DNS cache
sudo dscacheutil -flushcache; sudo killall -HUP mDNSResponder
```

### SSL Certificate Error

**Symptom:** "Your connection is not private" in browser

**Fix:** Wait longer (SSL cert takes 15 min after DNS propagates)

**Check status:**
```bash
gcloud run services describe rooster-game --region us-central1 --format="value(status.url)"
```

### 404 Not Found on playtosave.net

**Symptom:** Domain loads but shows 404

**Fix:** Domain mapping incomplete, retry Step 1

---

## Verification Checklist

- [ ] DNS records added to Namecheap (4 A + 4 AAAA)
- [ ] `nslookup playtosave.net` shows Google Cloud IPs
- [ ] `curl -I https://playtosave.net` returns HTTP/2 200
- [ ] Browser loads https://playtosave.net/game (no errors)
- [ ] HTTPS padlock is green
- [ ] Meta Pixel events fire on playtosave.net
- [ ] Old GitHub Pages site removed (coming_soon.html)
- [ ] Facebook Business Manager domain verified

---

## Alternative: Use gcloud CLI (Advanced)

If web console doesn't work, use CLI:

```bash
# Get service details
gcloud run services describe rooster-game --region us-central1

# Domain mapping is deprecated in newer gcloud versions
# Use Cloud Console instead
```

---

## Next Steps After Domain Connected

1. ✅ Update `.env` if any URLs hardcoded
2. ✅ Test full funnel on custom domain
3. ✅ Verify Facebook Pixel on playtosave.net
4. ✅ Update MaxBounty postback URL (if using domain in URL)
5. ✅ Move to Phase 4.1 (Build Postback Endpoint)

---

**Status:** Ready to execute  
**Estimated completion:** 30-45 minutes from start
