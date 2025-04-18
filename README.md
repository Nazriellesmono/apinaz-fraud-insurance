# 🛡️ Insurance Fraud Detection API

API ini dirancang untuk mendeteksi kemungkinan klaim asuransi palsu menggunakan machine learning. Model ini telah dilatih dengan dataset insurance fraud dan mendukung prediksi berdasarkan fitur top-10 yang paling berpengaruh.

---

## 🚀 Features
- Predict apakah klaim tergolong fraud
- Menyediakan probabilitas fraud
- Skor risiko: Low / Medium / High
- Menggunakan model XGBoost (Top 10 features)
- Support API Key untuk autentikasi

---

## 📦 Endpoint

### `POST /v1/predict`
- **Deskripsi**: Memprediksi kemungkinan fraud berdasarkan data input.
- **Headers**:
  - `x-api-key`: API key Anda
- **Body (JSON)**:
```json
{
  "data": {
    "Month": "Jan",
    "AccidentArea": "Urban",
    "Sex": "Male",
    "Fault": "Policy Holder",
    "VehicleCategory": "Sedan",
    "VehiclePrice": "20000",
    "Days:Policy-Claim": 15,
    "AgeOfVehicle": "2",
    "PoliceReportFiled": "Yes",
    "WitnessPresent": "No"
  }
}
```
- **Response**:
```json
{
  "prediction": "is fraud",
  "fraud_probability": 0.82,
  "risk_level": "high"
}
```

### `GET /v1/health`
- Mengecek status API

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
Untuk menggunakan endpoint, Anda perlu menambahkan header:
```bash
x-api-key: your_api_key_here
```

API Key default dapat Anda ubah di file `main.py`.

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
📦 **Stable MVP** – Siap digunakan untuk demo atau integrasi internal. Cocok untuk portofolio dan showcase profesional.

> Powered by OpenAI's GPT + Mentor feedback.

