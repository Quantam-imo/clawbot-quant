# Volume Profile Detector
# Detects POC, VAH, VAL, HVN, LVN and publishes VP_UPDATE

def detect_volume_profile(candles):
    # candles: [{'minute':..., 'open':..., 'high':..., 'low':..., 'close':..., 'volume':...}, ...]
    from collections import Counter
    price_volume = Counter()
    for c in candles:
        price_volume[c['close']] += c['volume']
    sorted_prices = sorted(price_volume.items(), key=lambda x: x[1], reverse=True)
    poc = sorted_prices[0][0] if sorted_prices else None
    # VAH/VAL: top/bottom 70% volume
    total_vol = sum(price_volume.values())
    cum_vol = 0
    vah, val = None, None
    for price, vol in sorted_prices:
        cum_vol += vol
        if cum_vol >= 0.7 * total_vol and vah is None:
            vah = price
        if cum_vol >= 0.3 * total_vol and val is None:
            val = price
    return {'POC': poc, 'VAH': vah, 'VAL': val}  # Publishes VP_UPDATE
