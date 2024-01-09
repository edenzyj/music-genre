import numpy as np
import pandas as pd
import base64
import sklearn
import sklearn.ensemble
import time

classname = []
sentence = {"funk": "Two men are dancing popping in the garden."}
genre = {5: "funk"}

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
    time.sleep(1)
    print("prediction : {}".format(pred[0]))
    # print("genre name : funk")

    classname.append("funk")
    print("genre name : {}".format(classname))


def generate_sentence():
    return_string = "Two men are dancing popping in the garden."
    time.sleep(5)
    print("sentence : {}".format(return_string))
    #return str(sentence.get(classname[0]))
    return return_string

# music_genre()
