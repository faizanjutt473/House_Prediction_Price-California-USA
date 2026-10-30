#  California House Price Prediction

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-REST%20API-009688?logo=fastapi&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Random%20Forest-F7931E?logo=scikitlearn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

A machine learning system that predicts **median house values in California** using a **Random Forest Regressor** and serves predictions through a **FastAPI** REST service. It supports instant single-property valuations as well as **bulk predictions** by uploading a CSV file, with downloadable results.

---

##  Table of Contents

1. [Overview](#-overview)
2. [Key Features](#-key-features)
3. [Tech Stack](#-tech-stack)
4. [Dataset](#-dataset)
5. [Project Structure](#-project-structure)
6. [Installation](#-installation)
7. [Usage](#-usage)
8. [API Reference](#-api-reference)
9. [Machine Learning Workflow](#-machine-learning-workflow)
10. [Model Evaluation](#-model-evaluation)
11. [Future Improvements](#-future-improvements)
12. [Contributing](#-contributing)
13. [Author](#-author)

---

##  Overview

Estimating property value accurately is important for buyers, sellers, real-estate agents and lenders. This project builds a regression model on the **California Housing dataset** and wraps it in a FastAPI application so that valuations are available on demand, around the clock, through a simple API.

---

##  Key Features

- 🏡 **Instant single-property valuation** — submit one property's details and get a predicted price
- 📂 **Bulk processing** — upload a CSV with hundreds of homes and predict all prices at once
- ⬇️ **Downloadable results** — get the updated file with predictions added
- 🌲 **Random Forest Regressor** for robust, non-linear price prediction
- ⚡ **FastAPI** backend with automatic Swagger documentation
- 🕒 Designed for **24/7 availability** as a deployed service

---

##  Tech Stack

| Category | Tools |
|---|---|
| Language | Python |
| Machine Learning | scikit-learn (Random Forest) |
| Data Handling | pandas, NumPy |
| API Framework | FastAPI, Uvicorn |
| Model Storage | joblib |

---

## 📊 Dataset

- **Dataset:** California Housing Dataset
- **Goal:** Build a regression model to predict **median house value**
- **Typical features:** median income, house age, average rooms, average bedrooms, population, average occupancy, latitude, longitude

---

## 📁 Project Structure

```
House_Prediction_Price-California-USA/
│
├── explore.py         # Data exploration and analysis
├── train.py           # Model training script
├── train_model.py     # Model training and evaluation for the housing dataset
├── main.py            # FastAPI application (single & bulk prediction)
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

| File | Purpose |
|---|---|
| `explore.py` | Explores the dataset: structure, statistics, missing values |
| `train.py` / `train_model.py` | Train the Random Forest model, evaluate it and save it |
| `main.py` | Loads the saved model and serves predictions through FastAPI |
| `requirements.txt` | Python dependencies |

---

##  Installation

**1. Clone the repository**

```bash
git clone https://github.com/faizanjutt473/House_Prediction_Price-California-USA.git
cd House_Prediction_Price-California-USA
```

**2. Create a virtual environment (recommended)**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

---

##  Usage

### Step 1 — Explore the data

```bash
python explore.py
```

### Step 2 — Train the model

```bash
python train_model.py
```

Trains the Random Forest model, prints evaluation metrics and saves the trained model.

### Step 3 — Run the API

```bash
uvicorn main:app --reload
```

- API: http://127.0.0.1:8000
- Swagger UI: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

---

##  API Reference

> Endpoint names and fields below follow the standard California Housing format. Adjust them to match your `main.py` if they differ.

### `POST /predict` — Single property

**Request**

```json
{
  "MedInc": 8.3252,
  "HouseAge": 41,
  "AveRooms": 6.98,
  "AveBedrms": 1.02,
  "Population": 322,
  "AveOccup": 2.55,
  "Latitude": 37.88,
  "Longitude": -122.23
}
```

**Response**

```json
{
  "predicted_price": 4.52
}
```

### `POST /predict-bulk` — CSV upload

Upload a CSV file containing one property per row. The API returns the file with a predicted price column added, ready to download.

---

##  Machine Learning Workflow

```
Raw Data → Exploration → Cleaning → Train/Test Split
        → Random Forest Regressor → Evaluation → Save Model → FastAPI Deployment
```

1. **Exploration** — understand distributions, ranges and missing values.
2. **Preprocessing** — clean the data and prepare features.
3. **Training** — fit a Random Forest Regressor on the training set.
4. **Evaluation** — measure error on unseen test data.
5. **Deployment** — serve the saved model through FastAPI for single and bulk predictions.

---

##  Model Evaluation

Regression metrics used:

| Metric | Description |
|---|---|
| R² Score | Share of price variance explained by the model |
| MAE | Mean Absolute Error — average size of the error |
| MSE | Mean Squared Error — penalizes large errors |
| RMSE | Root Mean Squared Error — error in original price units |

Run `python train_model.py` and add your scores:

| Metric | Score |
|---|---|
| R² Score | _add your value_ |
| MAE | _add your value_ |
| RMSE | _add your value_ |

---

##  Future Improvements

- Compare with Gradient Boosting, XGBoost and LightGBM
- Hyperparameter tuning with GridSearchCV / RandomizedSearchCV
- Feature importance and SHAP explanations
- Interactive map-based frontend (Streamlit or React)
- Docker containerization and cloud deployment
- Unit tests and CI/CD with GitHub Actions

---

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m "Add your feature"`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

##  Author

**Muhammad Faizan Farooq**
Machine Learning / AI Engineer

- GitHub: [faizanjutt473](https://github.com/faizanjutt473)
- LinkedIn: [Muhammad Faizan Farooq](https://www.linkedin.com/in/muhammad-faizan-farooq-8bab35372)
- Email: faizanprogrammer12@gmail.com

---

⭐ If you found this project useful, please consider giving it a star!
