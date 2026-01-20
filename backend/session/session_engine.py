from datetime import datetime, time

class SessionEngine:
    def get_session(self, utc_time):
        if time(0,0) <= utc_time < time(6,0):
            return "ASIA"
        elif time(7,0) <= utc_time < time(12,0):
            return "LONDON"
        elif time(12,30) <= utc_time < time(20,0):
            return "NEW_YORK"
        else:
            return "CLOSED"

    def is_trade_allowed(self, session, context):
        if session == "ASIA":
            return False  # marking only
        if session == "LONDON":
            return context.get("liquidity") and context.get("risk_valid")
        if session == "NEW_YORK":
            return context.get("risk_valid")
        return False
