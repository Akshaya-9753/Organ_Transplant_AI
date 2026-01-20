def contraindication_status(
    infection, cancer_stage, cardiac_event,
    diabetes, hypertension, adherence
):
    reasons = []

    if infection == "Yes":
        reasons.append("Active infection")

    if cancer_stage in ["Stage 3", "Stage 4"]:
        reasons.append("Advanced malignancy")

    if cardiac_event == "Yes":
        reasons.append("Recent major cardiac or stroke event")

    if reasons:
        return "Contraindicated", reasons

    conditional = []
    if diabetes:
        conditional.append("Uncontrolled diabetes")
    if hypertension:
        conditional.append("Uncontrolled hypertension")
    if adherence:
        conditional.append("Psychological / adherence risk")

    if conditional:
        return "Conditional", conditional

    return "Clear", []
