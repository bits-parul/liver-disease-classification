import unittest
from model_util import load_model, predict
import pandas as pd

class TestModel(unittest.TestCase):
    def test_model_loading(self):
        model = load_model('models/liver_disease_randomforest_model.joblib')
        self.assertIsNotNone(model)

    def test_model_prediction(self):
        model = load_model('models/liver_disease_randomforest_model.joblib')
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
        predictions = predict(model, new_data)
        self.assertIsNotNone(predictions)
        self.assertEqual(len(predictions), 1)
        self.assertIn(predictions[0], [0, 1])

if __name__ == '__main__':
    unittest.main()
