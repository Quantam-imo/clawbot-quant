def decide(ctx):
    # 1. Permission
    if ctx["qmo_phase"] not in ["DISTRIBUTION", "ACCUMULATION"]:
        return "WAIT", "Market not in execution phase"
    # 2. Liquidity
    if not ctx["liquidity"]:
        return "WAIT", "No liquidity event detected"
    # 3. Iceberg
    iceberg = ctx["iceberg"]
    if iceberg:
        if iceberg["side"] == "SELL" and ctx["price"] > iceberg["price"]:
            bias = "SELL"
        elif iceberg["side"] == "BUY" and ctx["price"] < iceberg["price"]:
            bias = "BUY"
        else:
            return "WAIT", "Price not aligned with iceberg"
    else:
        return "WAIT", "No institutional absorption"
    # 4. Timing
    if not (ctx["gann_level"] or ctx["astro"] or ctx["cycle"]):
        return "WAIT", "No timing confirmation"
    # 5. News
    if ctx["news_risk"] == "HIGH":
        return "WAIT", "High-impact news nearby"
    return "EXECUTE", bias
