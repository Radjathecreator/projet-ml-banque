from pydantic import BaseModel

class PredictRequest(BaseModel):
    amt: float
    city_pop: int
    gender: int

class PredictResponse(BaseModel):
    prediction: int
    model_version: str
