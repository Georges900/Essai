from fastapi import FastAPI
import json

app = FastAPI()

@app.get("/donnees")
def lire_fichier():
    with open("capteurs.json", "r") as f:
        data = json.load(f)   # Charger le JSON en dict Python
    return data 
