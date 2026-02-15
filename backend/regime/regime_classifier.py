# backend/regime/regime_classifier.py

class RegimeClassifier:
    def classify(self, context):
        vol = context["volatility"]
        structure = context["structure"]
        iceberg = context["iceberg"]
        session = context["session"]
        news = context["news"]

        # MANIPULATION
        if iceberg == "ABSORPTION" and structure == "RANGE":
            return "MANIPULATION"

        # EXPANSION
        if vol == "HIGH" and structure == "BREAKOUT":
            return "EXPANSION"

        # TRENDING
        if structure == "TREND" and vol != "LOW":
            return "TRENDING"

        # EXHAUSTION
        if iceberg == "CLIMAX" and vol == "EXTREME":
            return "EXHAUSTION"

        # DEFAULT
        return "BALANCED"
