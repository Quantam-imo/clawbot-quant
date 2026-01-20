# backend/mapping/gc_xau_mapper.py

class GCtoXAUMapper:
    def __init__(self):
        self.offset = None

    def update_offset(self, gc_price, xau_price):
        """
        Call every few seconds
        """
        self.offset = round(xau_price - gc_price, 2)
        return self.offset

    def map_price(self, gc_price):
        """
        Convert GC institutional level to XAUUSD
        """
        if self.offset is None:
            raise ValueError("GC-XAU offset not initialized")

        return round(gc_price + self.offset, 2)
