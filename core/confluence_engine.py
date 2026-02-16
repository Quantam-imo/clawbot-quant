# Confluence Detector
# Aggregates signals and publishes SIGNAL

def detect_confluence(signals):
    # signals: list of dicts with event types
    required = {'SWEEP_EVENT', 'ICEBERG_EVENT', 'DISPLACEMENT', 'BOS'}
    found = set(s['type'] for s in signals)
    if required.issubset(found):
        return {'signal': 'CONFLUENCE', 'type': 'SIGNAL'}
    return None
