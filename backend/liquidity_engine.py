class LiquidityEngine:
    def detect_sweep(self, high, low, prev_high, prev_low, close):
        if high > prev_high and close < prev_high:
            return "BUY_SIDE_SWEEP"
        if low < prev_low and close > prev_low:
            return "SELL_SIDE_SWEEP"
        return None

    def iceberg_proxy(self, volume, avg_volume, candle_range, body):
        return (
            volume > avg_volume * 1.5 and
            body < candle_range * 0.3
        )
