class JournalAnalyzer:
    def recurring_mistakes(self, journal):
        mistakes = {}
        for t in journal:
            if t["result"] and not t["result"]["win"]:
                setup = t["setup"]
                mistakes[setup] = mistakes.get(setup, 0) + 1
        return mistakes
