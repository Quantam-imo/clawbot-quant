# Displacement Detector
# Detects strong momentum candle and publishes DISPLACEMENT

def detect_displacement(candles, threshold=2.0):
    displacements = []
    for c in candles:
        if abs(c['close'] - c['open']) > threshold * (c['high'] - c['low']) / 2:
            displacements.append({'minute': c['minute'], 'type': 'DISPLACEMENT'})
    return displacements
