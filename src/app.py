from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load('models/liver_disease_randomforest_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():

    try:
        # Get the data from the POST request
        data = request.get_json(force=True)

        # Extract features from data
        features = [
            data['Age'],
            data['Total_Bilirubin'],
            data['Direct_Bilirubin'],
            data['Total_Protiens'],
            data['Albumin'],
            data['Albumin_and_Globulin_Ratio'],
            data['Alkaline_Phosphotase_normalized'],
            data['Alamine_Aminotransferase_normalized'],
            data['Aspartate_Aminotransferase_normalized']
        ]

        # Convert features to a numpy array
        features = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(features)

        # Decode the prediction
        decoded_prediction = 'Yes' if prediction[0] == 1 else 'No'

        # Return the prediction as a JSON response
        return jsonify({
            'prediction': decoded_prediction
        })

    except Exception as e:
        return jsonify({
            'error': str(e)
        })

@app.route('/')

def home():

    return 'Welcome to the Liver disease classification API!'


if __name__ == '__main__':

    app.run(debug=True, host='0.0.0.0', port=5000)
