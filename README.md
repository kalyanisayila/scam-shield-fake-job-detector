# ScamShield: Fake Job Detector

![demo](screenshots/demo.png)

Paste a job message or offer letter and ScamShield tells you if it looks like a scam.

## How it works
- Rule checks: finds red flags like registration fee, free Gmail, Aadhaar/OTP request, WhatsApp-only contact.
- ML model: TF-IDF + Logistic Regression trained on 17,880 job posts (98% accuracy, 90% recall on fake jobs).
- Final score: Low / Medium / High risk with reasons.

## Run it
pip install -r requirements.txt
streamlit run app.py

## Dataset
Real / Fake Job Posting Prediction (Kaggle). Put fake_job_postings.csv in the data folder, then run python src/model.py to train.