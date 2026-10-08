# Project Report

# California House Price Prediction System

**Author:** Muhammad Faizan Farooq
**Domain:** Machine Learning · Real Estate
**Technologies:** Python, scikit-learn (Random Forest), FastAPI
**Repository:** https://github.com/faizanjutt473/House_Prediction_Price-California-USA

---

## 1. Executive Summary

This project delivers an end-to-end system for predicting California house prices. A Random Forest regression model is trained on the California Housing dataset and deployed through a FastAPI service. Users can request an instant valuation for a single property or upload a CSV file to price hundreds of homes at once and download the results.

---

## 2. Problem Statement

Accurate property valuation supports buyers, sellers, agents and lenders, but manual appraisal is slow and does not scale. The goal is to build a model that estimates median house value from location and neighborhood features, and to make it usable through an always-available API.

---

## 3. Objectives

1. Explore the California Housing dataset and understand key price drivers.
2. Train and evaluate a Random Forest regression model.
3. Provide instant single-property predictions via a REST API.
4. Support bulk predictions through CSV upload with downloadable output.
5. Document the project so it is reproducible and extensible.

---

## 4. Tools and Technologies

| Component | Technology | Role |
|---|---|---|
| Language | Python | Core development |
| Data handling | pandas, NumPy | Loading and transforming data |
| Modeling | scikit-learn | Random Forest Regressor, metrics |
| Deployment | FastAPI, Uvicorn | REST API |
| Persistence | joblib | Saving and loading the model |

---

## 5. System Architecture

```
┌────────────┐   ┌─────────────┐   ┌──────────────────┐   ┌─────────────┐
│  Dataset   │ → │ explore.py  │ → │ train_model.py   │ → │ Saved Model │
└────────────┘   └─────────────┘   │ Random Forest    │   └──────┬──────┘
                                   └──────────────────┘          │
                                                                 ▼
                     ┌──────────────────┐             ┌──────────────────┐
                     │ Client / User    │  ←───────→  │ main.py (FastAPI)│
                     │ Single JSON / CSV│             │ Single + Bulk    │
                     └──────────────────┘             └──────────────────┘
```

### Repository Components

| File | Responsibility |
|---|---|
| `explore.py` | Dataset exploration |
| `train.py`, `train_model.py` | Model training and evaluation |
| `main.py` | FastAPI app with single and bulk prediction |
| `requirements.txt` | Dependencies |
| `README.md` | Documentation |

---

## 6. Methodology

### 6.1 Data Exploration

The dataset is inspected for structure, summary statistics, missing values and feature ranges. Relationships between features such as median income, location and house value are reviewed to guide modeling.

### 6.2 Data Preparation

Data is cleaned, features are prepared and the dataset is split into training and testing sets so performance is measured on unseen data.

### 6.3 Model Selection — Why Random Forest?

| Advantage | Explanation |
|---|---|
| Non-linear relationships | Captures complex interactions such as location and income |
| Robustness | Averages many trees, reducing overfitting |
| Little scaling needed | Works well without heavy feature scaling |
| Feature importance | Shows which features drive predictions |

### 6.4 Training and Evaluation

The Random Forest Regressor is trained on the training set and evaluated on the test set using R², MAE, MSE and RMSE. The final model is saved for the API.

### 6.5 Deployment with FastAPI

`main.py` loads the saved model and exposes:

- **Single prediction** — one property's features in, predicted price out.
- **Bulk prediction** — a CSV upload is processed row by row; the result file includes the predicted prices and can be downloaded.

FastAPI provides interactive documentation at `/docs`, and the service is designed for 24/7 availability.

---

## 7. Evaluation

| Metric | Meaning |
|---|---|
| R² Score | Proportion of variance in house value explained |
| MAE | Average absolute prediction error |
| MSE | Average squared error, penalizing large mistakes |
| RMSE | Error expressed in price units |

### Results

Run `python train_model.py` and record the scores:

| Metric | Score |
|---|---|
| R² Score | _add your value_ |
| MAE | _add your value_ |
| RMSE | _add your value_ |

---

## 8. Key Findings

- **Median income** is typically the strongest predictor of house value in this dataset.
- **Location** (latitude and longitude) strongly affects price, reflecting coastal and urban premiums.
- Random Forest handles these non-linear effects better than a plain linear model.

_(Confirm these against your own feature-importance output before final submission.)_

---

## 9. Challenges and Limitations

| Challenge | Impact |
|---|---|
| Capped target values | The dataset caps high house values, which can limit accuracy at the top end |
| Aggregated block-level data | Predictions describe neighborhoods, not individual houses |
| Dated data | Prices may not reflect the current market |
| Model size | Large forests can be heavy to store and load |

---

## 10. Future Work

1. Benchmark against Gradient Boosting, XGBoost and LightGBM.
2. Tune hyperparameters with cross-validation.
3. Add feature importance and SHAP explanations.
4. Build a map-based frontend.
5. Containerize with Docker and deploy to the cloud.
6. Add automated tests and CI/CD.
7. Retrain periodically on newer data.

---

## 11. How to Reproduce

```bash
git clone https://github.com/faizanjutt473/House_Prediction_Price-California-USA.git
cd House_Prediction_Price-California-USA
pip install -r requirements.txt

python explore.py
python train_model.py
uvicorn main:app --reload     # http://127.0.0.1:8000/docs
```

---

## 12. Conclusion

The project turns a classic regression problem into a usable service. By combining a Random Forest model with a FastAPI backend, it offers both instant single valuations and scalable bulk predictions, providing a solid, extensible foundation for real-estate price estimation.

---

**Prepared by:** Muhammad Faizan Farooq
**Contact:** faizanprogrammer12@gmail.com · [GitHub](https://github.com/faizanjutt473) · [LinkedIn](https://www.linkedin.com/in/muhammad-faizan-farooq-8bab35372)
