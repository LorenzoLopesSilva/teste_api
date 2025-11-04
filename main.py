from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "Minha api está no ar"

@app.get("/teste/")
def teste():
    return "Odinospitos"