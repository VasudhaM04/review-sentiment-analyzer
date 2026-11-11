import pickle
import sys
from pathlib import Path

import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

sys.path.append(str(Path(__file__).resolve().parent.parent))
from src import config  # noqa: E402
from src.preprocess import preprocess  # noqa: E402

app = FastAPI(title="Review Sentiment API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

state = {}


@app.on_event("startup")
def load_artifacts():
    # load both models once when the server starts, not on every request
    # classical model + its vectorizer, plus the rnn model + its tokenizer + label encoder
    # stash them all in the `state` dict above so predict() can use them
    pass


class ReviewRequest(BaseModel):
    review_text: str


class ModelResult(BaseModel):
    sentiment: str
    confidence: float


class PredictionResponse(BaseModel):
    classical: ModelResult
    rnn: ModelResult


@app.post("/predict", response_model=PredictionResponse)
def predict(request: ReviewRequest):
    # 1. clean the incoming text with preprocess()
    # 2. classical model: vectorizer.transform -> predict + predict_proba -> confidence is the max proba
    # 3. rnn model: tokenizer -> pad_sequences -> model.predict -> argmax -> label_encoder.inverse_transform
    # 4. return both wrapped in PredictionResponse
    pass


# mounted last so it doesn't shadow /predict
app.mount("/", StaticFiles(directory=Path(__file__).resolve().parent / "static", html=True), name="static")

# run with: uvicorn app.main:app --reload
