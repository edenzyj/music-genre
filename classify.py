import numpy as np
import pandas as pd
import base64
import sklearn
import sklearn.ensemble

classname = ""
sentence = {"blues" : "A man is dancing street dance."}
genre = {5 : "blues"}

def music_genre(data=None):
    train_set = pd.read_csv("input/train.csv")
    train_data = train_set.fillna(0)
    #print(train_data.head(5))

    df_train = train_data
    genre = df_train.pop("Class")
    del df_train["Artist Name"]
    del df_train["Track Name"]

    model = sklearn.ensemble.RandomForestClassifier()
    model.fit(df_train, genre)

    test_set = pd.read_csv("input/simple_test.csv")
    test_data = test_set.fillna(0)
    test_data.pop("Class")
    del test_data["Artist Name"]
    del test_data["Track Name"]

    pred = model.predict(test_data)
    pred = pred.ravel()
    #print(pred)

    return genre.get(pred[0])


def generate_sentence():
    return sentence.get(classname)

music_genre()
