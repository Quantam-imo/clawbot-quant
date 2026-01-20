
class ConfidenceEngine:
    WEIGHTS = {
        "qmo": 0.30,
        "imo": 0.25,
        "gann": 0.20,
        "astro": 0.15,
        "cycle": 0.10
    }

    def calculate(self, scores):
        confidence = 0
        for key, weight in self.WEIGHTS.items():
            confidence += scores.get(key, 0) * weight
        return round(confidence, 2)

    def grade(self, confidence):
        if confidence >= 0.85:
            return "A+"
        elif confidence >= 0.75:
            return "A"
        elif confidence >= 0.65:
            return "B"
        else:
            return "C"
