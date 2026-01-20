
class IcebergEngine:
    def __init__(self):
        self.active_zones = []

    def detect_sell_iceberg(self, candles):
        rejections = 0
        for c in candles[-6:]:
            body = abs(c["close"] - c["open"])
            wick = c["high"] - max(c["open"], c["close"])
            if wick > body:
                rejections += 1
        return rejections >= 3
