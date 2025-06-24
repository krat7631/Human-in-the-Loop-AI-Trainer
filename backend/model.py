import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import joblib
import os

MODEL_PATH = "model.joblib"

def load_data(csv_file="data/comments.csv"):
    df = pd.read_csv(csv_file)
    df = df.dropna(subset=["comment", "label"])
    return df

def train_model(df):
    X = df["comment"]
    y = df["label"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    pipeline = Pipeline([
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression(max_iter=1000))
    ])
    pipeline.fit(X_train, y_train)
    joblib.dump(pipeline, MODEL_PATH)
    return pipeline

def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    else:
        df = load_data()
        return train_model(df)

def predict(texts):
    model = load_model()
    return model.predict(texts), model.predict_proba(texts)
