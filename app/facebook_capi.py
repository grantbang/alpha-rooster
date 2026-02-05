"""
Facebook Conversions API (CAPI) Client
Phase 4.2: Send conversion events to Facebook for attribution
"""

import os
import logging
import time
from typing import Optional
from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.serverside.event import Event
from facebook_business.adobjects.serverside.event_request import EventRequest
from facebook_business.adobjects.serverside.user_data import UserData
from facebook_business.adobjects.serverside.custom_data import CustomData

logger = logging.getLogger(__name__)

# Initialize Facebook Ads API
def init_facebook_api():
    """Initialize Facebook Ads API with access token."""
    access_token = os.getenv("META_ACCESS_TOKEN")
    if not access_token:
        logger.warning("⚠️  META_ACCESS_TOKEN not set - CAPI disabled")
        return False
    
    try:
        FacebookAdsApi.init(access_token=access_token)
        logger.info("✅ Facebook Ads API initialized")
        return True
    except Exception as e:
        logger.error(f"❌ Failed to initialize Facebook API: {e}")
        return False


def send_conversion_event(
    event_id: str,
    fbclid: Optional[str],
    payout: float,
    user_agent: Optional[str] = None,
    client_ip: Optional[str] = None
) -> bool:
    """
    Send conversion event to Facebook CAPI.
    
    This tells Facebook which users converted so it can:
    - Optimize ad delivery to similar high-value users
    - Attribute revenue to the correct ad campaign
    - Improve ROAS over time through machine learning
    
    Args:
        event_id: Unique event ID for deduplication (matches browser pixel)
        fbclid: Facebook click ID from the ad click
        payout: Conversion value in dollars
        user_agent: User's browser user agent string
        client_ip: User's IP address
    
    Returns:
        bool: True if event sent successfully, False otherwise
    
    Raises:
        None - Logs errors but doesn't raise (don't block postback)
    """
    pixel_id = os.getenv("META_PIXEL_ID")
    if not pixel_id:
        logger.warning("⚠️  META_PIXEL_ID not set - skipping CAPI event")
        return False
    
    # Check if API is initialized
    if not FacebookAdsApi.get_default_api():
        if not init_facebook_api():
            return False
    
    try:
        # Build user data from fbclid
        user_data = UserData()
        
        if fbclid:
            # fbc format: fb.1.timestamp.fbclid
            fbc_value = f"fb.1.{int(time.time())}.{fbclid}"
            user_data.fbc = fbc_value
            logger.info(f"📊 CAPI user_data.fbc = {fbc_value[:50]}...")
        
        if client_ip:
            user_data.client_ip_address = client_ip
        
        if user_agent:
            user_data.client_user_agent = user_agent
        
        # Build custom data with conversion value
        custom_data = CustomData(
            value=payout,
            currency="USD"
        )
        
        # Build the conversion event
        event = Event(
            event_name="Purchase",  # Standard event for conversions
            event_time=int(time.time()),
            event_id=event_id,  # Deduplication key (matches browser pixel)
            user_data=user_data,
            custom_data=custom_data,
            event_source_url="https://playtosave.net",
            action_source="website"
        )
        
        # Send event request
        event_request = EventRequest(
            events=[event],
            pixel_id=pixel_id
        )
        
        logger.info(f"📡 Sending CAPI event: event_id={event_id}, value=${payout}")
        response = event_request.execute()
        
        logger.info(f"✅ CAPI event sent successfully: {response}")
        return True
        
    except Exception as e:
        logger.error(f"❌ CAPI event failed: {e}")
        # Don't raise - we don't want to block the postback
        return False


def send_page_view_event(
    event_id: str,
    fbclid: Optional[str],
    event_source_url: str,
    user_agent: Optional[str] = None,
    client_ip: Optional[str] = None
) -> bool:
    """
    Send PageView event to Facebook CAPI.
    
    Optional: Send page view events to improve attribution.
    Not critical for Phase 4.2 but can improve performance.
    
    Args:
        event_id: Unique event ID for deduplication
        fbclid: Facebook click ID from the ad click
        event_source_url: The URL of the page viewed
        user_agent: User's browser user agent string
        client_ip: User's IP address
    
    Returns:
        bool: True if event sent successfully, False otherwise
    """
    pixel_id = os.getenv("META_PIXEL_ID")
    if not pixel_id:
        return False
    
    if not FacebookAdsApi.get_default_api():
        if not init_facebook_api():
            return False
    
    try:
        user_data = UserData()
        
        if fbclid:
            fbc_value = f"fb.1.{int(time.time())}.{fbclid}"
            user_data.fbc = fbc_value
        
        if client_ip:
            user_data.client_ip_address = client_ip
        
        if user_agent:
            user_data.client_user_agent = user_agent
        
        event = Event(
            event_name="PageView",
            event_time=int(time.time()),
            event_id=event_id,
            user_data=user_data,
            event_source_url=event_source_url,
            action_source="website"
        )
        
        event_request = EventRequest(
            events=[event],
            pixel_id=pixel_id
        )
        
        logger.info(f"📊 Sending CAPI PageView: event_id={event_id}")
        response = event_request.execute()
        
        logger.info(f"✅ CAPI PageView sent: {response}")
        return True
        
    except Exception as e:
        logger.error(f"❌ CAPI PageView failed: {e}")
        return False
