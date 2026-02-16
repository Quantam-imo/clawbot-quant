# Gann Range Detector
# Detects 50%, 100%, 150%, 200% range levels and publishes GANN_LEVELS

def detect_gann_levels(range_high, range_low):
    levels = {}
    base = range_high - range_low
    for pct in [0.5, 1.0, 1.5, 2.0]:
        levels[f'{int(pct*100)}%'] = range_low + base * pct
    return {'levels': levels, 'type': 'GANN_LEVELS'}
