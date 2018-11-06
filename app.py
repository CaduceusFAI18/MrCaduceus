import pandas as pd 
import numpy as np 

import tensorflow as tf 
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Conv2D, MaxPooling2D, Dropout, Flatten, BatchNormalization
from keras import backend as K
from sklearn.metrics import f1_score

def create_model(input_shape, output_shape):
    model = Sequential()
    model.add(Dense(1280, activation="relu", input_dim=input_shape[1]))
    model.add(Dense(2560, activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(2560, activation="relu"))
    model.add(Dense(1280, activation="relu"))
    model.add(BatchNormalization())
    model.add(Dropout(0.2))
    model.add(Dense(512, activation="relu"))
    model.add(Dense(128, activation="relu"))
    model.add(Dense(output_shape[1], activation="sigmoid"))
     
    return model

def train(X, y):
    X = X.drop("SEQN", axis='columns')
    y = y.drop("SEQN", axis='columns')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = create_model(X.shape, y.shape)
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    X_train = np.array(X_train)
    model.fit(x=X_train, y=np.array(y_train), batch_size=128, epochs=30, validation_split=0.2)
    predict = model.predict(X_test)
    predict[predict>=0.5] = 1
    predict[predict<0.5] = 0
    unique, counts = np.unique(predict, return_counts=True)
    print(dict(zip(unique, counts)))
    points = model.evaluate(X_test, y_test)
    print("loss: ", points[0], "accuracy: ", points[1])

if __name__ == "__main__":

  X = pd.read_pickle("./data/preprocessed/merged/mergedX.pkl")
  y = pd.read_csv("./data/preprocessed/merged/Y.csv", index_col=0)
  for column in X.select_dtypes(include=['O']):
    X[column] = [ ord(x) - 64 if len(str(x)) is 1 else x for x in X[column]]
  
  X = X.sort_values("SEQN")
  y = y[y["SEQN"].isin(X["SEQN"])].sort_values("SEQN")
  X = X.drop(811) # X[~X.applymap(np.isreal).all(1)]
  y = y.drop(811)
  train(X, y)