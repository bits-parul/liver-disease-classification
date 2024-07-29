import pandas as pd
from model_util import load_model, predict


if __name__ == "__main__":
    model = load_model("models/liver_disease_randomforest_model.joblib")
    
    # Example new data for prediction
    new_data = pd.DataFrame({
        'Age': [74.000000],
        'Total_Bilirubin': [0.900000],
        'Direct_Bilirubin': [0.300000],
        'Total_Protiens': [7.900000],
        'Albumin': [4.000000],
        'Albumin_and_Globulin_Ratio': [1.000000],
        'Alkaline_Phosphotase_normalized': [3.490333],
        'Alamine_Aminotransferase_normalized': [1.421247],
        'Aspartate_Aminotransferase_normalized': [1.574394]
    })

    # Make predictions
    predictions = predict(model, new_data)
    decoded_predictions = [
        "yes" if pred == 1 else "no" for pred in predictions
        ]
    print("Predictions:", decoded_predictions)
    
