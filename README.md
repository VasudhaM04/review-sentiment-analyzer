# Review Sentiment Analyzer

Build a sentiment analysis tool that reads product reviews and predicts
whether they're positive, negative, or neutral — using two different
approaches (classical ML and an RNN) and serving both through a simple
web app.

## Project structure

```
review-sentiment-analyzer/
├── data/
│   └── reviews.csv          # sample data — replace with the real dataset (see below)
├── models/                  # your trained models will get saved here
├── src/
│   ├── config.py            # shared paths/constants — already done, no changes needed
│   ├── eda.py                # class balance, review length, common words, t-test — you fill this in
│   ├── preprocess.py        # text cleaning pipeline — you fill this in
│   ├── features.py          # sentiment labels + tfidf features — you fill this in
│   ├── train_classical.py   # logistic regression + random forest — you fill this in
│   ├── train_rnn.py         # keras rnn — you fill this in
│   └── predict.py            # cli sanity-check, no api needed — you fill this in
├── app/
│   ├── main.py               # fastapi — you fill this in
│   └── static/
│       └── index.html        # frontend — already built, don't need to touch this
├── run_pipeline.py           # runs everything in one command once you're done
├── requirements.txt
└── README.md
```

## Dataset

We're using the **Women's E-Commerce Clothing Reviews** dataset from Kaggle
(`nicapotato/womens-ecommerce-clothing-reviews`). ~23,000 real customer
reviews, single CSV file.

1. Download it from Kaggle
2. Save it as `data/reviews.csv`, keep the original column names as-is

The `reviews.csv` already in `data/` right now is a small placeholder so
you can test your code as you go — swap in the real file when you have it.

**Important:** there's no ready-made sentiment column in this dataset.
You'll build one yourself from `Rating` (1-5 stars) — that's the first
thing you write in `features.py`.

## Setup

```bash
pip install -r requirements.txt
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

## What you're building

Work through the files in this order:

1. **`src/preprocess.py`** — clean up raw review text (lowercase, remove
   punctuation, remove stopwords, stem) so it's ready to feed into a model
2. **`src/features.py`** — turn `Rating` into a sentiment label, and turn
   cleaned text into TF-IDF features
3. **`src/eda.py`** — look at the data before modeling it: class balance,
   review length, most common words per sentiment, and a quick hypothesis
   test comparing review length between positive and negative reviews
4. **`src/train_classical.py`** — train Logistic Regression and Random
   Forest, compare them, save the better one
5. **`src/train_rnn.py`** — train a small RNN on the same reviews (different
   feature representation — sequences instead of TF-IDF)
6. **`src/predict.py`** — a quick terminal script to test both models
   without needing the API running
7. **`app/main.py`** — wire both trained models into a `/predict` endpoint
   that the frontend calls

Once everything's filled in:

```bash
python run_pipeline.py
```

This trains both models and saves everything to `models/`. Then:

```bash
uvicorn app.main:app --reload
```

Open **http://localhost:8000** — type a review, hit analyze, and you should
see both models' predictions side by side with a confidence gauge for each.

## A few notes

- N-grams aren't a separate step — look at the `ngram_range` parameter
  on the TF-IDF vectorizer in `features.py`, that's where it lives.
- The comments in each function tell you what to build and give you
  reasonable starting numbers (like how many trees, how many epochs) —
  you don't need to guess those, just the logic.
- `config.py` and `app/static/index.html` are already done — you don't
  need to touch either of them.
