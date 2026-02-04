from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import joblib
from .schemas import Cliente
import os

app = FastAPI()

# Configuración obligatoria para que el navegador permita la conexión
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Permite peticiones desde cualquier origen (tu index.html)
    allow_credentials=True,
    allow_methods=["*"],      # Permite todos los métodos (incluyendo OPTIONS y POST)
    allow_headers=["*"],      # Permite todos los encabezados
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, "models", "rf_pipeline_smote.pkl")
modelo = joblib.load(MODEL_PATH)

@app.post("/predict")
def predecir(cliente: Cliente):
    # Convertimos a DataFrame
    df = pd.DataFrame([cliente.model_dump()])

     # Predecir
    prediccion = modelo.predict(df)[0]
    probabilidad = modelo.predict_proba(df)[0].tolist()

    return{
        "prediccion": int(prediccion),
        "probabilidad": float(probabilidad[1])
    }