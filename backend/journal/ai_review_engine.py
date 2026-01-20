class AIReviewEngine:
    def review(self, trade, result):
        insights = []

        if result["win"]:
            insights.append("Execution followed plan")
        else:
            insights.append("Loss accepted per rules")

        if trade["confidence"] < 0.75:
            insights.append("Low-confidence trade — caution")

        return {
            "summary": insights,
            "discipline_score": self.score(trade, result)
        }

    def score(self, trade, result):
        score = 100
        if trade["confidence"] < 0.7:
            score -= 15
        if not result["win"]:
            score -= 10
        return max(score, 0)
