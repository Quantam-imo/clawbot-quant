class MemoryEngine:
    def __init__(self):
        self.trades = []
        self.icebergs = []

    def record_trade(self, trade):
        self.trades.append(trade)

    def iceberg_success_rate(self, zone):
        relevant = [i for i in self.icebergs if i["zone"] == zone]
        if not relevant:
            return 0.5
        wins = [i for i in relevant if i["result"] == "WIN"]
        return len(wins) / len(relevant)
