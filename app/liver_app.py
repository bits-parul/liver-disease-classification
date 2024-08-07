from flask import Flask, request, jsonify
import joblib
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the trained model
model = joblib.load('best_liver_disease_prediction_LR_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():

    try:
        scaler = StandardScaler()
        # Get the data from the POST request
        data = request.get_json(force=True)

        input_data = pd.DataFrame(data, index=[0])

        scaled_data = scaler.fit_transform(input_data)

        # Make prediction
        prediction = model.predict(scaled_data)

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
    app.run(debug=True, host='0.0.0.0', port=8000)