# 🏠 Boston Housing Price Prediction (FastAPI + Machine Learning)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-brightgreen)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML%20Model-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A web-based **machine learning app** that predicts **Boston housing prices** using a **Linear Regression** model deployed with **FastAPI** and a **Jinja2-powered HTML interface**.

---

## 📘 Overview

This project demonstrates a **complete ML workflow**:

1. Train a regression model on the Boston Housing dataset
2. Save it using `pickle` for reuse
3. Deploy the model using **FastAPI**
4. Build a dynamic HTML form to collect input
5. Predict and render results using **Jinja2 templates**

---

## 🧩 Features

✅ FastAPI backend for ML inference  
✅ Clean and interactive HTML form (Jinja2 + CSS + JS)  
✅ Real-time prediction display  
✅ Input validation with form fields  
✅ Easily deployable (Docker / Cloud / Localhost)

---

## 🧱 Folder Structure

```
boston_house_price/
│
├── app.py                  # FastAPI backend (main entry)
├── regmodel.pkl            # Trained Linear Regression model
├── scaling.pkl             # StandardScaler for input scaling
│
├── templates/
│   └── form.html           # HTML frontend template
│
├── static/
│   ├── style.css           # CSS for styling
│   └── script.js           # JS for animation/interactivity
│
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Tech Stack

| Category              | Technology                       |
| --------------------- | -------------------------------- |
| **Backend**           | FastAPI                          |
| **Frontend**          | HTML5, CSS3, JavaScript          |
| **Templating Engine** | Jinja2                           |
| **Model**             | Linear Regression (Scikit-learn) |
| **Data Handling**     | Pandas                           |
| **Web Server**        | Uvicorn (ASGI)                   |

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/santhoshkumar0810/boston_house_price.git
cd boston_house_price
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # macOS/Linux
.venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

Using `pip`:

```bash
pip install -r requirements.txt
```

or using `uv`:

```bash
uv add fastapi uvicorn jinja2 python-multipart scikit-learn pandas
```

### 4️⃣ Run the FastAPI App

```bash
uvicorn app:app --reload --port 5000
```

Now open your browser at:
👉 **http://127.0.0.1:5000**

---

## 💻 Usage

1. Enter values for the 13 housing features in the form
2. Click **Predict**
3. The app will:
   - Scale your inputs using the trained `StandardScaler`
   - Predict price using the saved regression model
   - Render the result instantly in the browser

---

## 🧮 Model Details

The trained **Linear Regression** model predicts the **median value of owner-occupied homes (MEDV)** in $1000’s.  
It uses the following 13 features:

| Feature | Description                                            |
| ------- | ------------------------------------------------------ |
| CRIM    | Per capita crime rate by town                          |
| ZN      | Residential land zoned proportion                      |
| INDUS   | Non-retail business acres per town                     |
| CHAS    | Charles River dummy variable (1 if bounds river)       |
| NOX     | Nitric oxides concentration                            |
| RM      | Average number of rooms per dwelling                   |
| AGE     | Proportion of owner-occupied units built before 1940   |
| DIS     | Weighted distances to employment centers               |
| RAD     | Accessibility to radial highways                       |
| TAX     | Property-tax rate per $10,000                          |
| PTRATIO | Pupil-teacher ratio                                    |
| B       | 1000(Bk - 0.63)^2 (Bk = proportion of Black residents) |
| LSTAT   | % lower status population                              |

---

## 📂 requirements.txt

```txt
fastapi
uvicorn
jinja2
python-multipart
pandas
scikit-learn
```

## 🧠 API Endpoints

| Method | Endpoint | Description                                               |
| ------ | -------- | --------------------------------------------------------- |
| `GET`  | `/`      | Renders the HTML form                                     |
| `POST` | `/`      | Accepts input data, scales, predicts, and displays result |

### Example cURL request

```bash
curl -X 'POST'   'http://127.0.0.1:5000/'   -F 'CRIM=0.02'   -F 'ZN=18'   -F 'INDUS=2.3'   -F 'CHAS=0'   -F 'NOX=0.5'   -F 'RM=6'   -F 'AGE=60'   -F 'DIS=4'   -F 'RAD=1'   -F 'TAX=300'   -F 'PTRATIO=15'   -F 'B=390'   -F 'LSTAT=5'
```

---

## ☁️ Deployment

### ▶️ Local

```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

```


## 👨‍💻 Author

Santhosh Kumar M
📧 santhoshkumar082003@gmail.com
🌐 https://github.com/santhoshkumar0810

---

```
