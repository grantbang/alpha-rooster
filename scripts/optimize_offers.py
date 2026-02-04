#!/usr/bin/env python3
"""
MaxBounty Offer Optimizer
Automatically scans all approved offers and identifies best opportunities.

Usage:
    python3 scripts/optimize_offers.py --scan-all
    python3 scripts/optimize_offers.py --category insurance --min-payout 5.00
"""

import os
import sys
import argparse
import requests
import json
from datetime import datetime, timedelta
from typing import List, Dict
from dotenv import load_dotenv

load_dotenv()


class MaxBountyOptimizer:
    """Automated offer discovery and optimization."""
    
    def __init__(self):
        self.api_key = os.getenv("MAXBOUNTY_API_KEY")
        if not self.api_key:
            raise ValueError("MAXBOUNTY_API_KEY not set in .env file")
        
        self.base_url = "https://affiliates.maxbounty.com/api"
    
    def fetch_all_approved_offers(self) -> List[Dict]:
        """Get all offers you're approved for."""
        url = f"{self.base_url}/campaigns/approved"
        params = {
            "api_key": self.api_key,
            "format": "json"
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        return data.get("campaigns", [])
    
    def get_offer_stats(self, offer_id: str, days: int = 30) -> Dict:
        """Get performance stats for an offer."""
        url = f"{self.base_url}/stats"
        
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        params = {
            "api_key": self.api_key,
            "campaign_id": offer_id,
            "date_start": start_date.strftime("%Y-%m-%d"),
            "date_end": end_date.strftime("%Y-%m-%d"),
            "format": "json"
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        return response.json()
    
    def calculate_offer_score(self, offer: Dict, stats: Dict = None) -> float:
        """
        Calculate opportunity score for an offer.
        
        Scoring factors:
        - Payout amount (higher = better)
        - EPC (earnings per click)
        - Conversion rate
        - Mobile-friendly
        - Simple conversion flow
        - Geographic availability (US = higher score)
        
        Returns:
            float: Score from 0-100 (higher = better opportunity)
        """
        score = 0.0
        
        # Factor 1: Payout (0-30 points)
        payout = float(offer.get("payout", 0))
        if payout >= 20:
            score += 30
        elif payout >= 10:
            score += 20
        elif payout >= 5:
            score += 10
        
        # Factor 2: Category preference (0-20 points)
        preferred_categories = ["Insurance", "Finance", "Credit", "Loans"]
        if offer.get("category") in preferred_categories:
            score += 20
        
        # Factor 3: Geographic targeting (0-15 points)
        countries = offer.get("countries", "").upper()
        if "US" in countries or "USA" in countries:
            score += 15
        
        # Factor 4: Mobile-friendly (0-15 points)
        if offer.get("mobile_friendly", False):
            score += 15
        
        # Factor 5: Conversion type (0-10 points)
        conversion_type = offer.get("conversion_type", "").lower()
        if "email" in conversion_type or "form" in conversion_type:
            score += 10  # Simple conversions
        
        # Factor 6: Historical performance (0-10 points)
        if stats:
            epc = stats.get("epc", 0)
            if epc >= 0.50:
                score += 10
            elif epc >= 0.30:
                score += 5
        
        return round(score, 2)
    
    def find_best_offers(
        self, 
        min_payout: float = 5.0,
        category: str = None,
        top_n: int = 10
    ) -> List[Dict]:
        """
        Find the best offers to promote.
        
        Args:
            min_payout: Minimum payout threshold
            category: Filter by category (optional)
            top_n: Return top N offers
        
        Returns:
            List of offers sorted by opportunity score
        """
        print("🔍 Scanning all approved MaxBounty offers...")
        
        all_offers = self.fetch_all_approved_offers()
        print(f"   Found {len(all_offers)} approved offers\n")
        
        # Filter and score
        scored_offers = []
        for offer in all_offers:
            # Apply filters
            if float(offer.get("payout", 0)) < min_payout:
                continue
            
            if category and offer.get("category") != category:
                continue
            
            # Get stats (optional - can be slow for many offers)
            # stats = self.get_offer_stats(offer["id"])
            stats = None
            
            # Calculate score
            score = self.calculate_offer_score(offer, stats)
            
            scored_offers.append({
                "id": offer["id"],
                "name": offer["name"],
                "payout": float(offer.get("payout", 0)),
                "category": offer.get("category"),
                "countries": offer.get("countries"),
                "score": score,
                "url": f"https://affiliates.maxbounty.com/campaign/{offer['id']}"
            })
        
        # Sort by score (highest first)
        scored_offers.sort(key=lambda x: x["score"], reverse=True)
        
        return scored_offers[:top_n]
    
    def generate_optimization_report(self, offers: List[Dict]) -> str:
        """Generate markdown report of best offers."""
        report = ["# MaxBounty Offer Optimization Report"]
        report.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        report.append("## Top Opportunities\n")
        
        for i, offer in enumerate(offers, 1):
            report.append(f"### {i}. {offer['name']}")
            report.append(f"- **Offer ID:** {offer['id']}")
            report.append(f"- **Payout:** ${offer['payout']}")
            report.append(f"- **Category:** {offer['category']}")
            report.append(f"- **Countries:** {offer['countries']}")
            report.append(f"- **Opportunity Score:** {offer['score']}/100")
            report.append(f"- **URL:** {offer['url']}")
            report.append("")
        
        return "\n".join(report)


def main():
    parser = argparse.ArgumentParser(description="MaxBounty Offer Optimizer")
    parser.add_argument("--scan-all", action="store_true", help="Scan all approved offers")
    parser.add_argument("--category", type=str, help="Filter by category (e.g., Insurance)")
    parser.add_argument("--min-payout", type=float, default=5.0, help="Minimum payout (default: $5)")
    parser.add_argument("--top", type=int, default=10, help="Show top N offers (default: 10)")
    parser.add_argument("--output", type=str, help="Save report to file")
    
    args = parser.parse_args()
    
    try:
        optimizer = MaxBountyOptimizer()
        
        # Find best offers
        best_offers = optimizer.find_best_offers(
            min_payout=args.min_payout,
            category=args.category,
            top_n=args.top
        )
        
        # Print results
        print(f"🏆 Top {len(best_offers)} Offers (Score-Ranked):\n")
        for i, offer in enumerate(best_offers, 1):
            print(f"{i}. {offer['name']}")
            print(f"   Payout: ${offer['payout']} | Score: {offer['score']}/100")
            print(f"   Category: {offer['category']} | ID: {offer['id']}")
            print()
        
        # Generate report
        if args.output:
            report = optimizer.generate_optimization_report(best_offers)
            with open(args.output, 'w') as f:
                f.write(report)
            print(f"✅ Report saved to: {args.output}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
