# Execution Engine
# Consumes TRADE_ALLOWED and publishes TRADE_OPENED/TRADE_CLOSED

def execute_trade(trade_quality):
    if trade_quality['allowed']:
        return {'status': 'TRADE_OPENED', 'trade': trade_quality}
    else:
        return {'status': 'TRADE_BLOCKED', 'trade': trade_quality}

def close_trade(trade):
    return {'status': 'TRADE_CLOSED', 'trade': trade}
