class VolumeProfileEngine:
    def __init__(self):
        self.profile = {}

    def build_profile(self, candles):
        volume_by_price = {}

        for c in candles:
            price = round(c["close"], 1)
            volume_by_price[price] = volume_by_price.get(price, 0) + c["volume"]

        poc = max(volume_by_price, key=volume_by_price.get)

        prices = sorted(volume_by_price.keys())
        total_vol = sum(volume_by_price.values())
        cum_vol = 0

        vah = val = poc

        for p in prices:
            cum_vol += volume_by_price[p]
            if cum_vol >= total_vol * 0.7:
                vah = p
                break

        cum_vol = 0
        for p in reversed(prices):
            cum_vol += volume_by_price[p]
            if cum_vol >= total_vol * 0.7:
                val = p
                break

        self.profile = {
            "POC": poc,
            "VAH": vah,
            "VAL": val
        }

        return self.profile
