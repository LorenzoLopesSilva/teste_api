# 1. Instale as dependências
# pip install fastapi uvicorn pydantic

# 2. Crie o arquivo main.py
from fastapi import FastAPI
from pydantic import BaseModel

# 3. Defina o modelo de dados para o JSON
class Item(BaseModel):
    nome: str
    email: str

# 4. Crie a instância do FastAPI
app = FastAPI()

# 5. Crie a rota que recebe o JSON via POST
@app.post("/items/")
async def criar_item(item: Item):
    """
    Recebe dados JSON, os valida e retorna uma mensagem de confirmação.
    """
    return {"mensagem": f"Item '{item.nome}' criado com sucesso!"}

# 6. Execute a API com o Uvicorn
# No terminal, use o comando: uvicorn main:app --reload
