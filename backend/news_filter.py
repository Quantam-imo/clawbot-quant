class NewsFilter:
    def __init__(self, events):
        self.events = events

    def is_blocked(self, current_time):
        for e in self.events:
            if abs(current_time - e["time"]) <= 15:
                return e["impact"] == "HIGH"
        return False

    def is_conditional(self, event):
        return event["impact"] == "MEDIUM"
