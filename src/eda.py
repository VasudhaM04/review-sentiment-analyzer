import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from scipy import stats

import sys
from pathlib import Path

# makes "from src import ..." work whether this file is run with
# `python -m src.xxx` OR run directly as `python src/xxx.py`
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src import config
from src.features import load_dataset, build_clean_corpus

sns.set_style("whitegrid")


def class_balance(df):
    # value_counts() on sentiment, print it, and plot it with sns.countplot
    # save the chart to config.MODELS_DIR / "eda_class_balance.png"
    # (call config.MODELS_DIR.mkdir(parents=True, exist_ok=True) first, or savefig will fail)
    pass


def review_length_distribution(df):
    # add a review_length column (word count of Review Text) to a COPY of df
    # plot a histogram, split/colored by sentiment (hue="sentiment")
    # save to config.MODELS_DIR / "eda_review_length.png" (mkdir first, same as above)
    pass


def most_common_words(df, sentiment="positive", top_n=15):
    # filter df to just this sentiment, join all clean_text together,
    # split into words, use collections.Counter to get the top_n most common
    pass


def hypothesis_test_review_length(df):
    # IMPORTANT: this function does NOT receive a review_length column for free —
    # add it yourself here, the same one line as in review_length_distribution:
    #   df["review_length"] = df["Review Text"].astype(str).apply(lambda x: len(x.split()))
    # this keeps the function self-contained, so it works no matter what order
    # the functions below get called in
    #
    # t-test: is there a real difference in review length between positive
    # and negative reviews, or could it just be noise?
    # scipy.stats.ttest_ind(positive_lengths, negative_lengths, equal_var=False)
    # print the means, t-statistic, p-value, and whether p < 0.05
    pass


def run():
    # load + clean the data, then call all four functions above in order
    pass


if __name__ == "__main__":
    run()
