import time

iceberg_zones = []

def record_iceberg(price, side, strength):
    iceberg_zones.append({
        "price": price,
        "side": side,   # BUY / SELL
        "strength": strength,
        "time": time.time()
    })

def get_active_zones():
    return iceberg_zones[-10:]
