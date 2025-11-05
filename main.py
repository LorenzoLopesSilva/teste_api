from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

pessoas = []

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("index.html")

@app.post("/postdata/")

def postdata(escolha: str = Form()):
    return {'escolha': escolha}
    