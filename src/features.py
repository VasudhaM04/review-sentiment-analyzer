import pickle

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

import sys
from pathlib import Path

# makes "from src import ..." work whether this file is run with
# `python -m src.xxx` OR run directly as `python src/xxx.py`
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src import config
from src.preprocess import preprocess


def rating_to_sentiment(rating: int) -> str:
    # dataset doesn't have a sentiment column, so we make one from Rating
    # 1-2 stars -> negative, 3 -> neutral, 4-5 -> positive
    pass


def load_dataset() -> pd.DataFrame:
    # read the csv, drop rows with no review text, add the sentiment column using the function above
    pass


def build_clean_corpus(df: pd.DataFrame) -> pd.DataFrame:
    # apply preprocess() to Review Text, store it in a new clean_text column
    pass


def build_tfidf_features(corpus, max_features: int = 3000, ngram_range: tuple = (1, 2)):
    # tfidf on the cleaned text, top ~3000 words, unigrams + bigrams so
    # word pairs like "not good" aren't lost as separate meaningless words
    pass


def prepare_data():
    # tie it all together: load -> clean -> vectorize
    # also pickle the fitted vectorizer to models/ so train_classical.py and the api can reuse it
    # return df, X, y, vectorizer
    pass


if __name__ == "__main__":
    df, X, y, vectorizer = prepare_data()
    print("rows:", len(df))
    print("feature matrix shape:", X.shape)
    print(y.value_counts())
