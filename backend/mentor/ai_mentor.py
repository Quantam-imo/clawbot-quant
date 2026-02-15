class AIMentor:
    def build_message(self, context):
        lines = []
        lines.append(f"SESSION: {context['session']} ({context['time']})")
        lines.append("")
        lines.append("Market Context:")
        lines.append(context["structure"])
        lines.append("")
        lines.append("Liquidity:")
        lines.append(context["liquidity"])
        lines.append("")
        lines.append("Order Flow:")
        lines.append(context["iceberg"])
        if context.get("timing"):
            lines.append("")
            lines.append("Timing:")
            lines.append(context["timing"])
        lines.append("")
        lines.append("Risk:")
        lines.append(context["risk"])
        lines.append("")
        lines.append("Guidance:")
        lines.append(context["guidance"])
        return "\n".join(lines)
