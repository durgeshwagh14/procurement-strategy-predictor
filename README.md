# 📦 Procurement Strategy Predictor  
### Kraljic Matrix Classification using Machine Learning

🔗 **Live Application:**  
https://procurement-strategy-predictor-vfnpkxaynblfqma9xxicsh.streamlit.app/

---

## 📌 Project Overview

The **Procurement Strategy Predictor** is an end-to-end Machine Learning web application that classifies products into the four Kraljic Matrix categories:

- 🟢 Non-Critical
- 🔵 Leverage
- 🟡 Bottleneck
- 🔴 Strategic

This tool helps procurement managers, supply chain analysts, and business strategists make data-driven sourcing decisions.

The model is trained on a realistic procurement dataset and deployed using **Streamlit**.

---

## 🧠 Business Problem

Procurement teams must categorize products based on:

- Supply Risk
- Profit Impact
- Lead Time
- Cost
- Supplier Dependency

Manual classification can be subjective and inconsistent.

This ML model provides:
- Objective classification
- Instant prediction
- Decision-support automation

---

## 📊 Kraljic Matrix Concept

The Kraljic Matrix categorizes procurement items based on:
- **Supply Risk**
- **Profit Impact**

| Category       | Description |
|---------------|-------------|
| Strategic     | High risk, high impact |
| Bottleneck    | High risk, low impact |
| Leverage      | Low risk, high impact |
| Non-Critical  | Low risk, low impact |

---

## 🏗 Project Architecture

```

User Input (Streamlit UI)
↓
Preprocessing
↓
Trained ML Pipeline (Scaling + Naive Bayes)
↓
Prediction Output
↓
Displayed Category + Probability

```

---

## ⚙️ Features Used for Prediction

The model uses the following input features:

- Lead_Time_Days
- Order_Volume_Units
- Cost_per_Unit
- Supply_Risk_Score
- Profit_Impact_Score
- Environmental_Impact
- Single_Source_Risk (Encoded: Yes=1, No=0)

---

## 🤖 Machine Learning Approach

### Models Tested:

- K-Nearest Neighbors
- Gaussian Naive Bayes 
- Logistic Regression ✅ (Best Performing)
- Support Vector Machine

### Model Selection

Gaussian Naive Bayes achieved:

- ✅ 94% Accuracy
- Strong Precision & Recall
- Balanced Performance Across Classes

### Final Model

A **Scikit-learn Pipeline** was used:

- StandardScaler (Feature Scaling)
- GaussianNB (Classifier)

This ensures:
- Proper scaling
- Correct feature order
- Stable deployment performance

---

## 📁 Project Structure

```

├── app.py
├── Procurement.pkl
├── requirements.txt
├── realistic_kraljic_dataset.csv
└── README.md

````

## 🚀 Installation Guide (Run Locally)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
````

---

### 2️⃣ Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run Streamlit App

```bash
streamlit run app.py
```

Open browser:

```
http://localhost:8501
```

---

## 🌐 Deployment

This application is deployed using:

* Streamlit Cloud

Live URL:
[https://procurement-strategy-predictor-vfnpkxaynblfqma9xxicsh.streamlit.app/](https://procurement-strategy-predictor-vfnpkxaynblfqma9xxicsh.streamlit.app/)

---

## 🧪 Example Input

| Feature              | Example Value |
| -------------------- | ------------- |
| Lead Time            | 30            |
| Order Volume         | 100           |
| Cost per Unit        | 50            |
| Supply Risk Score    | 5             |
| Profit Impact Score  | 7             |
| Environmental Impact | 4             |
| Single Source Risk   | Yes           |

---

## 📈 Example Output

```
Predicted Category: Strategic
Prediction Probability:
Strategic: 0.85
Bottleneck: 0.05
Leverage: 0.05
Non-Critical: 0.05
```

---

## 🛠 Tech Stack

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Pickle

---

## 🎯 Key Learnings

* End-to-end ML workflow
* Model comparison & evaluation
* Handling feature scaling
* Pipeline creation
* Model serialization (.pkl)
* Streamlit deployment
* Production-ready prediction system

---

## 📌 Future Improvements

* Add authentication system
* Add data upload (CSV input)
* Add visualization dashboard
* Convert to REST API (FastAPI)
* Add database integration
* Deploy using Docker

---

