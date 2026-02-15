def format_message(ctx, decision, reason):
    return {
        "headline": f"{decision} — {reason}",
        "details": [
            f"Price: {ctx['price']}",
            f"Market Phase: {ctx['qmo_phase']}",
            f"Liquidity: {ctx['liquidity']}",
            f"Iceberg: {ctx['iceberg']}",
            f"Gann: {ctx['gann_level']}",
            f"Astro: {ctx['astro']}",
            f"Cycle: {ctx['cycle']}"
        ]
    }
