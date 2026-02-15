"""
Institutional Confidence, Scoring & AI Discipline Engine
Scores every potential trade across 5 pillars, enforces discipline, and blocks low-confidence execution.
"""

class ConfidenceEngine:
    def __init__(self, qmo, liquidity, iceberg_memory, execution_quality, timing):
        self.qmo = qmo
        self.liquidity = liquidity
        self.iceberg_memory = iceberg_memory
        self.execution_quality = execution_quality
        self.timing = timing

    def score_pillar(self, pillar, context):
        # Each pillar: context is a dict with relevant info
        if pillar == "QMO":
            if context.get("trend") and context.get("expansion"):
                return 18 if context["expansion"] else 15
            elif context.get("structure") == "clean_range":
                return 12
            else:
                return 6 if context.get("structure") == "chop" else 0
        if pillar == "LIQUIDITY":
            if context.get("sweep") and context.get("rejection"):
                return 20
            elif context.get("sweep"):
                return 15
            else:
                return 5
        if pillar == "ICEBERG":
            if context.get("historical_absorption") and context.get("same_price"):
                return 20
            elif context.get("historical_absorption"):
                return 15
            else:
                return 8
        if pillar == "EXECUTION":
            if context.get("tight_stop") and context.get("clear_invalidation"):
                return 20
            elif context.get("moderate_risk"):
                return 15
            else:
                return 8
        if pillar == "TIMING":
            if context.get("session_open") or context.get("cycle_turn"):
                return 20
            elif context.get("normal_timing"):
                return 15
            else:
                return 8
        return 0

    def compute_confidence(self, qmo_ctx, liquidity_ctx, iceberg_ctx, execution_ctx, timing_ctx):
        qmo_score = self.score_pillar("QMO", qmo_ctx)
        liquidity_score = self.score_pillar("LIQUIDITY", liquidity_ctx)
        iceberg_score = self.score_pillar("ICEBERG", iceberg_ctx)
        execution_score = self.score_pillar("EXECUTION", execution_ctx)
        timing_score = self.score_pillar("TIMING", timing_ctx)
        total = qmo_score + liquidity_score + iceberg_score + execution_score + timing_score
        return {
            "total": total,
            "qmo": qmo_score,
            "liquidity": liquidity_score,
            "iceberg": iceberg_score,
            "execution": execution_score,
            "timing": timing_score
        }

    def action_zone(self, total):
        if total < 60:
            return "BLOCK"
        elif total < 70:
            return "OBSERVE"
        elif total < 80:
            return "SMALL_EXECUTION"
        elif total < 90:
            return "FULL_EXECUTION"
        else:
            return "A_PLUS"

    def enforce_discipline(self, total, session_trades, last_trade_result):
        # Hard lock rules
        if total < 70:
            return False, "Confidence too low (<70). No trade."
        if session_trades >= 1:
            return False, "Max 1 trade per session. Session locked."
        if last_trade_result == "LOSS":
            return False, "First loss this session. Session locked."
        return True, "Trade allowed."

    def mentor_message(self, confidence_result, action_zone):
        total = confidence_result["total"]
        if action_zone == "BLOCK":
            return f"Setup detected but confidence = {total}%. Conditions incomplete. Observation mode only."
        if action_zone == "OBSERVE":
            return f"Setup detected. Confidence = {total}%. Monitor only."
        if action_zone == "SMALL_EXECUTION":
            return f"Trade opportunity detected. Confidence: {total}%. Small size allowed."
        if action_zone == "FULL_EXECUTION":
            return f"Trade opportunity detected. Confidence: {total}%. Full size allowed."
        if action_zone == "A_PLUS":
            return f"A+ SETUP. Confidence: {total}%. Institutional absorption confirmed. Execution approved."
        return "Unknown confidence state."
