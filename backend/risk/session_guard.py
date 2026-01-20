# backend/risk/session_guard.py

class SessionGuard:
    def __init__(self):
        self.session_losses = {}
        self.max_session_loss = 0.0075

    def register_session_pnl(self, session, pnl, balance):
        loss = max(0, -pnl)
        self.session_losses[session] = self.session_losses.get(session, 0) + loss

        if self.session_losses[session] >= self.max_session_loss * balance:
            return False
        return True
