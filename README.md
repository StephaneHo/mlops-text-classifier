# Projet de classification, basé sur un projet soclaire



## train.py
Sert à entrainer le modèle

## fetch_model
Recupère le modèle qu'on avait entrainé, et le model_name est donné par le paramètre: registered_model_name qu'on avait renseigné dans train.py

## data_model
Sert à créer un modèle Pydantic pour consolider le modèle de données



# Pour lancer l'application

## Installer les dépendances
uv sync

## Entrainer le modèle
python app/train.py

## Lancer un serveur web ASGI pour l'API FastAPI.
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000

la page http://localhost:8000/docs#/ doit alors etre disponible avec les API
(FastAPI sert automatiquement Swagger UI) 

## Faire une prédiction
dans mmain.py on a défini l'API @app.post("/predict") avec des paramètres
{
  "sepal_length": 5,
  "sepal_width": 3.6,
  "petal_length": 1.4,
  "petal_width": 0.2
}
on devrait trouver: {
  "prediction": 0
}, ce qui correspond à la classe iris setosa