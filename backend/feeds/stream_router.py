from feeds.message_parser import parse_trade, parse_quote
# Import your engine handlers below (implement as needed)
# from engines.orderflow import process_trade
# from engines.iceberg import process_quote
# from engines.qmo import update_qmo
# from engines.imo import update_imo

def route_message(msg):
    if msg.get("type") == "trade":
        trade = parse_trade(msg)
        # process_trade(trade)
        # update_qmo(trade)
        # update_imo(trade)
        print("TRADE:", trade)
    elif msg.get("type") == "quote":
        quote = parse_quote(msg)
        # process_quote(quote)
        print("QUOTE:", quote)
