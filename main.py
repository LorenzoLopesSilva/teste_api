from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

pessoas = []

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("index.html")

@app.post("/postdata/")

def postdata(username: str = Form(), userage: int = Form()):
    pessoas.append({"name": username, "age": userage})
    return root()