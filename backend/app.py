from fastapi import FastAPI
from pydantic import BaseModel
from backend.model import predict, train_model, load_data
from backend.feedback_loop import save_feedback
import pandas as pd

app = FastAPI()

class PredictInput(BaseModel):
    texts: list

class FeedbackInput(BaseModel):
    text: str
    label: int

@app.post("/predict")
def predict_endpoint(data: PredictInput):
    preds, probs = predict(data.texts)
    return {"predictions": preds.tolist(), "probabilities": probs.tolist()}

@app.post("/feedback")
def feedback_endpoint(data: FeedbackInput):
    save_feedback(data.text, data.label)
    return {"message": "Feedback received."}

@app.post("/retrain")
def retrain_endpoint():
    original = load_data("data/comments.csv")
    try:
        feedback = pd.read_csv("data/user_feedback.csv")
        combined = pd.concat([original, feedback], ignore_index=True)
    except FileNotFoundError:
        combined = original
    train_model(combined)
    return {"message": "Model retrained successfully."}
