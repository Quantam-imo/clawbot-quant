class SessionStatsEngine:
    def __init__(self):
        self.data = {
            "ASIA": [],
            "LONDON": [],
            "NEW_YORK": [],
            "ROLL": []
        }

    def record_trade(self, session, result):
        """
        result = {
          "setup": "ICEBERG_FADE",
          "rr": 2.1,
          "win": True,
          "confidence": 0.82
        }
        """
        self.data[session].append(result)

    def get_session_data(self, session):
        return self.data.get(session, [])
