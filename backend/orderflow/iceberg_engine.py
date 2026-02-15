class IcebergDetector:

    def detect(self, candles, htf_zone=None, session=None, liquidity_sweep=False):
        recent = candles[-6:]
        highs = [c["high"] for c in recent]
        lows = [c["low"] for c in recent]
        volumes = [c["volume"] for c in recent]
        price_range = max(highs) - min(lows)
        volume_avg = sum(volumes) / len(volumes)
        # Absorption: tight range, rising volume
        absorption = price_range < 0.4 * (max(highs) - min(lows)) and volume_avg > 1.2 * volumes[-1]
        # Distribution: repeated high tests, volume up, price not breaking higher
        distribution = price_range < 0.4 * (max(highs) - min(lows)) and volume_avg > 1.2 * volumes[-1]
        # Context filter: only valid if HTF zone, session, and liquidity sweep
        if not (htf_zone and session and liquidity_sweep):
            return None
        # Confidence grading
        strength = "A" if absorption and volume_avg > 2 * volumes[-1] else ("B" if absorption else "C")
        if absorption:
            return {
                "type": "BUY_ICEBERG",
                "strength": strength,
                "range": (min(lows), max(highs)),
                "session": session
            }
        if distribution:
            return {
                "type": "SELL_ICEBERG",
                "strength": strength,
                "range": (min(lows), max(highs)),
                "session": session
            }
        return None
