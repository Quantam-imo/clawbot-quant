# News Block Detector
# Detects news window and publishes NEWS_STATUS

def detect_news_block(news_times, current_time):
    # news_times: list of datetime, current_time: datetime
    for nt in news_times:
        if abs((nt - current_time).total_seconds()) < 900:
            return {'status': 'NEWS_WINDOW', 'type': 'NEWS_STATUS'}
    return {'status': 'NO_NEWS', 'type': 'NEWS_STATUS'}
