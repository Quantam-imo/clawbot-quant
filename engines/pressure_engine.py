# Institutional Pressure Detector
# Detects buy vs sell % dominance

def detect_pressure(trades):
    # trades: [{'side': 'buy'/'sell', 'volume': ...}, ...]
    buy_vol = sum(t['volume'] for t in trades if t['side'] == 'buy')
    sell_vol = sum(t['volume'] for t in trades if t['side'] == 'sell')
    total = buy_vol + sell_vol
    if total == 0:
        return None
    buy_pct = buy_vol / total * 100
    sell_pct = sell_vol / total * 100
    return {'buy_pct': buy_pct, 'sell_pct': sell_pct, 'type': 'PRESSURE_UPDATE'}
