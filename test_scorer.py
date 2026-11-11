from src.scorer import get_risk

scam = "Urgent hiring! Pay Rs 2000 registration fee. Contact on WhatsApp. Email: hr.company@gmail.com"
real = "We are hiring a Python developer. Requirements: 2 years experience, knowledge of Django and SQL. Apply on our careers page. Interview process: 2 technical rounds and 1 HR round."

print("SCAM MESSAGE:", get_risk(scam))
print("REAL MESSAGE:", get_risk(real))