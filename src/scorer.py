from src.rules import check_rules
from src.model import predict_scam_probability


def get_risk(text):
    reasons = check_rules(text)
    ml_probability = predict_scam_probability(text)

    score = int(ml_probability * 60 + len(reasons) * 15)
    score = min(score, 100)

    if score >= 60:
        level = "High"
    elif score >= 30:
        level = "Medium"
    else:
        level = "Low"

    return {
        "score": score,
        "level": level,
        "reasons": reasons,
        "ml_percent": round(ml_probability * 100),
    }