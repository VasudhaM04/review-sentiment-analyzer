import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

STOPWORDS = set(stopwords.words("english"))
STEMMER = PorterStemmer()


def clean_text(text: str) -> str:
    # lowercase everything, strip out punctuation/numbers, collapse extra spaces
    pass


def tokenize(text: str) -> list[str]:
    # just split into word tokens, nltk has a function for this
    pass


def remove_stopwords(tokens: list[str]) -> list[str]:
    # drop anything in STOPWORDS
    pass


def stem_tokens(tokens: list[str]) -> list[str]:
    # run each token through STEMMER
    pass


def preprocess(text: str) -> str:
    # chain everything above together and rejoin into one string
    # this is what features.py calls to build the tfidf corpus
    pass


if __name__ == "__main__":
    sample = "This dress is AMAZING!! Fits perfectly, I loved it."
    print("Original :", sample)
    print("Processed:", preprocess(sample))
