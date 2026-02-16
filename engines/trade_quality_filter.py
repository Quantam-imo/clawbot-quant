# Trade Quality Filter Detector
# Detects counter-trend, bad R:R, inside value area

def detect_trade_quality(trade, trend, value_area):
    # trade: {'side': 'buy'/'sell', ...}, trend: 'up'/'down', value_area: (vah, val)
    allowed = True
    reasons = []
    if trade['side'] == 'buy' and trend == 'down':
        allowed = False
        reasons.append('Counter-trend')
    if trade.get('rr', 1) < 1.5:
        allowed = False
        reasons.append('Bad R:R')
    if value_area[0] >= trade['price'] >= value_area[1]:
        allowed = False
        reasons.append('Inside value area')
    return {'allowed': allowed, 'reasons': reasons, 'type': 'TRADE_ALLOWED' if allowed else 'TRADE_BLOCKED'}
