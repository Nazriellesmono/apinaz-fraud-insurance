# 🛡️ API - Insurance Fraud Detection (FastAPI)

This project provides a FastAPI-based Machine Learning API to detect insurance fraud and return a risk level: **Low**, **Mid**, or **High**.

## 📦 Features

- Real-time fraud detection
- Outputs fraud risk levels
- Simple JSON input/output
- Dockerized for easy deployment

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- Docker (for containerized deployment)

### Installation

```bash
git clone https://github.com/username/apinaz-fraud-insurance.git
cd apinaz-fraud-insurance
pip install -r requirements.txt
uvicorn main:app --reload --port 8888
