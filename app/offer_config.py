# Offer Configuration
# Each offer has its own configuration for prepop parameters and redirect

OFFERS = {
    "champion-auto": {
        "name": "Champion Auto Insurance",
        "maxbounty_id": "22134",
        "payout": 3.00,  # Single opt-in (SOI) - $3.00 per lead
        "redirect_url": "https://afflat3c2.com/trk/lnk/A41B827D-15FA-4B0B-AD52-0CAB1F1B1F18/?o=22134&c=918277&a=784915&k=06FA1624995991BCD1B175746E5C9B06&l=22980&s1={{event_id}}&s2={{fbclid}}",
        "prepop_format": "x",  # MaxBounty uses &x= for prepop
        "fields_required": ["firstName", "lastName", "email"],  # Prepop: firstName, lastName, email only
        "daily_cap": 15,  # MaxBounty daily limit
        "active": True
    },
    "champion-home": {
        "name": "Champion Home Insurance", 
        "maxbounty_id": "29676",
        "payout": 6.00,
        "redirect_url": "https://track.maxbounty.com/visit/?bta=37191&nci=5491",  # Replace with your actual tracking link
        "prepop_format": "x",
        "fields_required": ["firstName", "lastName", "email", "zipCode"],
        "active": True
    }
    # Add more offers here as you get approved
}

def get_offer_config(offer_slug: str):
    """Get offer configuration by slug. Returns None if not found or inactive."""
    offer = OFFERS.get(offer_slug)
    if offer and offer.get("active"):
        return offer
    return None

def build_maxbounty_url(offer_config: dict, event_id: str, form_data: dict, fbclid: str = None) -> str:
    """
    Build MaxBounty redirect URL with tracking parameters and prepopulated data.
    
    Args:
        offer_config: Offer configuration dict
        event_id: Unique event ID for tracking
        form_data: Form fields dict (firstName, lastName, email, zipCode)
        fbclid: Facebook click ID (optional)
    
    Returns:
        str: Complete MaxBounty tracking URL with prepop
    
    Example:
        https://afflat3c2.com/.../?o=22134&...&s1=abc123&s2=fbclid&x=firstName%3DJohn%26lastName%3DDoe%26email%3Dtest@test.com
    """
    from urllib.parse import quote
    
    base_url = offer_config["redirect_url"]
    
    # Replace placeholders with actual values
    tracking_url = base_url.replace("{{event_id}}", event_id)
    tracking_url = tracking_url.replace("{{fbclid}}", fbclid or "")
    
    # Build prepop string: firstName=John&lastName=Doe&email=test@test.com
    prepop_params = []
    for field in offer_config["fields_required"]:
        if field in form_data and form_data[field]:
            prepop_params.append(f"{field}={form_data[field]}")
    
    if prepop_params:
        # Join with &
        prepop_string = "&".join(prepop_params)
        # Encode for URL: = becomes %3D, & becomes %26, @ becomes %40, etc.
        encoded_prepop = quote(prepop_string, safe='')
        # Add as &x= parameter
        tracking_url += f"&x={encoded_prepop}"
    
    return tracking_url
