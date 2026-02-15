class TradeManager:
    def manage(self, trade, market_state):
        actions = []
        # Stage 1: Risk Removal
        if trade.r_multiple >= 1:
            actions.append("TAKE_PARTIAL_1")
            trade.stop = trade.entry  # Move stop to breakeven
        # Stage 2: Structure Trail
        if getattr(market_state, "structure_break", False):
            actions.append("TAKE_PARTIAL_2")
            trade.stop = getattr(market_state, "last_swing", trade.stop)
        # Stage 3: Context Exit
        if getattr(market_state, "exit_signal", False):
            actions.append("EXIT_ALL")
        # Overrides
        if getattr(market_state, "iceberg_against", False):
            actions.append("EXIT_ALL")
        if getattr(market_state, "htf_bias_flip", False):
            actions.append("EXIT_ALL")
        if getattr(market_state, "news_event", False):
            actions.append("EXIT_ALL")
        if getattr(market_state, "volatility_spike", False):
            actions.append("EXIT_ALL")
        return actions
