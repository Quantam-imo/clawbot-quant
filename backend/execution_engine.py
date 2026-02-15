

class ExecutionEngine:
    def __init__(self, balance):
        self.balance = balance
        self.daily_loss = 0

    def validate(self, context):
        required = [
            context["qmo"],
            context["liquidity"],
            context["smt"],
            context["iceberg"],
            context["session"]
        ]
        return all(required)

    def validate_entry(self, htf_bias, iceberg, ltf_trigger):
        return htf_bias and iceberg and ltf_trigger

    def calculate_stop(self, highest_wick, buffer=3):
        return highest_wick + buffer

    def targets(self, liquidity_levels):
        return liquidity_levels

    def build_trade(self, entry, stop, targets, risk):
        return {
            "entry": entry,
            "stop": stop,
            "targets": targets,
            "risk": risk
        }

    def position_size(self, risk_pct, stop_points):
        risk_amount = self.balance * risk_pct
        return risk_amount / stop_points

    def allow_trade(self, daily_loss):
        return daily_loss > -0.02 * self.balance
