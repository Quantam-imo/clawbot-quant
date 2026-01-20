class ConfidenceEngine:
    def score(self, qmo, imo, iceberg, structure, timing):
        return (
            qmo * 0.30 +
            imo * 0.25 +
            iceberg * 0.20 +
            structure * 0.15 +
            timing * 0.10
        )
