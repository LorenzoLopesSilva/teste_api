#-------------------------------------------------------
import pandas as pd

planilha = pd.read_excel('sub-faturamento.xlsx', sheet_name='Sheet1')


pessoas = {}

for i in range(len(planilha)):
    fornecedor = planilha.iloc[i].iloc[6]
    email = planilha.iloc[i].iloc[7]
    pessoas[i] = {"fornecedor": fornecedor, "email": email}

print(pessoas)

