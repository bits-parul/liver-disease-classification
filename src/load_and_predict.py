import pandas as pd
from model_util import load_model, predict


if __name__ == "__main__":
    model = load_model("models/liver_disease_randomforest_model.joblib")
    
    # Example new data for prediction
    new_data = pd.DataFrame({
        'Age': [45],
        'Total_Bilirubin': [1.0],
        'Direct_Bilirubin': [0.3],
        'Alkaline_Phosphotase': [200],
        'Alamine_Aminotransferase': [50],
        'Aspartate_Aminotransferase': [45],
        'Total_Protiens': [6.5],
        'Albumin': [3.5],
        'Albumin_and_Globulin_Ratio': [1.0]
    })

    # Make predictions
    predictions = predict(model, new_data)
    decoded_predictions = ["Yes" if pred==1 else "No" for pred in predictions]
    print("Predictions:", decoded_predictions)
    
