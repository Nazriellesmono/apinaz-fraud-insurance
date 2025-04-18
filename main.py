# app/main.py

from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel, Field
import joblib
import pandas as pd
import uvicorn

app = FastAPI(
    title="Insurance Fraud Detection API",
    version="1.0.0",
    description="API untuk mendeteksi potensi insurance fraud dari data klaim."
)


# Load model dan fitur saat startup
model = joblib.load("model_top10.joblib")
top10_features = joblib.load("top10_features_list.joblib")

from pydantic import BaseModel, Field

class FraudRequest(BaseModel):
    data: dict = Field(
        ...,
        example={
            "Fault": 1,
            "BasePolicy": 1,
            "AddressChange-Claim": 0,
            "Year": 1995,
            "Deductible": 400,
            "Month": 11,
            "PolicyType": 2,
            "NumberOfCars": 0,
            "MonthClaimed": 12,
            "AccidentArea": 1
        }
    )


# API Key
API_KEY = "b6e9ff7542abbd81a0a47b6e76c9d2a30ec89f39f772edc7196e3fbf37dd74e6"

@app.post("/v1/predict")
def predict_fraud(req: FraudRequest, x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")

    try:
        df = pd.DataFrame([req.data])
        df = df[top10_features]

        # Prediksi
        pred = model.predict(df)[0]
        prob = model.predict_proba(df)[0][1]

        # Risk level
        if prob >= 0.8:
            risk_level = "high"
        elif prob >= 0.5:
            risk_level = "medium"
        else:
            risk_level = "low"

        return {
            "is_fraud": bool(pred),
            "fraud_probability": round(float(prob), 4),
            "risk_level": risk_level
        }

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/v1/health")
def health_check():
    return {
        "status": "ok",
        "message": "Insurance Fraud Detection API is healthy.",
        "version": "1.0.0"
    }



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8888, reload=True)
