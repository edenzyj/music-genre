import numpy as np
import pandas as pd
import base64
import sklearn
import sklearn.ensemble

classname = []
sentence = {"funk" : "A man is dancing street dance."}
genre = {5 : "funk"}

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
    print("prediction : {}".format(pred[0]))
    print("genre name : {}".format(genre[pred[0]]))

    classname.append(genre[pred[0]])
    print(classname[0])


def generate_sentence():
    print("sentence : " + str(sentence.get(classname[0])))
    #return str(sentence.get(classname[0]))
    return_string = "A man is dancing popping."
    return return_string

music_genre()
