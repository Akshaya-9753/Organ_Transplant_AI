def eligibility(contra_status, risk_level):
    if contra_status == "Contraindicated":
        return "Not Eligible"
    if risk_level == "High Risk":
        return "Conditionally Eligible"
    return "Eligible"
