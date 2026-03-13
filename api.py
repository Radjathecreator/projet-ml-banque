from fastapi import FastAPI
from schemas import PredictRequest, PredictResponse
import joblib

app = FastAPI(title="API de Prédiction de Fraude")

# On charge le modèle au démarrage
artefact = joblib.load("model.joblib")
modele = artefact["model"]
version_modele = artefact["version"]

@app.get("/health")
def health():
    return {"status": "ok", "version": version_modele}

@app.post("/predict", response_model=PredictResponse)
def predict(payload: PredictRequest):
    donnees_entree = [[payload.amt, payload.city_pop, payload.gender]]
    prediction_resultat = modele.predict(donnees_entree)[0]
    return PredictResponse(prediction=int(prediction_resultat), model_version=version_modele)
