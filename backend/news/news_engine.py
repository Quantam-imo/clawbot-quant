from datetime import datetime, timedelta

class NewsEngine:
    def __init__(self):
        self.high_impact = [
            "FOMC", "CPI", "NFP", "PCE",
            "Interest Rate Decision", "Fed Chair"
        ]

    def classify(self, event):
        for keyword in self.high_impact:
            if keyword in event["title"]:
                return "HIGH"
        return "MEDIUM"

    def trading_allowed(self, event_time, current_time):
        before = event_time - timedelta(minutes=30)
        after = event_time + timedelta(minutes=30)
        if before <= current_time <= after:
            return False
        return True
