import json
import websocket
from feeds.stream_router import route_message

CME_WS_URL = "wss://dataservices.cmegroup.com/ws"
API_KEY = "YOUR_CME_API_KEY"  # TODO: Move to environment variable

def on_message(ws, message):
    data = json.loads(message)
    route_message(data)

def on_error(ws, error):
    print("CME ERROR:", error)

def on_close(ws):
    print("CME CONNECTION CLOSED")

def on_open(ws):
    print("✅ CME CONNECTED")
    subscribe_msg = {
        "type": "subscribe",
        "channel": "marketdata",
        "symbols": ["GC"],
        "data": ["trades", "quotes"]
    }
    ws.send(json.dumps(subscribe_msg))

def start_cme_feed():
    ws = websocket.WebSocketApp(
        CME_WS_URL,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()
