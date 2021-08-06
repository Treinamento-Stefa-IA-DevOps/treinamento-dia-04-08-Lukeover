import pickle
from fastapi import FastAPI ,status

app = FastAPI()
@app.post('/model', status_code=200)
## Coloque seu codigo na função abaixo
def titanic(Sex:int,Age:float,Lifeboat:int,Pclass:int):
    pred = ([[Sex,Age,Lifeboat,Pclass]])
    with open('model/Titanic.pkl', 'rb') as fid: 
        print(pred)
        titanic = pickle.load(fid)
        answer = bool(titanic.predict(pred))
        m = "Que pena, você morreria no titanic :("
        if answer: 
            m = "Parabéns você sobreviveria ao titanic!"
        status_code = status.HTTP_200_OK
    return {"survived": answer,"status": status_code,"message": m}

@app.get('/model')
def get():
    return {'hello':'test'}
