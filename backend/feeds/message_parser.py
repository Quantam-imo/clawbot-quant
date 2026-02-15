def parse_trade(msg):
    return {
        "type": "TRADE",
        "symbol": msg["symbol"],
        "price": float(msg["price"]),
        "size": int(msg["size"]),
        "timestamp": msg["timestamp"]
    }

def parse_quote(msg):
    return {
        "type": "QUOTE",
        "symbol": msg["symbol"],
        "bid": float(msg["bid"]),
        "ask": float(msg["ask"]),
        "bid_size": int(msg["bidSize"]),
        "ask_size": int(msg["askSize"]),
        "timestamp": msg["timestamp"]
    }
