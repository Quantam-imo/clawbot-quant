
class StructureEngine:
    def __init__(self, htf_high, htf_low):
        self.high = htf_high
        self.low = htf_low
        self.eq = (htf_high + htf_low) / 2

    def location(self, price):
        if price > self.eq:
            return "PREMIUM"
        elif price < self.eq:
            return "DISCOUNT"
        return "EQUILIBRIUM"

    def trade_allowed(self, trend, price):
        loc = self.location(price)
        if trend == "BEARISH" and loc == "PREMIUM":
            return True
        if trend == "BULLISH" and loc == "DISCOUNT":
            return True
        return False
