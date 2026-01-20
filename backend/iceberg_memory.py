class IcebergMemory:
    def __init__(self):
        self.history = []

    def store(self, iceberg, session, timestamp):
        iceberg["session"] = session
        iceberg["time"] = timestamp
        self.history.append(iceberg)

    def recent(self, lookback=5):
        return self.history[-lookback:]
