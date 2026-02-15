class PerformanceEngine:
    def expectancy(self, wins, avg_win, losses, avg_loss):
        return (wins * avg_win) - (losses * avg_loss)

    def edge_valid(self, expectancy):
        return expectancy > 0

    def risk_adjust(self, weekly_result):
        if weekly_result > 2:
            return "INCREASE_RISK"
        elif weekly_result < -1:
            return "REDUCE_RISK"
        return "HOLD"
