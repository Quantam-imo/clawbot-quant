# backend/engines/orderflow_engine.py

class OrderFlowEngine:
    def __init__(self):
        self.window = []

    def update(self, trade):
        """
        trade = {
          price,
          size,
          side: 'BUY' or 'SELL',
          timestamp
        }
        """
        self.window.append(trade)

        # keep last 60 seconds
        cutoff = trade["timestamp"] - 60
        self.window = [t for t in self.window if t["timestamp"] >= cutoff]

    def snapshot(self):
        buy_qty = sum(t["size"] for t in self.window if t["side"] == "BUY")
        sell_qty = sum(t["size"] for t in self.window if t["side"] == "SELL")

        delta = buy_qty - sell_qty

        return {
            "buy_qty": buy_qty,
            "sell_qty": sell_qty,
            "delta": delta,
            "bias": self._bias(delta)
        }

    def _bias(self, delta):
        if delta > 500:
            return "BUY"
        elif delta < -500:
            return "SELL"
        return "NEUTRAL"

# Absorption logic

def absorption_detected(price_change, volume):
    return volume > 800 and abs(price_change) < 0.3
