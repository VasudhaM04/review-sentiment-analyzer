"""
project-wide paths and constants
everything else imports from here so we're not hardcoding paths all over the place
"""

from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = ROOT_DIR / "data" / "reviews.csv"
MODELS_DIR = ROOT_DIR / "models"

TFIDF_VECTORIZER_PATH = MODELS_DIR / "tfidf_vectorizer.pkl"
BEST_ML_MODEL_PATH = MODELS_DIR / "best_ml_model.pkl"

RNN_MODEL_PATH = MODELS_DIR / "rnn_model.keras"
RNN_TOKENIZER_PATH = MODELS_DIR / "rnn_tokenizer.pkl"
LABEL_ENCODER_PATH = MODELS_DIR / "label_encoder.pkl"

# rnn settings, reused by train_rnn.py and app/main.py so they always match
RNN_VOCAB_SIZE = 5000
RNN_MAX_LEN = 50

RANDOM_STATE = 42
