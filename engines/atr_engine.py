# ATR Volatility Detector
# Calculates ATR and publishes ATR values

def detect_atr(candles, period=14):
    # candles: [{'open':..., 'high':..., 'low':..., 'close':..., 'volume':...}, ...]
    trs = []
    for i in range(1, len(candles)):
        high = candles[i]['high']
        low = candles[i]['low']
        prev_close = candles[i-1]['close']
        tr = max(high - low, abs(high - prev_close), abs(low - prev_close))
        trs.append(tr)
    atr = sum(trs[-period:]) / period if len(trs) >= period else None
    return atr  # Publishes ATR values
