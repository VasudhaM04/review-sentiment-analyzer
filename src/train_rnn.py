import pickle

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.layers import Dense, Embedding, SimpleRNN
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

import sys
from pathlib import Path

# makes "from src import ..." work whether this file is run with
# `python -m src.xxx` OR run directly as `python src/xxx.py`
sys.path.append(str(Path(__file__).resolve().parent.parent))

from src import config
from src.features import build_clean_corpus, load_dataset


def build_sequences(texts):
    # unlike tfidf, the rnn needs integer sequences of a fixed length
    # tokenizer -> fit -> texts_to_sequences -> pad_sequences (use config.RNN_VOCAB_SIZE / RNN_MAX_LEN)
    pass


def build_rnn(vocab_size, max_len, num_classes, embedding_dim=64, rnn_units=32):
    # keep it small - embedding around 64 dims, rnn units around 32 is plenty for this dataset size
    # Embedding -> SimpleRNN -> Dense(softmax), compile with adam + sparse_categorical_crossentropy
    pass


def run():
    # load + clean data, build sequences, encode labels with LabelEncoder,
    # split train/test, build the model, fit it (10 epochs, batch_size 16 is a fine start),
    # check val accuracy, then save the model + tokenizer + label encoder to models/
    #
    # NOTE: call config.MODELS_DIR.mkdir(parents=True, exist_ok=True) BEFORE
    # saving any of the three files, or the save will fail if models/ doesn't
    # already exist
    pass


if __name__ == "__main__":
    run()
