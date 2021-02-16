from pydantic import BaseModel

class PredictReponse(BaseModel):
    prediction: float
    duration: float = None
