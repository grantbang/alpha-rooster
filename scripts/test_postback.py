#!/usr/bin/env python3
"""
Test Postback Endpoint
Simulates MaxBounty sending a conversion notification.

Usage:
    python3 scripts/test_postback.py
"""

import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Configuration
BASE_URL = os.getenv("APP_DOMAIN", "http://localhost:8080")
AFFILIATE_SECRET = os.getenv("AFFILIATE_SECRET")

if not AFFILIATE_SECRET:
    print("❌ ERROR: AFFILIATE_SECRET not set in .env file")
    print("Generate one with: openssl rand -hex 32")
    exit(1)

# Test conversion data
test_event_id = "test-conversion-abc123"
test_payout = 6.75

print(f"🧪 Testing Postback Endpoint")
print(f"   URL: {BASE_URL}/postback")
print(f"   Event ID: {test_event_id}")
print(f"   Payout: ${test_payout}")
print()

# Make request
url = f"{BASE_URL}/postback"
params = {
    "subId1": test_event_id,
    "payout": test_payout,
    "secret": AFFILIATE_SECRET
}

try:
    response = requests.get(url, params=params, timeout=10)
    
    print(f"📡 Response Status: {response.status_code}")
    print(f"📄 Response Body:")
    print(response.json())
    print()
    
    if response.status_code == 200:
        print("✅ SUCCESS: Postback endpoint is working!")
        print()
        print("Next steps:")
        print("1. Check BigQuery for conversion record:")
        print(f"   SELECT * FROM rooster_data.conversion_signals WHERE event_id = '{test_event_id}'")
        print()
        print("2. Configure postback URL in MaxBounty:")
        print(f"   https://playtosave.net/postback?subId1=[s1]&payout=[payout]&secret={AFFILIATE_SECRET}")
    else:
        print(f"❌ FAILED: Postback returned {response.status_code}")
        
except requests.exceptions.ConnectionError:
    print("❌ ERROR: Could not connect to server")
    print("Make sure FastAPI is running: uvicorn app.main:app --reload")
    
except Exception as e:
    print(f"❌ ERROR: {str(e)}")
