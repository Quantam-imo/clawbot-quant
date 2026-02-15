class NewsMemory:
    def __init__(self):
        self.history = []

    def record(self, event, reaction):
        self.history.append({
            "event": event,
            "reaction": reaction
        })

    def last_similar(self, title):
        return [
            h for h in self.history
            if title in h["event"]["title"]