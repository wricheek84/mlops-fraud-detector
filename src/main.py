import joblib
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# 1. Create a FastAPI app instance
app = FastAPI()

# 2. Load the trained model and scaler
# These are loaded once when the application starts.
model = joblib.load('../models/xgboost_model.joblib')
scaler = joblib.load('../models/scaler.joblib')

# 3. Define the input data model using Pydantic
# This ensures that the data we receive has the correct format and types.
class Transaction(BaseModel):
    Time: float
    V1: float
    V2: float
    V3: float
    V4: float
    V5: float
    V6: float
    V7: float
    V8: float
    V9: float
    V10: float
    V11: float
    V12: float
    V13: float
    V14: float
    V15: float
    V16: float
    V17: float
    V18: float
    V19: float
    V20: float
    V21: float
    V22: float
    V23: float
    V24: float
    V25: float
    V26: float
    V27: float
    V28: float
    Amount: float

# 4. Create the prediction endpoint
@app.post("/predict")
def predict(data: Transaction):
    # Convert the input data into a pandas DataFrame
    input_df = pd.DataFrame([data.dict()])

    # Scale the input data using the loaded scaler
    scaled_df = scaler.transform(input_df)

    # Make a prediction using the loaded model
    prediction = model.predict(scaled_df)

    # Get the prediction result (0 or 1)
    result = int(prediction[0])

    # Return the result
    if result == 1:
        return {"prediction": "Fraudulent Transaction"}
    else:
        return {"prediction": "Legitimate Transaction"}