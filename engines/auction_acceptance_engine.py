# Auction Acceptance / Rejection Detector
# Detects acceptance/rejection at VAH/VAL and publishes events

def detect_auction_acceptance(price, vah, val):
    if price > vah:
        return 'ACCEPTANCE_EVENT'
    elif price < val:
        return 'REJECTION_EVENT'
    else:
        return None
