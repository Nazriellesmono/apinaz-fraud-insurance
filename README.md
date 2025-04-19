# 🛡️ Insurance Fraud Detection API

This API is designed to detect potential fraudulent insurance claims using machine learning. The model has been trained with an insurance fraud dataset and supports prediction based on the top 10 most influential features.

---

## 🚀 Features
- Predict whether a claim is fraudulent
- Returns fraud probability
- Risk level: Low / Medium / High
- Powered by XGBoost model (Top 10 features)
- API Key authentication supported

---

## 📦 Endpoints

### `POST /v1/predict`
- **Description**: Predicts the likelihood of insurance fraud based on input data.
- **Headers**:
  - `x-api-key`: Your API key
- **Body (JSON)**:
```json
{
  "data": {
    "AccidentArea": 1,
    "AddressChange-Claim": 0,
    "BasePolicy": 1,
    "Deductible": 400,
    "Fault": 1,
    "Month": 11,
    "MonthClaimed": 12,
    "NumberOfCars": 0,
    "PolicyType": 2,
    "Year": 1995
  }
}
```
- **Response**:
```json
{
  "is_fraud": false,
  "fraud_probability": 0.0035,
  "risk_level": "low"
}
```

### `GET /v1/health`
- Check the health status of the API

---

## 🐳 Docker Support
### Build
```bash
docker build -t apinaz-fraud-insurance .
```
### Run
```bash
docker run -d -p 8888:8888 apinaz-fraud-insurance
```

---

## 🔐 API Key
To use the endpoint, include the header:
```bash
x-api-key: your_api_key_here
```

You can change the default API Key inside `main.py`.

---

## 🧪 API Documentation (Swagger)

Once the Docker container is running, you can access the interactive API documentation via Swagger UI:

👉 [http://localhost:8888/docs](http://localhost:8888/docs)

This documentation includes:
- Input schema (JSON)
- Example payloads
- Output probability of fraud detection
- Real-time ROC/AUC evaluation

---

## 📚 Tech Stack
- FastAPI
- XGBoost
- Joblib
- Docker
- Pydantic

---

## 🧠 Author
- **Nazriellesmono**
- GitHub: [@Nazriellesmono](https://github.com/Nazriellesmono)

---

## ✨ Status
📦 **Stable MVP** – Ready for demo and internal integration. Ideal for portfolio and professional showcase.

> Powered by OpenAI's GPT + Mentor feedback.

