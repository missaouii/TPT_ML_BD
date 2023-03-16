import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse 
from fastapi.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
import pandas as pd
import numpy as np
import pickle
from fastapi.responses import JSONResponse
from fastapi import FastAPI,Response


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

pkl_filename = "model.pkl"
with open(pkl_filename, 'rb') as file:
    model_data = pickle.load(file)

feature_names = model_data.feature_names_in_
target_names = model_data.classes_
model = model_data
@app.get("/")
def home():
    return{"Voici la partie Api avec FastApi pour le modèle":"Random Forrest"}


@app.post('/predict', response_class=HTMLResponse)
async def predict(request: Request,                   
                age: float = Form(),
                sexe: str = Form(),
                taux: float = Form(),
                situationFamiliale: str = Form(),
                nbEnfantsAcharge: float = Form(),
                secvoiture: str = Form()
                  ):


    if not(sexe.lower() in ["male", "female"]):
        return JSONResponse({'error': 'Sexe doit être male ou female.'})
    if not(situationFamiliale.lower() in ["celibataire", "en couple"]):
        return JSONResponse({'error': 'situationFamiliale doit être celibataire ou en couple.'})
    if not(secvoiture.lower() in ["oui", "non"]):
        return JSONResponse({'error': 'secvoiture doit être oui ou non.'})
    

    sexe_male = 0
    sexe_female = 0

    if sexe.lower() == 'male':
        sexe_male = 1
        sexe_female = 0
    elif sexe.lower() == 'female':
        sexe_male = 0
        sexe_female = 1
    
    if situationFamiliale.lower() == 'celibataire':
        situationFamiliale_Célibataire = 1
        situationFamiliale_En_couple = 0
    elif situationFamiliale.lower() == 'en couple':
        situationFamiliale_Célibataire = 0
        situationFamiliale_En_couple = 1
    if secvoiture.lower() == 'oui':
        secvoiture = 1
    elif situationFamiliale.lower() == 'non':
        secvoiture = 0

    int_features = [age, taux,nbEnfantsAcharge,secvoiture,sexe_female,sexe_male,situationFamiliale_Célibataire,situationFamiliale_En_couple]
    final = np.array(int_features)
    print(final)
    data_unseen = pd.DataFrame([final], columns = feature_names)
    print(data_unseen)
    prediction =  model.predict(data_unseen)[0]
    return JSONResponse({"La catégorie de voiture est ": prediction})

if(__name__) == '__main__':
    uvicorn.run(
        "app:app",
        host    = "0.0.0.0",
        port    = 5000, 
        reload  = True
    )