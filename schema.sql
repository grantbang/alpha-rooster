-- Alpha Rooster - BigQuery Schema Definitions
-- Project: rooster-486417
-- Dataset: rooster_data
-- Created: February 4, 2026

-- =============================================================================
-- Table 1: user_events
-- Purpose: Track all user interactions (clicks, page views, spins, claims)
-- =============================================================================

CREATE TABLE IF NOT EXISTS `rooster-486417.rooster_data.user_events` (
  event_id STRING NOT NULL OPTIONS(description="Unique event identifier (UUID) for deduplication"),
  fbclid STRING OPTIONS(description="Facebook Click ID - primary attribution key for linking clicks to conversions"),
  timestamp TIMESTAMP NOT NULL OPTIONS(description="When the event occurred (UTC)"),
  event_type STRING NOT NULL OPTIONS(description="Event type: page_view, qualify_submit, spin, claim_click"),
  variant_id STRING OPTIONS(description="Landing page or creative variant identifier for A/B testing"),
  user_agent STRING OPTIONS(description="Browser/device user agent string for fraud detection and device analytics")
)
PARTITION BY DATE(timestamp)
OPTIONS(
  description="User interaction events from the Alpha Rooster funnel. Tracks all user actions from initial click through conversion claim."
);

-- =============================================================================
-- Table 2: conversion_signals
-- Purpose: Track affiliate conversion postbacks (revenue events)
-- =============================================================================

CREATE TABLE IF NOT EXISTS `rooster-486417.rooster_data.conversion_signals` (
  event_id STRING NOT NULL OPTIONS(description="Unique conversion identifier - links to user_events.event_id for attribution"),
  fbclid STRING OPTIONS(description="Facebook Click ID - used for Meta CAPI conversion reporting"),
  payout FLOAT64 OPTIONS(description="Revenue amount in USD from affiliate network"),
  offer_id STRING OPTIONS(description="Affiliate offer identifier (e.g. MaxBounty offer number)"),
  conversion_time TIMESTAMP NOT NULL OPTIONS(description="When the conversion occurred (UTC) - from affiliate postback"),
  raw_postback STRING OPTIONS(description="Full postback URL or payload for debugging and audit trail")
)
PARTITION BY DATE(conversion_time)
OPTIONS(
  description="Affiliate conversion postbacks for revenue tracking. Populated via /postback endpoint when user completes offer."
);

-- =============================================================================
-- Usage Notes:
-- =============================================================================
-- 
-- To create these tables, run:
--   bq query --use_legacy_sql=false < schema.sql
--
-- To add columns later (non-breaking):
--   ALTER TABLE `rooster-486417.rooster_data.user_events`
--   ADD COLUMN new_column_name STRING;
--
-- To view schema:
--   bq show rooster-486417:rooster_data.user_events
--
-- =============================================================================
