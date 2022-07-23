from unittest import skip
import pandas as pd

archivo_ipc = "sh_ipc_aperturas.xls"

#archivo_ipc = "prueba.xlsx"

ipc_patagonico = pd.read_excel(archivo_ipc, sheet_name = "Variación mensual aperturas", skiprows = 252, nrows=  45)

ipc_patagonico = ipc_patagonico.dropna ()

print(ipc_patagonico)

ipc_patagonico.to_csv("ipc.csv")