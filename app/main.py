from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import joblib
import numpy as np
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Bisa diubah ke ["*"] untuk mengizinkan semua
    allow_credentials=True,
    allow_methods=["*"],  # Izinkan semua metode (GET, POST, OPTIONS, dll)
    allow_headers=["*"],  # Izinkan semua header
)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.options("/predict")
async def options_handler():
    return {"message": "OK"}

with open("app/rf.pkl", "rb") as model_file:
    model = joblib.load(model_file)

with open("app/skew.pkl", "rb") as model_skew:
    skew_model = joblib.load(model_skew)

with open("app/scaler.pkl", "rb") as model_scaler:
    scaler_model = joblib.load(model_scaler)

class InputData(BaseModel):
    data: list[list[float]] #Multiple data
    #data: list[float] Single Data

@app.get("/")
def root():
    return {"API is Runnning, Use /predict to Get Predictions"}

@app.post("/predict")
async def predict(input_data: InputData):
    X = np.array(input_data.data) #Jika menggunakan multiple data tidak perlu dilakukan reshape
    select_feature = [1, 3, 4, 7, 10, 11, 12, 14, 16, 17, 18]
    filter_data = X[:,select_feature]
    X_transform = skew_model.transform(filter_data)
    X_scaler = scaler_model.transform(X_transform)
    X_final = X_scaler[:,1:]
    predict = model.predict(X_final).tolist()
    predict_labels = ["Non" if p == 0 else "Fraud" for p in predict]
    return {"prediction": predict_labels}