"""
Institutional Execution Engine
Receives liquidity story, market structure, iceberg memory, and live price behavior.
Allows or blocks execution based on strict institutional rules.
"""

class ExecutionEngine:
    def __init__(self, liquidity_story_engine, qmo, iceberg_memory):
        self.liquidity_story_engine = liquidity_story_engine
        self.qmo = qmo
        self.iceberg_memory = iceberg_memory
        self.state = "WAIT"  # WAIT, PREPARE, EXECUTE, STAND_DOWN
        self.last_session = None
        self.trades_this_session = 0
        self.session_locked = False

    def reset_session(self, session):
        if session != self.last_session:
            self.trades_this_session = 0
            self.session_locked = False
            self.last_session = session
            self.state = "WAIT"

    def evaluate(self, current_price, live_orderflow, session, liquidity_targets, news_risk, triggers):
        self.reset_session(session)
        if self.session_locked or news_risk == "HIGH":
            self.state = "STAND_DOWN"
            return self._mentor_message()
        # Step 1: All required context must be present
        story = self.liquidity_story_engine.generate_story(current_price, live_orderflow, session, liquidity_targets)
        if not story or story["story"].startswith("No significant"):
            self.state = "STAND_DOWN"
            return self._mentor_message(story)
        if not self.qmo.is_valid():
            self.state = "WAIT"
            return self._mentor_message(story)
        if not self.iceberg_memory.get_active_zones(session=session):
            self.state = "WAIT"
            return self._mentor_message(story)
        # Step 2: Execution location check
        if not self._valid_entry_location(current_price, liquidity_targets):
            self.state = "WAIT"
            return self._mentor_message(story)
        # Step 3: Trigger check
        trigger = self._detect_trigger(triggers)
        if trigger == "NONE":
            self.state = "PREPARE"
            return self._mentor_message(story)
        # Step 4: Execute
        if self.trades_this_session >= 1:
            self.state = "STAND_DOWN"
            return self._mentor_message(story)
        self.state = "EXECUTE"
        self.trades_this_session += 1
        return self._mentor_message(story, trigger)

    def _valid_entry_location(self, price, liquidity_targets):
        # Only allow at institutional locations
        # (iceberg zone, range extreme, liquidity sweep, Gann, HTF zone)
        # Example: check iceberg zone
        for z in self.iceberg_memory.get_active_zones():
            if z["price_low"] <= price <= z["price_high"]:
                return True
        # Add more checks as needed
        return False

    def _detect_trigger(self, triggers):
        # triggers: dict with keys 'absorption', 'failed_breakout', 'momentum_shift'
        if triggers.get("absorption"):
            return "ABSORPTION"
        if triggers.get("failed_breakout"):
            return "FAILED_BREAKOUT"
        if triggers.get("momentum_shift"):
            return "MOMENTUM_SHIFT"
        return "NONE"

    def _mentor_message(self, story=None, trigger=None):
        if self.state == "WAIT":
            return {
                "state": "WAIT",
                "message": story["story"] if story else "Waiting for valid execution context. Patience required."
            }
        if self.state == "PREPARE":
            return {
                "state": "PREPARE",
                "message": story["story"] + "\nWatching for execution trigger."
            }
        if self.state == "EXECUTE":
            reasons = []
            if trigger == "ABSORPTION":
                reasons.append("Absorption confirmed")
            if trigger == "FAILED_BREAKOUT":
                reasons.append("Failed breakout detected")
            if trigger == "MOMENTUM_SHIFT":
                reasons.append("Momentum shift detected")
            return {
                "state": "EXECUTE",
                "message": "EXECUTION APPROVED\nReason(s): " + ", ".join(reasons) + "\n" + (story["story"] if story else "")
            }
        if self.state == "STAND_DOWN":
            return {
                "state": "STAND_DOWN",
                "message": story["story"] if story else "No valid trade. Stand down."
            }
        return {"state": self.state, "message": "Unknown state."}
