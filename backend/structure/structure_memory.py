class StructureMemory:
    def __init__(self):
        self.history = []

    def store(self, timeframe, direction, level):
        self.history.append({
            "tf": timeframe,
            "dir": direction,
            "level": level
        })

    def last(self, timeframe=None):
        for h in reversed(self.history):
            if timeframe is None or h["tf"] == timeframe:
                return h
        return None
