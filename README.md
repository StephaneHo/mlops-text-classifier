Project of classification, based on a scholar project



# train.py
Sert à entrainer le modèle

# fetch_model
Recupère le modèle qu'on avait entrainé, et le model_name est donné par le paramètre: registered_model_name qu'on avait renseigné dans train.py

# data_model
Sert à créer un modèle Pydantic pour consolider le modèle de données



To launch:

# Install dependencies
uv sync

# Lancer un serveur web ASGI pour l'API FastAPI.
uv run uvicorn app.main:app --host 0.0.0.0 --port 8000


