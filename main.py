from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Item(BaseModel):
    nome: str
    email: str



app = FastAPI()


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credencials=False,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/items/")
async def criar_item(item: Item):
    """
    Recebe dados JSON, os valida e retorna uma mensagem de confirmação.
    """
    return {"mensagem": f"Item '{item.nome}' criado com sucesso!"}
