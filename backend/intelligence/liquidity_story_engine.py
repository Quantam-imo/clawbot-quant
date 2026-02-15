"""
Institutional Liquidity Story Engine
Connects iceberg memory, live orderflow, and session context into a human-readable market narrative.
"""
from datetime import datetime

class LiquidityStoryEngine:
    def __init__(self, iceberg_memory):
        self.iceberg_memory = iceberg_memory

    def generate_story(self, current_price, live_orderflow, session, liquidity_targets):
        zones = self.iceberg_memory.get_active_zones(session=session)
        story = ""
        expectation = ""
        # Q1: Is price near a previous iceberg zone?
        relevant_zone = None
        for z in zones:
            if z["price_low"] <= current_price <= z["price_high"]:
                relevant_zone = z
                break
        if not relevant_zone:
            return {
                "story": "No significant institutional memory at this price. Stand down.",
                "expectation": "No trade."
            }
        # Q2: What was the original intention?
        side = relevant_zone["side"]
        date = relevant_zone["date"]
        times_retested = relevant_zone["times_retested"]
        # Q3: What is price doing now? (from live_orderflow)
        reaction = live_orderflow.get("reaction", "Unknown")
        # Q4: What liquidity is nearby?
        liquidity = ", ".join([f"{k}: {v}" for k, v in liquidity_targets.items()])
        # Story types
        if side == "SELL_ABSORPTION" and reaction == "Stalling":
            story = f"Price is revisiting a {relevant_zone['session']}-session sell absorption zone from {date}. Price has retested this zone {times_retested} times. Current price action shows stalling with no expansion above {relevant_zone['price_high']}. {liquidity}"
            expectation = "Reversal or distribution likely."
        elif side == "BUY_ABSORPTION" and reaction == "Stalling":
            story = f"Price is revisiting a {relevant_zone['session']}-session buy absorption zone from {date}. Price has retested this zone {times_retested} times. Current price action shows stalling with no breakdown below {relevant_zone['price_low']}. {liquidity}"
            expectation = "Continuation or accumulation likely."
        elif side == "SELL_ABSORPTION" and reaction == "Aggressive Expansion":
            story = f"Sell absorption zone at {relevant_zone['price_low']}-{relevant_zone['price_high']} broken by aggressive buying. Liquidity above is being targeted. {liquidity}"
            expectation = "Breakout or stop-hunt in play."
        elif side == "BUY_ABSORPTION" and reaction == "Aggressive Expansion":
            story = f"Buy absorption zone at {relevant_zone['price_low']}-{relevant_zone['price_high']} broken by aggressive selling. Liquidity below is being targeted. {liquidity}"
            expectation = "Breakdown or stop-hunt in play."
        elif times_retested > 2:
            story = f"Multiple retests of {side.lower()} zone at {relevant_zone['price_low']}-{relevant_zone['price_high']} ({times_retested}x). Range compression suggests large move coming. {liquidity}"
            expectation = "Expansion likely after absorption."
        else:
            story = f"Price is near institutional memory zone at {relevant_zone['price_low']}-{relevant_zone['price_high']} ({side.lower()}). {liquidity}"
            expectation = "Monitor for absorption or reversal."
        return {
            "story": story,
            "expectation": expectation
        }
