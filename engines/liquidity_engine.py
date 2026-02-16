# Liquidity Sweep Detector
# Detects buy/sell-side sweeps and publishes SWEEP_EVENT

def detect_liquidity_sweep(candles):
    sweeps = []
    for i in range(1, len(candles)):
        if candles[i]['high'] > candles[i-1]['high'] and candles[i]['volume'] > candles[i-1]['volume'] * 1.5:
            sweeps.append({'minute': candles[i]['minute'], 'type': 'BUY_SWEEP'})
        if candles[i]['low'] < candles[i-1]['low'] and candles[i]['volume'] > candles[i-1]['volume'] * 1.5:
            sweeps.append({'minute': candles[i]['minute'], 'type': 'SELL_SWEEP'})
    return sweeps
