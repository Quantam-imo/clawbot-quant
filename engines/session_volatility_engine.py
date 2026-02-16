# Session Volatility Detector
# Detects first 15-min expansion and publishes SESSION_REGIME

def detect_session_volatility(candles):
    # Example: first 15 candles
    first_15 = candles[:15]
    high = max(c['high'] for c in first_15)
    low = min(c['low'] for c in first_15)
    expansion = high - low
    return {'expansion': expansion, 'type': 'SESSION_REGIME'}
