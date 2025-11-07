import pickle

import pandas as pd
import uvicorn
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# ===== Load Model and Scaler =====
model = pickle.load(open("regmodel.pkl", "rb"))
scaler = pickle.load(open("scaling.pkl", "rb"))

# ===== Initialize App =====
app = FastAPI(title="Boston Housing Prediction")

# Serve static files (CSS, JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

FEATURES = [
    "CRIM",
    "ZN",
    "INDUS",
    "CHAS",
    "NOX",
    "RM",
    "AGE",
    "DIS",
    "RAD",
    "TAX",
    "PTRATIO",
    "B",
    "LSTAT",
]


@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse(
        "form.html", {"request": request, "prediction": None}
    )


@app.post("/", response_class=HTMLResponse)
async def post_predict(
    request: Request,
    CRIM: float = Form(...),
    ZN: float = Form(...),
    INDUS: float = Form(...),
    CHAS: float = Form(...),
    NOX: float = Form(...),
    RM: float = Form(...),
    AGE: float = Form(...),
    DIS: float = Form(...),
    RAD: float = Form(...),
    TAX: float = Form(...),
    PTRATIO: float = Form(...),
    B: float = Form(...),
    LSTAT: float = Form(...),
):
    data = pd.DataFrame(
        [[CRIM, ZN, INDUS, CHAS, NOX, RM, AGE, DIS, RAD, TAX, PTRATIO, B, LSTAT]],
        columns=FEATURES,
    )
    scaled = scaler.transform(data)
    prediction = model.predict(scaled)[0]

    return templates.TemplateResponse(
        "form.html", {"request": request, "prediction": round(prediction, 2)}
    )


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5000, reload=True)
