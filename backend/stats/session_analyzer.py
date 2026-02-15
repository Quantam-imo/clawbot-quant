class SessionAnalyzer:

    def summarize(self, trades):
        if not trades:
            return {"win_rate": 0, "avg_rr": 0}

        wins = [t for t in trades if t["win"]]
        avg_rr = sum(t["rr"] for t in trades) / len(trades)

        return {
            "trades": len(trades),
            "win_rate": round(len(wins) / len(trades), 2),
            "avg_rr": round(avg_rr, 2)
        }

    def weak_session(self, summary):
        return summary["win_rate"] < 0.45
