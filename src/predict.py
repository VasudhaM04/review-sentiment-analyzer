import pickle
import sys

import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

from pathlib import Path

# makes "from src import ..." work whether this file is run with
# `python -m src.xxx` OR run directly as `python src/xxx.py`
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src import config
from src.preprocess import preprocess


def load_artifacts():
    # load both saved models the same way app/main.py does -
    # classical model + vectorizer, rnn model + tokenizer + label encoder
    # return all five
    pass


def predict(review_text, classical_model, vectorizer, rnn_model, rnn_tokenizer, label_encoder):
    # same logic as the /predict route in app/main.py, just returned as a dict
    # instead of a PredictionResponse - clean text, run through both models
    pass


def main():
    # grab the review text from the command line - join everything after the
    # filename into one string with " ".join(sys.argv[1:]) so it still works
    # even if someone forgets to wrap it in quotes
    #
    # if nothing was typed after the filename at all (len(sys.argv) < 2),
    # fall back to input("Enter review text: ") instead of crashing - that
    # makes this friendlier to run live in front of a class
    #
    # then: load the artifacts, run predict(), print both results nicely
    # usage: python -m src.predict this product is amazing
    pass


if __name__ == "__main__":
    main()
