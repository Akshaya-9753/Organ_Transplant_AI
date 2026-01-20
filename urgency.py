def urgency_level(organ: str, severity: float) -> str:
    if organ == "Kidney":
        return "High Urgency" if severity < 15 else "Moderate Urgency"

    if organ == "Liver":
        return "High Urgency" if severity >= 25 else "Moderate Urgency"

    if organ == "Heart":
        return "High Urgency" if severity < 30 else "Moderate Urgency"

    if organ == "Lung":
        return "High Urgency" if severity < 35 else "Moderate Urgency"

    return "Standard Urgency"
