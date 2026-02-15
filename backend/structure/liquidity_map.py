class LiquidityMap:
    def detect(self, highs, lows):
        pools = []
        if highs[-1] == highs[-2]:
            pools.append({"type": "EQH", "price": highs[-1]})
        if lows[-1] == lows[-2]:
            pools.append({"type": "EQL", "price": lows[-1]})
        # Add session high/low, range high/low, etc. as needed
        return pools
