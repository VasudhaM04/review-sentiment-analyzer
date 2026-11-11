from src import eda, train_classical, train_rnn


def main():
    print("=" * 60)
    print("running eda")
    print("=" * 60)
    eda.run()

    print("\n" + "=" * 60)
    print("training classical models (logistic regression + random forest)")
    print("=" * 60)
    train_classical.run()

    print("\n" + "=" * 60)
    print("training rnn")
    print("=" * 60)
    train_rnn.run()

    print("\nall models trained and saved to models/")
    print("start the api with: uvicorn app.main:app --reload")


if __name__ == "__main__":
    main()
