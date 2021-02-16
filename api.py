from fastapi import FastAPI
from api_models import PredictReponse
from datetime import datetime
from predict import HousePriceModel


app = FastAPI()

@app.get("/")
def root():
    return {"status": "online"}


@app.post("/predict", response_model=PredictReponse)
def predict(inputs: dict):

    model = HousePriceModel()

    start = datetime.today()
    pred = model.predict(inputs)[0]
    dur = (datetime.today() - start).total_seconds()

    # Create response object
    response = PredictReponse(prediction=pred, duration=dur)

    return response
