class SMTDetector:
    def bearish_smt(self, a_high, b_high):
        return a_high > b_high

    def bullish_smt(self, a_low, b_low):
        return a_low < b_low
