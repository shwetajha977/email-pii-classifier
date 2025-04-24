from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import joblib

def train_model():
    df = pd.read_csv("combined_emails_with_natural_pii.csv")
    from utils import mask_pii
    df["masked_email"] = df["email"].apply(lambda x: mask_pii(x)[0])

    X = df["masked_email"]
    y = df["type"]

    vectorizer = TfidfVectorizer()
    X_vec = vectorizer.fit_transform(X)

    model = MultinomialNB()
    model.fit(X_vec, y)

    joblib.dump(model, "email_classifier_model.pkl")
    joblib.dump(vectorizer, "vectorizer.pkl")
    print("✅ Model and vectorizer saved.")

def classify_email(email):
    import joblib
    vectorizer = joblib.load("vectorizer.pkl")
    model = joblib.load("email_classifier_model.pkl")

    X = vectorizer.transform([email])
    return model.predict(X)[0]
