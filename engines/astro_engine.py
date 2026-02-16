# Astro Timing Detector
# Detects planetary cycle times and publishes ASTRO_EVENT

def detect_astro_event(planetary_times, current_time):
    # planetary_times: list of datetime, current_time: datetime
    for pt in planetary_times:
        if abs((pt - current_time).total_seconds()) < 600:
            return {'event': 'PLANETARY_CYCLE', 'type': 'ASTRO_EVENT'}
    return {'event': 'NO_EVENT', 'type': 'ASTRO_EVENT'}
