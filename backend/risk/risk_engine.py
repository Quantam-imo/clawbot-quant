# backend/risk/risk_engine.py

class RiskEngine:

    def __init__(self, account_balance, equity_drawdown=0, daily_loss=0, trades_today=0):
        self.balance = account_balance
        self.equity_drawdown = equity_drawdown
        self.daily_loss = daily_loss
        self.trades_today = trades_today
        self.max_daily_loss = 0.02 * account_balance
        self.loss_streak = 0

    def register_trade(self, pnl):
        self.daily_loss += max(0, -pnl)
        if pnl < 0:
            self.loss_streak += 1
        else:
            self.loss_streak = 0
        self.trades_today += 1

    def allowed_trade(self, session="LONDON"):
        # Account-level caps
        if self.equity_drawdown <= -0.06:
            return False, "Account drawdown limit reached"
        if self.daily_loss >= self.max_daily_loss:
            return False, "Daily drawdown limit reached"
        if self.trades_today >= 3:
            return False, "Max trades per day reached"
        if self.loss_streak >= 3:
            return False, "Max consecutive losses reached"
        # Session caps
        session_caps = {"LONDON": 2, "NY_AM": 2, "NY_PM": 1, "ASIA": 0}
        session_loss_caps = {"LONDON": 0.01, "NY_AM": 0.01, "NY_PM": 0.005, "ASIA": 0}
        if self.trades_today >= session_caps.get(session, 0):
            return False, f"Max trades for {session} session reached"
        if self.daily_loss >= session_loss_caps.get(session, 0) * self.balance:
            return False, f"Session loss cap for {session} reached"
        return True, "SAFE"

    def position_size(self, stop_points, confidence=0.75, volatility="normal", news_soon=False):
        # Confidence-based risk
        if confidence >= 0.85:
            risk_pct = 0.005
        elif confidence >= 0.75:
            risk_pct = 0.0035
        elif confidence >= 0.70:
            risk_pct = 0.0025
        else:
            return 0.0
        # Volatility/news adjustment
        vol_map = {"normal": 1.0, "high": 0.7, "extreme": 0.4}
        multiplier = vol_map.get(volatility, 1.0)
        if news_soon:
            multiplier = min(multiplier, 0.4)
        # Drawdown adaptation
        if self.equity_drawdown <= -0.02:
            multiplier *= 0.75
        if self.equity_drawdown <= -0.04:
            multiplier *= 0.5
        risk_amount = self.balance * risk_pct
        lot_size = risk_amount / stop_points
        lot_size *= multiplier
        return round(lot_size, 2)
