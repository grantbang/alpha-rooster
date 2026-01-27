# Meta Pixel Testing Guide

## Phase 3.4: Meta Pixel Integration

### Events Being Tracked

| Event | Location | Trigger | Purpose |
|-------|----------|---------|---------|
| **PageView** | All pages | Page load | Track all page visits |
| **ViewContent** | /game | Page load | Track game page views |
| **SpinWheel** (custom) | /game | Spin button click | Track engagement |
| **InitiateCheckout** | /game | Claim button click | Track conversion intent |

### Testing Without Real Pixel ID

**Current Setup:**
- Pixel code is in `base.html`
- Pixel ID loaded from `META_PIXEL_ID` environment variable
- Falls back to `"YOUR_PIXEL_ID"` if not set
- All `fbq()` calls wrapped in `typeof fbq !== 'undefined'` checks

**To Test Locally (Without Pixel):**
1. Leave `META_PIXEL_ID` empty in `.env`
2. Open browser DevTools → Console
3. Visit pages and interact
4. Look for console.log messages: "Meta Pixel: [EventName] tracked"
5. No errors should appear (fbq is safely undefined)

### Testing With Real Pixel ID

**Step 1: Get Your Pixel ID**
1. Go to Meta Events Manager: https://business.facebook.com/events_manager2
2. Create a new pixel (or use existing)
3. Copy the Pixel ID (15-16 digit number)

**Step 2: Add to Environment**
```bash
# In .env file
META_PIXEL_ID=123456789012345
```

**Step 3: Restart Server**
```bash
# Kill existing server (Ctrl+C)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8080
```

**Step 4: Test in Browser**
1. Visit http://localhost:8080/qualify
2. Open DevTools → Network tab
3. Filter by "fbevents" or "tr?"
4. You should see POST requests to facebook.com
5. Fill form, submit, spin wheel, click claim
6. Each action should fire a pixel request

**Step 5: Verify in Meta Events Manager**
1. Go to Test Events: https://business.facebook.com/events_manager2/test_events
2. Enter your IP or use browser extension
3. Interact with your site
4. Events should appear in real-time (green dots)

### Event Payload Examples

**PageView (automatic):**
```javascript
fbq('track', 'PageView');
```

**ViewContent (game page load):**
```javascript
fbq('track', 'ViewContent', {
    content_name: 'Spin Wheel Game',
    content_category: 'Game',
    fbclid: 'abc123'
});
```

**SpinWheel (custom event):**
```javascript
fbq('trackCustom', 'SpinWheel', {
    content_name: 'Wheel Spin',
    value: 1
});
```

**InitiateCheckout (claim click):**
```javascript
fbq('track', 'InitiateCheckout', {
    content_name: 'Claim Reward',
    fbclid: 'abc123'
});
```

### Network Tab Verification

**What to look for:**
- Requests to `https://www.facebook.com/tr?`
- Query params include: `id=YOUR_PIXEL_ID`, `ev=PageView`, etc.
- Status: 200 OK
- Each interaction triggers a new request

**Common Issues:**
- **No requests**: Check if `META_PIXEL_ID` is set
- **403 errors**: Pixel ID might be wrong
- **Duplicate events**: Make sure fbq('init') only called once
- **Events not in Events Manager**: Check Test Events, not live traffic

### Browser Extensions for Testing

**Meta Pixel Helper (Chrome):**
1. Install: https://chrome.google.com/webstore (search "Meta Pixel Helper")
2. Icon turns blue when pixel detected
3. Click icon to see fired events
4. Shows errors if misconfigured

### Console Logs

Our implementation logs every pixel event:
```
Meta Pixel: ViewContent tracked
Meta Pixel: SpinWheel custom event tracked
Meta Pixel: InitiateCheckout tracked
```

If you see these but no network requests, check:
- `META_PIXEL_ID` is set correctly
- No ad blockers interfering
- Browser allows third-party cookies

### Production Notes

**Before Deploying:**
- [ ] `META_PIXEL_ID` set in Cloud Run environment variables
- [ ] Test Events verified working
- [ ] Custom events (SpinWheel) approved in Meta Events Manager
- [ ] Conversion API (CAPI) integrated for redundancy (Phase 4)

**Privacy & Compliance:**
- Pixel automatically respects browser tracking preferences
- Add Privacy Policy link to footer (required by Meta)
- Consider cookie consent banner for EU traffic
- Terms of Service already includes tracking disclosure

### Next Steps (Phase 3.5)

After pixel is verified:
1. Add BigQuery logging for server-side backup
2. Implement Meta CAPI for deduplication
3. Track revenue values with conversion events
4. Build analytics dashboard

---

**Files Modified in Phase 3.4:**
- `app/templates/base.html` - Added Meta Pixel base code
- `app/templates/game.html` - Added ViewContent and InitiateCheckout tracking
- `app/static/js/wheel.js` - Added SpinWheel custom event
- `app/main.py` - Pass pixel_id to all templates
