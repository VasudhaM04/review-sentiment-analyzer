import pickle

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from sklearn.model_selection import train_test_split

import sys
from pathlib import Path

# makes "from src import ..." work whether this file is run with
# `python -m src.xxx` OR run directly as `python src/xxx.py`
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src import config
from src.features import prepare_data


def split_data(X, y):
    # standard 80/20 split, stratify on y so the class balance stays consistent
    pass


def train_logistic_regression(X_train, y_train):
    # nothing fancy, just fit it, maybe bump max_iter so it actually converges
    pass


def train_random_forest(X_train, y_train):
    # around 200 trees is a reasonable starting point
    pass


def evaluate(model, X_test, y_test, name="model"):
    # print accuracy + classification_report so we can eyeball which model wins
    pass


def run():
    # prepare data, split it, train both models, evaluate both,
    # pick whichever has the higher accuracy, save it as the "best" model
    #
    # NOTE: call config.MODELS_DIR.mkdir(parents=True, exist_ok=True) BEFORE
    # you try to save anything into it, or the save will fail with
    # "No such file or directory" if models/ doesn't already exist
    #
    # also worth saving the test set + predictions somewhere - useful later if you
    # want to look at what the model actually got wrong
    pass


if __name__ == "__main__":
    run()
