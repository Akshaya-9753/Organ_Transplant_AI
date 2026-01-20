def calculate_risk_score(age, infection, icu, sepsis, hla, pra, prev_tx):
    score = 0
    factors = []

    if age >= 65:
        score += 1
        factors.append("age")

    if infection == "Yes":
        score += 2
        factors.append("infection")

    if icu == "Yes":
        score += 2
        factors.append("icu")

    if sepsis == "High":
        score += 3
        factors.append("sepsis")

    if pra > 50:
        score += 1
        factors.append("high_pra")

    if prev_tx == "Yes":
        score += 1
        factors.append("previous_transplant")

    return score, factors


def risk_level(score: int) -> str:
    if score >= 6:
        return "High Risk"
    elif score >= 3:
        return "Moderate Risk"
    else:
        return "Low Risk"
