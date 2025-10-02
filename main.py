from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
# from starlette.responses import JSONResponse

class Item(BaseModel):
    nome: str
    email: str

#

app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/items/")
async def criar_item(item: Item):

    # return{"mensagem": f"Olá {item.nome}"}

    return JSONResponse (
        content={"mensagem": f"Seja bem vindo {item.nome}"}
    )

@app.get("/")
async def read_root():
    return {"hello": "World"}
