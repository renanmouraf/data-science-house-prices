from fastapi import FastAPI
from datetime import datetime
from predict import HousePriceModel

app = FastAPI()

@app.get("/")
def root():
    return {"status": "online"}

@app.post("/predict")
def predict(inputs: dict):

    model = HousePriceModel()

    start = datetime.today()
    pred = model.predict(inputs)[0]
    dur = (datetime.today() - start).total_seconds()

    return pred
