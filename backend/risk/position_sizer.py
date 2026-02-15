class PositionSizer:
    def calculate_lot_size(self, balance, risk_percent, stop_loss_pips, pip_value, volatility="normal", reduce=False):
        # Volatility multipliers
        vol_map = {"normal": 1.0, "high": 0.7, "extreme": 0.4}
        multiplier = vol_map.get(volatility, 1.0)
        if reduce:
            multiplier *= 0.5
        risk_amount = balance * risk_percent
        lot_size = risk_amount / (stop_loss_pips * pip_value)
        lot_size *= multiplier
        return round(lot_size, 2)

    def get_risk_percent(self, confidence):
        if confidence >= 0.85:
            return 0.01
        elif confidence >= 0.75:
            return 0.0075
        elif confidence >= 0.70:
            return 0.005
        else:
            return 0.0

    def session_risk_cap(self, session):
        if session == "ASIA":
            return 0.005
        elif session in ["LONDON", "NEW_YORK"]:
            return 0.015
        return 0.0

    def kill_switch(self, daily_loss, loss_count):
        if daily_loss <= -0.02:
            return "locked"
        elif daily_loss <= -0.015 or loss_count >= 2:
            return "reduced"
        return "normal"
