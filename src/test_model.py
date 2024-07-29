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
        predictions = predict(model, new_data)
        self.assertIsNotNone(predictions)
        self.assertEqual(len(predictions), 1)
        self.assertIn(predictions[0], [0, 1])

if __name__ == '__main__':
    unittest.main()
