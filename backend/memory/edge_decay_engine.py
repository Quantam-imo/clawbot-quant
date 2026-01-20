# backend/memory/edge_decay_engine.py

class EdgeDecayEngine:
    def __init__(self):
        self.stats = {}

    def update(self, key, win):
        data = self.stats.get(key, {"wins": 0, "losses": 0})
        if win:
            data["wins"] += 1
        else:
            data["losses"] += 1
        self.stats[key] = data

    def edge_strength(self, key):
        data = self.stats.get(key)
        if not data:
            return 1.0  # neutral
        total = data["wins"] + data["losses"]
        if total < 5:
            return 1.0
        return data["wins"] / total
