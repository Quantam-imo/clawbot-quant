class AuctionEngine:
    def evaluate(self, price, profile, delta):
        if price > profile["VAH"] and delta < 0:
            return "REJECTION_ABOVE"

        if price < profile["VAL"] and delta > 0:
            return "REJECTION_BELOW"

        if profile["VAL"] <= price <= profile["VAH"]:
            return "ACCEPTANCE"

        return "INITIATIVE"
