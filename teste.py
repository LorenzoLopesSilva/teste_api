#-------------------------------------------------------
import pandas as pd

planilha = pd.read_excel('teste.xlsx', sheet_name='Planilha')

pessoas = {}

for i in range(len(planilha)):
    nome = planilha.iloc[i].iloc[0]
    idade = int(planilha.iloc[i].iloc[1])
    pessoas[i] = {"nome": nome, "idade": idade}

print(pessoas)

