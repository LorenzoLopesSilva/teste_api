from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

class Pessoas(BaseModel):
    nome: str
    idade: int | None = None
    email: str

app = FastAPI()

@app.get("/")
def home():
    return "Acessar /pessoas"

#----------------------------------------------------------
df = pd.read_excel('teste.xlsx', sheet_name='Planilha')

pessoas = {}

for i in range(len(df)):
    nome = df.iloc[i].iloc[0]
    idade = int(df.iloc[i].iloc[1])
    pessoas[i] = {"nome": nome, "idade": idade}


@app.get("/pessoas/")
def visualizarPessoas():
    return pessoas

