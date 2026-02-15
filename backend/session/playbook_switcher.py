# backend/session/playbook_switcher.py

class SessionPlaybookSwitcher:

    def get_session(self, hour_utc):
        if 0 <= hour_utc < 6:
            return "ASIA"
        if 6 <= hour_utc < 12:
            return "LONDON"
        if 12 <= hour_utc < 20:
            return "NEW_YORK"
        return "ROLL"

    def allowed_setups(self, session, regime):
        playbooks = {
            "ASIA": {
                "BALANCED": ["RANGE", "VWAP"],
                "MANIPULATION": ["ICEBERG_ACCUMULATION"],
                "default": []
            },
            "LONDON": {
                "MANIPULATION": ["STOP_HUNT", "ICEBERG_FADE"],
                "EXPANSION": ["BREAKOUT"],
                "default": ["VWAP"]
            },
            "NEW_YORK": {
                "TRENDING": ["BOS", "CONTINUATION"],
                "EXHAUSTION": ["REVERSAL", "GANN_200"],
                "default": ["EXECUTION"]
            },
            "ROLL": {
                "default": ["NO_TRADE"]
            }
        }

        return playbooks.get(session, {}).get(regime,
               playbooks.get(session, {}).get("default", []))
