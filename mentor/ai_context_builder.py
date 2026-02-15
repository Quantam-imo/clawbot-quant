def build_context(market):
    return {
        "price": market["price"],
        "qmo_phase": market["qmo_phase"],
        "structure": market["structure"],
        "liquidity": market["liquidity"],
        "iceberg": market["iceberg"],
        "gann_level": market["gann"],
        "astro": market["astro"],
        "cycle": market["cycle"],
        "news_risk": market["news"]
    }
