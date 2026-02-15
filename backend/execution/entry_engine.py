class EntryEngine:
    def execute(self, context):
        # All prior conditions must be met
        if not context.get("conditions_met"):
            return None
        entry_type = context.get("entry_type")
        if entry_type == "REJECTION":
            return "ENTER_NOW"
        if entry_type == "BREAK_RETEST":
            return "ENTER_ON_RETEST"
        if entry_type == "DISPLACEMENT":
            return "AGGRESSIVE_ENTRY"
        return None
