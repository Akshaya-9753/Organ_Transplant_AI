def interpret_severity(organ: str, severity: float) -> str:
    if organ == "Kidney":
        if severity < 15:
            return "Severely reduced GFR (<15): End-stage renal disease"
        elif severity < 30:
            return "Moderately reduced GFR (15–29)"
        else:
            return "Mild renal impairment"

    if organ == "Liver":
        if severity >= 30:
            return "High MELD score (>30): Critical liver failure"
        elif severity >= 20:
            return "Moderate MELD score (20–29)"
        else:
            return "Lower MELD score (<20)"

    if organ == "Heart":
        if severity < 25:
            return "Severely reduced ejection fraction (<25%)"
        elif severity < 40:
            return "Moderately reduced ejection fraction (25–40%)"
        else:
            return "Preserved ejection fraction (>40%)"

    if organ == "Lung":
        if severity < 30:
            return "Severely reduced lung function"
        elif severity < 50:
            return "Moderately reduced lung function"
        else:
            return "Mild lung impairment"

    return "Severity interpretation unavailable"
