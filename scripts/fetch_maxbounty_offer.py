#!/usr/bin/env python3
"""
MaxBounty Offer Details Extractor
Extracts offer details from browser console using copy(document.body.innerText).

Since MaxBounty doesn't have a public API, this script processes
text copied from the offer page in your browser.

Usage:
    1. Open MaxBounty offer page in browser
    2. Press F12 → Console tab
    3. Run: copy(document.body.innerText)
    4. Paste into: /Applications/alphaRooster/app/offers/offer-29678-raw.txt
    5. Run: python3 scripts/fetch_maxbounty_offer.py 29678
"""

import os
import re
import json
from pathlib import Path
from typing import Dict, Optional

def parse_offer_text(text: str, offer_id: str) -> Dict:
    """
    Parse offer details from raw text copied from MaxBounty offer page.
    
    Args:
        text: Raw text from document.body.innerText
        offer_id: MaxBounty offer number (e.g., "29678")
    
    Returns:
        dict: Extracted offer details
    """
    offer = {
        "id": offer_id,
        "name": None,
        "payout": None,
        "description": None,
        "countries": [],
        "restrictions": [],
        "qualifying_actions": None,
        "allowed_traffic": [],
        "daily_cap": None,
        "epc": None,
        "category": None,
        "raw_text": text
    }
    
    # Extract offer name (format: "OfferName - Type - CPL (US) ID: 29678")
    name_match = re.search(r'(.+?)\s*-\s*(?:Auto|Home|Life|Health)?\s*(?:Insurance|CPL|CPA)\s*-?\s*(?:\([A-Z]+\))?\s*ID:\s*\d+', text)
    if name_match:
        offer["name"] = name_match.group(1).strip()
    
    # Extract category
    category_match = re.search(r'(Insurance|Finance|Credit|Health|Software|Education)\s*-\s*(\w+)', text)
    if category_match:
        offer["category"] = f"{category_match.group(1)} - {category_match.group(2)}"
    
    # Extract payout
    payout_match = re.search(r'\$?([\d.]+)\s*(?:per|/)\s*(?:lead|sale|action|conversion)', text, re.IGNORECASE)
    if payout_match:
        offer["payout"] = float(payout_match.group(1))
    
    # Extract EPC
    epc_match = re.search(r'EPC\s*\$?([\d.]+)', text, re.IGNORECASE)
    if epc_match:
        offer["epc"] = float(epc_match.group(1))
    
    # Extract countries/geo
    geo_match = re.search(r'Countries?\s+Allowed\s+(.+?)(?:\n\n|Devices)', text, re.IGNORECASE | re.DOTALL)
    if geo_match:
        countries_text = geo_match.group(1).strip()
        offer["countries"] = [c.strip() for c in countries_text.split('\n') if c.strip()]
    
    # Extract allowed traffic types
    traffic_match = re.search(r'Allowed Traffic Types\s+(.+?)(?:\n|Your Status)', text, re.IGNORECASE | re.DOTALL)
    if traffic_match:
        traffic_text = traffic_match.group(1).strip()
        # Split on capital letters (e.g., "DisplaySearchSocial" -> ["Display", "Search", "Social"])
        traffic_types = re.findall(r'[A-Z][a-z]*(?:\s+[A-Z][a-z]*)*', traffic_text)
        offer["allowed_traffic"] = traffic_types
    
    # Extract daily cap
    cap_match = re.search(r'Daily Cap\s+(\d+)\s+actions', text, re.IGNORECASE)
    if cap_match:
        offer["daily_cap"] = int(cap_match.group(1))
    
    # Extract description (from Campaign Description section)
    desc_match = re.search(r'Campaign Description\s+(.+?)(?:Converts on|Targeting:|Restrictions:|Tracking)', text, re.IGNORECASE | re.DOTALL)
    if desc_match:
        offer["description"] = desc_match.group(1).strip()
    
    # Extract qualifying actions (what converts)
    converts_match = re.search(r'Converts on\s+(.+?)\.', text, re.IGNORECASE)
    if converts_match:
        offer["qualifying_actions"] = converts_match.group(1).strip()
    
    # Extract restrictions
    restrictions_match = re.search(r'Restrictions:\s*(.+?)(?:\n\n|Tracking|$)', text, re.IGNORECASE | re.DOTALL)
    if restrictions_match:
        restrictions_text = restrictions_match.group(1).strip()
        offer["restrictions"] = [r.strip() for r in restrictions_text.split('.') if r.strip()]
    
    return offer


def process_offer(offer_id: str):
    """
    Process offer details from raw text file.
    
    Args:
        offer_id: MaxBounty offer number
    """
    input_path = f"/Applications/alphaRooster/app/offers/offer-{offer_id}-raw.txt"
    output_path = f"/Applications/alphaRooster/app/offers/offer-{offer_id}.json"
    
    # Check if raw text file exists
    if not Path(input_path).exists():
        print(f"❌ File not found: {input_path}\n")
        print("📋 To create this file:")
        print(f"   1. Open https://affiliates.maxbounty.com/campaign/{offer_id}")
        print(f"   2. Press F12 → Console tab")
        print(f"   3. Paste: copy(document.body.innerText)")
        print(f"   4. Press Enter")
        print(f"   5. Create file: code {input_path}")
        print(f"   6. Paste (Cmd+V) and save")
        print(f"   7. Run this script again")
        return
    
    # Read raw text
    print(f"📖 Reading offer #{offer_id} from: {input_path}")
    with open(input_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    
    # Parse offer details
    offer_data = parse_offer_text(raw_text, offer_id)
    
    # Save to JSON
    with open(output_path, 'w') as f:
        json.dump(offer_data, f, indent=2)
    
    print(f"✅ Saved offer details to: {output_path}\n")
    
    # Print extracted details
    print("📊 Extracted Offer Details:")
    print(f"   Name: {offer_data.get('name') or '(not found)'}")
    print(f"   Payout: ${offer_data.get('payout') or '(not found)'}")
    print(f"   Countries: {', '.join(offer_data.get('countries', [])) or '(not found)'}")
    print(f"   Description: {(offer_data.get('description') or '(not found)')[:200]}...")
    if offer_data.get('restrictions'):
        print(f"   Restrictions: {len(offer_data['restrictions'])} items")
    
    return offer_data


if __name__ == "__main__":
    import sys
    
    # Get offer ID from command line or use default
    offer_id = sys.argv[1] if len(sys.argv) > 1 else "29678"
    process_offer(offer_id)
