from datetime import datetime

class JournalEngine:
    def __init__(self, store, reviewer):
        self.store = store
        self.reviewer = reviewer

    def record_trade(self, trade):
        entry = {
            "id": f"T{int(datetime.utcnow().timestamp())}",
            "time": datetime.utcnow().isoformat(),
            "market": trade["market"],
            "session": trade["session"],
            "setup": trade["setup"],
            "entry": trade["entry"],
            "stop": trade["stop"],
            "targets": trade["targets"],
            "confidence": trade["confidence"],
            "context": trade["context"],
            "result": None
        }
        self.store.save(entry)
        return entry["id"]
