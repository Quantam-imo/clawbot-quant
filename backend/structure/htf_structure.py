
class HTFStructure:
    def analyze(self, highs, lows):
        if highs[-1] < highs[-2] and lows[-1] < lows[-2]:
            return "BEARISH"
        if highs[-1] > highs[-2] and lows[-1] > lows[-2]:
            return "BULLISH"
        return "RANGE"

    def premium_discount(self, high, low, price):
        eq = (high + low) / 2
        if price > eq:
            return "PREMIUM"
        else:
            return "DISCOUNT"

    def compute_htf_structure(self, candles):
        high = max(c["high"] for c in candles)
        low = min(c["low"] for c in candles)
        eq = (high + low) / 2
        trend = self.analyze([c["high"] for c in candles], [c["low"] for c in candles])
        zone = self.premium_discount(high, low, candles[-1]["close"])
        return {
            "high": high,
            "low": low,
            "eq": eq,
            "trend": trend,
            "zone": zone
        }
