"""
Alpha Rooster - BigQuery Client
Phase 3.5: Event Tracking Integration

Handles all BigQuery insert operations for user events and conversion signals.
"""

import os
import logging
from datetime import datetime
from typing import Optional
from google.cloud import bigquery
from google.api_core import retry
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logger = logging.getLogger(__name__)

# Initialize BigQuery client
try:
    project_id = os.getenv("GCP_PROJECT_ID")
    if not project_id:
        raise EnvironmentError("GCP_PROJECT_ID not set in environment variables")
    
    client = bigquery.Client(project=project_id)
    dataset_id = os.getenv("BIGQUERY_DATASET", "rooster_data")
    logger.info(f"✓ BigQuery client initialized: {project_id}.{dataset_id}")
except Exception as e:
    logger.error(f"Failed to initialize BigQuery client: {e}")
    raise


def insert_user_event(
    event_id: str,
    event_type: str,
    fbclid: Optional[str] = None,
    variant_id: Optional[str] = None,
    user_agent: Optional[str] = None
) -> bool:
    """
    Insert a user interaction event into BigQuery.
    
    Args:
        event_id: Unique event identifier (UUID)
        event_type: Type of event (page_view, qualify_submit, spin, claim_click)
        fbclid: Facebook Click ID for attribution
        variant_id: Landing page/creative variant for A/B testing
        user_agent: Browser user agent string
    
    Returns:
        bool: True if insert successful
    
    Raises:
        Exception: If BigQuery insert fails after retries
    """
    table_id = f"{project_id}.{dataset_id}.user_events"
    
    row = {
        "event_id": event_id,
        "fbclid": fbclid,
        "timestamp": datetime.utcnow().isoformat(),
        "event_type": event_type,
        "variant_id": variant_id,
        "user_agent": user_agent
    }
    
    logger.info(f"Inserting user_event: {event_type} | event_id={event_id} | fbclid={fbclid}")
    
    try:
        # insert_rows_json with automatic retry on transient failures
        errors = client.insert_rows_json(table_id, [row], retry=retry.Retry())
        
        if errors:
            logger.error(f"BigQuery insert_rows_json errors: {errors}")
            raise Exception(f"Failed to insert user_event: {errors}")
        
        logger.info(f"✓ Successfully inserted user_event: {event_id}")
        return True
        
    except Exception as e:
        logger.error(f"BigQuery insert failed for event {event_id}: {str(e)}")
        raise


def insert_conversion_signal(conversion_data: dict) -> bool:
    """
    Insert an affiliate conversion signal into BigQuery.
    
    Args:
        conversion_data: Dictionary with conversion details:
            - event_id: Unique conversion identifier (from subId1)
            - payout: Revenue amount in USD
            - status: Conversion status ("approved", "pending", "rejected")
            - conversion_time: ISO format timestamp
            - affiliate_network: Network name ("maxbounty", etc.)
            - offer_id: Affiliate offer identifier
    
    Returns:
        bool: True if insert successful
    
    Raises:
        Exception: If BigQuery insert fails after retries
    """
    table_id = f"{project_id}.{dataset_id}.conversion_signals"
    
    # Use provided data directly (already formatted in main.py)
    row = conversion_data
    
    logger.info(f"Inserting conversion_signal: event_id={row.get('event_id')} | payout=${row.get('payout')}")
    
    try:
        # insert_rows_json with automatic retry on transient failures
        errors = client.insert_rows_json(table_id, [row], retry=retry.Retry())
        
        if errors:
            logger.error(f"BigQuery insert_rows_json errors: {errors}")
            raise Exception(f"Failed to insert conversion_signal: {errors}")
        
        logger.info(f"✓ Successfully inserted conversion_signal: {row.get('event_id')} | ${row.get('payout')}")
        return True
        
    except Exception as e:
        logger.error(f"BigQuery insert failed for conversion {row.get('event_id')}: {str(e)}")
        raise


def validate_connection() -> bool:
    """
    Validate BigQuery connection by listing tables in dataset.
    
    Returns:
        bool: True if connection works
    """
    try:
        dataset_ref = f"{project_id}.{dataset_id}"
        tables = list(client.list_tables(dataset_ref))
        table_names = [table.table_id for table in tables]
        
        logger.info(f"✓ BigQuery connection validated. Tables: {table_names}")
        return True
        
    except Exception as e:
        logger.error(f"BigQuery connection validation failed: {e}")
        return False
