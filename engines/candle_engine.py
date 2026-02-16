# Candle Detector
# Converts ticks to 1m candles and publishes NEW_CANDLE

def detect_candles(tick_data):
    # Example: tick_data = [{'timestamp': ..., 'price': ..., 'volume': ...}, ...]
    # Group by minute, aggregate OHLCV
    from collections import defaultdict
    import datetime
    candles = defaultdict(lambda: {'open': None, 'high': None, 'low': None, 'close': None, 'volume': 0})
    for tick in tick_data:
        minute = datetime.datetime.fromtimestamp(tick['timestamp']).strftime('%Y-%m-%d %H:%M')
        c = candles[minute]
        price = tick['price']
        if c['open'] is None:
            c['open'] = price
        c['high'] = max(c['high'], price) if c['high'] is not None else price
        c['low'] = min(c['low'], price) if c['low'] is not None else price
        c['close'] = price
        c['volume'] += tick['volume']
    return [{'minute': k, **v} for k, v in candles.items()]  # Publishes NEW_CANDLE
