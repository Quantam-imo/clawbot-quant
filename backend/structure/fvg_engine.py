class FVGEngine:
    def detect(self, candles):
        gaps = []
        for i in range(1, len(candles)-1):
            c1, c2, c3 = candles[i-1], candles[i], candles[i+1]
            # Bearish FVG: c1 low > c3 high
            if c1["low"] > c3["high"]:
                gaps.append({
                    "type": "BEARISH",
                    "from": c3["high"],
                    "to": c1["low"]
                })
            # Bullish FVG: c1 high < c3 low
            if c1["high"] < c3["low"]:
                gaps.append({
                    "type": "BULLISH",
                    "from": c1["high"],
                    "to": c3["low"]
                })
        return gaps
