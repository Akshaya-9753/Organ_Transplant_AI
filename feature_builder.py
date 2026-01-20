# ml/feature_builder.py

def build_features(
    age, organ, severity, icu, infection, sepsis,
    hla, pra, prev_tx, cancer
):
    """
    Returns features as a DICTIONARY (clean & explainable)
    """

    organ_map = {
        "Kidney": 0,
        "Liver": 1,
        "Heart": 2,
        "Lung": 3
    }

    sepsis_map = {
        "Low": 0,
        "Medium": 1,
        "High": 2
    }

    features = {
        "age": age,
        "organ": organ_map[organ],
        "severity": severity,
        "icu": 1 if icu == "Yes" else 0,
        "infection": 1 if infection == "Yes" else 0,
        "sepsis": sepsis_map[sepsis],
        "hla": hla,
        "pra": pra,
        "prev_tx": 1 if prev_tx == "Yes" else 0,
        "cancer": 0 if cancer == "None" else 1
    }

    return features
