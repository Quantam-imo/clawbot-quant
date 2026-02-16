# Structure Break Detector
# Detects BOS/CHOCH and publishes BOS

def detect_structure_break(candles):
    # Simple example: break of previous high/low
    bos = []
    for i in range(1, len(candles)):
        if candles[i]['high'] > candles[i-1]['high']:
            bos.append({'minute': candles[i]['minute'], 'type': 'BOS'})
        if candles[i]['low'] < candles[i-1]['low']:
            bos.append({'minute': candles[i]['minute'], 'type': 'CHOCH'})
    return bos
