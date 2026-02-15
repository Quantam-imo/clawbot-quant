import json

class JournalStore:
    FILE = "trade_journal.json"

    def save(self, entry):
        data = self.load()
        data.append(entry)
        with open(self.FILE, "w") as f:
            json.dump(data, f, indent=2)

    def load(self):
        try:
            with open(self.FILE, "r") as f:
                return json.load(f)
        except:
            return []
