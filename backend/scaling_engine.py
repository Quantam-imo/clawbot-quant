class ScalingEngine:
    def __init__(self, account_size, risk_pct=0.0025):
        self.account_size = account_size
        self.risk_pct = risk_pct
        self.scaling_locked = False

    def update_account(self, new_size):
        self.account_size = new_size

    def position_risk(self):
        return self.account_size * self.risk_pct

    def can_scale(self, last_phase_profitable, drawdown_ok, rules_ok, data_ok, psychology_ok, system_unchanged):
        return all([
            last_phase_profitable,
            drawdown_ok,
            rules_ok,
            data_ok,
            psychology_ok,
            system_unchanged
        ]) and not self.scaling_locked

    def freeze_scaling(self):
        self.scaling_locked = True

    def unfreeze_scaling(self):
        self.scaling_locked = False

    def withdraw(self, profit, percent=0.25):
        withdrawal = profit * percent
        self.account_size -= withdrawal
        return withdrawal
