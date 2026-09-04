import numpy as np
import tensorflow as tf
import pandas as pd
import joblib

from schema.schemas import LonaApprovalModel

class ModelServices:

    def Loan_Approval(self, data: LonaApprovalModel):
        model = tf.keras.models.load_model("D:\\pycharm\\fastapi\\app\ml_models\\loan_prediction\\loan_prediction_ann.keras")
        scaler = joblib.load("D:\\pycharm\\fastapi\\app\\ml_models\\loan_prediction\\loan_prediction_scaler.pkl")

        education = 0
        self_employed = 0

        if data.education == "Graduate":
            education = 1

        if data.self_employed == "Yes":
            self_employed = 1

        input_data = pd.DataFrame(
            [
                {
                    "no_of_dependents": data.no_of_dependents,
                    "education": education,
                    "self_employed": self_employed,
                    "income_annum": data.income_annum,
                    "loan_amount": data.loan_amount,
                    "loan_term": data.loan_term,
                    "cibil_score": data.cibil_score,
                    "residential_assets_value": data.residential_assets_value,
                    "commercial_assets_value": data.commercial_assets_value,
                    "luxury_assets_value": data.luxury_assets_value,
                    "bank_asset_value": data.bank_asset_value
                }
            ]
        )

        input_scaled = scaler.transform(input_data)
        prob = float(model.predict(input_scaled)[0][0])  # sigmoid output, 0-1
        prediction = "Approved" if prob > 0.5 else "Rejected"

        return {"prediction": prediction, "probability": round(prob, 4)}