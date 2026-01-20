# backend/engines/iceberg_zone_engine.py

class IcebergZoneEngine:
    def __init__(self):
        self.zones = []

    def create_zone(self, xau_price, direction, strength, session):
        zone_height = {
            "A": 3.0,
            "B": 2.0,
            "C": 1.5
        }.get(strength, 1.5)

        zone = {
            "top": round(xau_price + zone_height, 2),
            "bottom": round(xau_price - zone_height, 2),
            "direction": direction,
            "strength": strength,
            "session": session,
            "active": True
        }

        self.zones.append(zone)
        return zone

    def get_active_zones(self):
        return [z for z in self.zones if z["active"]]
