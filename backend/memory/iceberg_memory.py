

import json
import os
from datetime import datetime

class IcebergMemoryEngine:
    FILE = "iceberg_memory.json"

    def __init__(self):
        self.zones = []
        self.load()

    def save_zone(self, zone):
        self.zones.append(zone)
        self.save()

    def save(self):
        with open(self.FILE, "w") as f:
            json.dump(self.zones, f, indent=2)

    def load(self):
        if os.path.exists(self.FILE):
            with open(self.FILE, "r") as f:
                self.zones = json.load(f)
        else:
            self.zones = []

    def record_iceberg(self, instrument, price_low, price_high, session, side, volume_strength, delta_bias, reaction_result):
        zone = {
            "instrument": instrument,
            "price_low": price_low,
            "price_high": price_high,
            "session": session,
            "date": datetime.utcnow().strftime("%Y-%m-%d"),
            "side": side,
            "volume_strength": volume_strength,
            "delta_bias": delta_bias,
            "reaction_result": reaction_result,
            "times_retested": 0
        }
        self.save_zone(zone)

    def retest_zone(self, price, tolerance=0.5):
        for zone in self.zones:
            if zone["price_low"] - tolerance <= price <= zone["price_high"] + tolerance:
                zone["times_retested"] += 1
        self.save()

    def get_active_zones(self, session=None):
        today = datetime.utcnow().strftime("%Y-%m-%d")
        return [z for z in self.zones if (session is None or z["session"] == session) and z["date"] <= today]

    def get_zones_for_chart(self):
        # For chart overlays: return all zones with price, session, and side
        return [
            {
                "price_low": z["price_low"],
                "price_high": z["price_high"],
                "session": z["session"],
                "side": z["side"],
                "date": z["date"],
                "times_retested": z["times_retested"]
            }
            for z in self.zones
        ]

    def clear_old_zones(self, days=10):
        today = datetime.utcnow().strftime("%Y-%m-%d")
        self.zones = [z for z in self.zones if (datetime.strptime(today, "%Y-%m-%d") - datetime.strptime(z["date"], "%Y-%m-%d")).days <= days]
        self.save()
