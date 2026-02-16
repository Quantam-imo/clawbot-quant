import databento as db
from datetime import datetime

def get_ohlc_candles(api_key, symbol, dataset, limit=100, interval="5m", start=None, end=None):
    """
    Fetch OHLC candles from Databento. If start/end are provided, use Historical API, else use Live API.
    """
    interval_map = {
        "1m": 60,
        "5m": 300,
        "15m": 900,
        "1h": 3600,
        "4h": 14400,
        "1d": 86400
    }
    seconds = interval_map.get(interval, 300)
    candles = []
    if start and end:
        # Use Databento Historical API with continuous contract symbology for Gold Futures
        client = db.Historical(api_key)
        # Override symbol and stype_in for Gold Futures continuous contract
        db_symbol = "GC.n.0"
        data = client.timeseries.get_range(
            dataset=dataset,
            schema="trades",
            symbols=[db_symbol],
            stype_in="continuous",
            start=start,
            end=end,
            limit=limit
        )
        current_candle = None
        candle_start = None
        candle_count = 0
        for msg in data:
            # Only process messages that have all required attributes
            if not (hasattr(msg, "ts") and hasattr(msg, "price") and hasattr(msg, "size")):
                continue
            ts = datetime.fromtimestamp(msg.ts / 1e9)
            if candle_start is None:
                candle_start = ts.replace(second=0, microsecond=0)
                current_candle = {
                    "timestamp": candle_start.isoformat(),
                    "open": msg.price / 1e9,
                    "high": msg.price / 1e9,
                    "low": msg.price / 1e9,
                    "close": msg.price / 1e9,
                    "volume": msg.size
                }
            elif (ts - candle_start).total_seconds() >= seconds:
                candles.append(current_candle)
                candle_count += 1
                if candle_count >= limit:
                    break
                candle_start = ts.replace(second=0, microsecond=0)
                current_candle = {
                    "timestamp": candle_start.isoformat(),
                    "open": msg.price / 1e9,
                    "high": msg.price / 1e9,
                    "low": msg.price / 1e9,
                    "close": msg.price / 1e9,
                    "volume": msg.size
                }
            else:
                price = msg.price / 1e9
                current_candle["high"] = max(current_candle["high"], price)
                current_candle["low"] = min(current_candle["low"], price)
                current_candle["close"] = price
                current_candle["volume"] += msg.size
        if current_candle and candle_count < limit:
            candles.append(current_candle)
        print(f"[Databento] Loaded {len(candles)} historical candles from Databento (GC.n.0, continuous contract).")
        return candles
    else:
        # Use Databento Live API
        client = db.Live(key=api_key)
        client.subscribe(dataset=dataset, schema="trades", symbols=[symbol])
        current_candle = None
        candle_start = None
        candle_count = 0
        for msg in client:
            # Only process messages that have all required attributes
            if not (hasattr(msg, "ts") and hasattr(msg, "price") and hasattr(msg, "size")):
                continue
            ts = datetime.fromtimestamp(msg.ts / 1e9)
            if candle_start is None:
                candle_start = ts.replace(second=0, microsecond=0)
                current_candle = {
                    "timestamp": candle_start.isoformat(),
                    "open": msg.price / 1e9,
                    "high": msg.price / 1e9,
                    "low": msg.price / 1e9,
                    "close": msg.price / 1e9,
                    "volume": msg.size
                }
            elif (ts - candle_start).total_seconds() >= seconds:
                candles.append(current_candle)
                candle_count += 1
                if candle_count >= limit:
                    break
                candle_start = ts.replace(second=0, microsecond=0)
                current_candle = {
                    "timestamp": candle_start.isoformat(),
                    "open": msg.price / 1e9,
                    "high": msg.price / 1e9,
                    "low": msg.price / 1e9,
                    "close": msg.price / 1e9,
                    "volume": msg.size
                }
            else:
                price = msg.price / 1e9
                current_candle["high"] = max(current_candle["high"], price)
                current_candle["low"] = min(current_candle["low"], price)
                current_candle["close"] = price
                current_candle["volume"] += msg.size
        if current_candle and candle_count < limit:
            candles.append(current_candle)
        print(f"[Databento] Loaded {len(candles)} candles from Databento.")
        return candles
