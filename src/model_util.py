# Importing the libraries.

import joblib
import pandas as pd


def load_model(model_path):
    return joblib.load(model_path)
    
    
def predict(model, data):
    return model.predict(data)