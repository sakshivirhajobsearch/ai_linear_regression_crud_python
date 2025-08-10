import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
import database

def train_model():
    data = database.get_all_data()
    if len(data) < 2:
        return None  # Need at least 2 points to train
    df = pd.DataFrame(data, columns=["id", "x_value", "y_value"])
    X = df[["x_value"]]
    y = df["y_value"]
    model = LinearRegression()
    model.fit(X, y)
    return model

def predict_value(x_input):
    model = train_model()
    if model is None:
        return "Not enough data to train the model."
    prediction = model.predict(np.array([[x_input]]))
    return prediction[0]
