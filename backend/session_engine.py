
from datetime import datetime

class SessionEngine:
    def __init__(self):
        # IST hours as float (e.g., 5.5 = 05:30)
        self.sessions = {
            "ASIA": (5.5, 11.5),
            "LONDON": (13.5, 17.5),
            "NEW_YORK": (18.5, 22.5)
        }

    def current_session(self, hour):
        for name, (start, end) in self.sessions.items():
            if start <= hour <= end:
                return name
        return "DEAD"

    def is_kill_zone(self, hour):
        return (14 <= hour <= 15.5) or (19 <= hour <= 20.5)
