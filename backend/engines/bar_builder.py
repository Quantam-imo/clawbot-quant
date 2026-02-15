from collections import defaultdict
import time

bars = defaultdict(dict)

def update_bar(symbol, price, size, timeframe="1m"):
    now = int(time.time())
    bucket = now - (now % 60)
    bar = bars.setdefault((symbol, timeframe, bucket), {
        "open": price,
        "high": price,
        "low": price,
        "close": price,
        "volume": 0
    })
    bar["high"] = max(bar["high"], price)
    bar["low"] = min(bar["low"], price)
    bar["close"] = price
    bar["volume"] += size
    return bar
