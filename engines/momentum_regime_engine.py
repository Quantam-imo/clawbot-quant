# Momentum Regime Detector
# Detects 3 consecutive displacement candles and publishes TREND_MODE

def detect_momentum_regime(displacements):
    trend = []
    for i in range(2, len(displacements)):
        if (displacements[i-2]['type'] == 'DISPLACEMENT' and
            displacements[i-1]['type'] == 'DISPLACEMENT' and
            displacements[i]['type'] == 'DISPLACEMENT'):
            trend.append({'minute': displacements[i]['minute'], 'type': 'TREND_MODE'})
    return trend
