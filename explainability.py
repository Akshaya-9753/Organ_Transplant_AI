def build_explainability(severity_text, risk_factors, contra_reasons):
    explanations = []

    explanations.append(f"Clinical severity assessment: {severity_text}")

    for factor in risk_factors:
        if factor == "infection":
            explanations.append("Active infection significantly increased short-term mortality risk")
        elif factor == "icu":
            explanations.append("ICU admission indicates physiological instability")
        elif factor == "high_pra":
            explanations.append("High PRA increases rejection probability")
        elif factor == "age":
            explanations.append("Advanced age moderately increases perioperative risk")

    for reason in contra_reasons:
        explanations.append(f"Safety concern identified: {reason}")

    return explanations
