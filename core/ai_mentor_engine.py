# AI Mentor Detector
# Aggregates all signals and publishes AI_MENTOR_REPORT

def generate_ai_mentor_report(signals):
    # signals: list of dicts
    summary = f"Total signals: {len(signals)}\n"
    types = set(s['type'] for s in signals)
    summary += f"Signal types: {', '.join(types)}\n"
    return {'report': summary, 'type': 'AI_MENTOR_REPORT'}
