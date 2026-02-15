class SessionEngine:
    def __init__(self, utc_time):
        self.utc_time = utc_time

    def current_session(self):
        if 7 <= self.utc_time < 10:
            return "LONDON"
        if 13.5 <= self.utc_time < 16:
            return "NY_AM"
        if 16 <= self.utc_time < 20:
            return "NY_PM"
        return "OFF_SESSION"

    def in_kill_zone(self):
        if 7 <= self.utc_time < 9:
            return "LONDON_KILL"
        if 13.5 <= self.utc_time < 15:
            return "NY_KILL"
        return None

    def time_left(self, end):
        return max(0, end - self.utc_time)

    def trading_allowed(self, qmo_state, loss_count=0, volatility=1.0, news_soon=False):
        session = self.current_session()
        if session not in ["LONDON", "NY_AM"]:
            return False
        if qmo_state != "EXECUTION":
            return False
        if loss_count >= 3:
            return False
        if volatility > 2.0:
            return False
        if news_soon:
            return False
        return True
