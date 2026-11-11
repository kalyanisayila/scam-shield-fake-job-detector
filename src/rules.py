import re

RULES = {
    "Asks for money (registration/training/security fee)": r"(registration|security|training|processing|kit|refundable)\s*(fee|fees|deposit|charges?|amount)|pay\s+(rs|₹|inr)",
    "Asks for Aadhaar/PAN/bank details/OTP": r"aadhaar|aadhar|pan card|bank (account )?details|\botp\b|\bcvv\b|atm pin",
    "Uses free email (Gmail/Yahoo etc.)": r"[\w.+-]+@(gmail|yahoo|hotmail|outlook|rediffmail)\.",
    "Urgent pressure": r"urgent|immediate joining|limited (seats|vacancies)|apply (now|today)",
    "Contact only on WhatsApp/Telegram": r"whatsapp|telegram",
    "Too-good-to-be-true offer": r"no interview|direct selection|guaranteed (job|placement)|daily payment|easy money|no experience (needed|required)|earn\s*(rs\.?|₹)?\s*\d[\d,]*\s*(per|/)\s*(day|week)",
    "Fake easy online work (typing/like videos)": r"typing job|like (youtube )?videos|copy paste job|data entry.*(home|online)",
}


def check_rules(text):
    text = text.lower()
    reasons = []
    for name, pattern in RULES.items():
        if re.search(pattern, text):
            reasons.append(name)
    return reasons