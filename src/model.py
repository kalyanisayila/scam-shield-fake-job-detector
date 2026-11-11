import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.pipeline import make_pipeline

MODEL_PATH = "model.pkl"
TEXT_COLUMNS = ["title", "company_profile", "description", "requirements", "benefits"]


def load_data():
    df = pd.read_csv("data/fake_job_postings.csv")
    df[TEXT_COLUMNS] = df[TEXT_COLUMNS].fillna("")
    df["text"] = df[TEXT_COLUMNS].agg(" ".join, axis=1)
    return df["text"], df["fraudulent"]


def train():
    X, y = load_data()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    model = make_pipeline(
        TfidfVectorizer(stop_words="english", max_features=20000),
        LogisticRegression(max_iter=1000, class_weight="balanced"),
    )
    model.fit(X_train, y_train)
    print(classification_report(y_test, model.predict(X_test)))
    joblib.dump(model, MODEL_PATH)
    print("Model saved!")


def predict_scam_probability(text):
    model = joblib.load(MODEL_PATH)
    return float(model.predict_proba([text])[0][1])


if __name__ == "__main__":
    train()