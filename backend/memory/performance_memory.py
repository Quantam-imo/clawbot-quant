
class PerformanceMemory:
    def __init__(self):
        self.trades = []

    def record(self, signal_id, context, result):
        self.trades.append({
            "signal_id": signal_id,
            "context": context,
            "result": result  # pnl, r, mfe, mae
        })

    def recent(self, n=50):
        return self.trades[-n:]
