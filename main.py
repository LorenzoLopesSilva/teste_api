from fastapi import FastAPI, Form
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def root():
    return FileResponse("index.html")

@app.post("/postdata/")
def postdata(username: str = Form(), userage: int = Form()):
    return {"name": username, "age": userage}