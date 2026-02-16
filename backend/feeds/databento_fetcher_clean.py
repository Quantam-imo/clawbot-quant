from dotenv import load_dotenv
load_dotenv()
import os
from collections import defaultdict
from backend.feeds.databento_ohlc_clean import get_ohlc_candles

class DatabentoCMLiveStream:
    def __init__(self, api_key: str = None):
        self.api_key = api_key or os.getenv("DATABENTO_API_KEY")
        if not self.api_key:
            raise ValueError("❌ DATABENTO_API_KEY not found. Set environment variable or pass to constructor.")
        self.symbol = "GCG6"  # Gold Futures - Feb 2026 front month contract
        self.dataset = "GLBX.MDP3"  # CME Globex
        self.client = None
        self.is_connected = False
        self.latest_price = None
        self.latest_bid_ask = None
        self.volume_profile = defaultdict(int)
        self.iceberg_zones = []
        print(f"📊 Databento initialized for {self.symbol} on {self.dataset}")
        print(f"🔑 API Key: {self.api_key[:8]}***")

    async def get_ohlc_candles(self, limit: int = 100, interval: str = "5m", start: str = None, end: str = None) -> list:
        try:
            return get_ohlc_candles(self.api_key, self.symbol, self.dataset, limit, interval, start, end)
        except Exception as e:
            print(f"[Databento] get_ohlc_candles error: {e}")
            return []
