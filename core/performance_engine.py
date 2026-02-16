# Performance Engine
# Detects PnL, winrate, publishes trade logs

def track_performance(trades):
    wins = sum(1 for t in trades if t.get('pnl', 0) > 0)
    losses = sum(1 for t in trades if t.get('pnl', 0) <= 0)
    total = len(trades)
    winrate = wins / total * 100 if total else 0
    pnl = sum(t.get('pnl', 0) for t in trades)
    return {'winrate': winrate, 'pnl': pnl, 'trades': trades}
