import pandas as pd

archivo_ipc = "sh_ipc_aperturas.xls"

ipc_patagonico = pd.read_excel(archivo_ipc, sheet_name = "Variación mensual aperturas", skiprows = 252, nrows=  45)

ipc_patagonico = ipc_patagonico.dropna ()

ipc_patagonico = ipc_patagonico.melt (id_vars=["Región Patagonia"], var_name= "Periodo",value_name="IPC")

ipc_patagonico.rename (columns = {"Región Patagonia" : "Nivel"}, inplace=True)

print (ipc_patagonico.dtypes)

ipc_patagonico.to_csv ("tabla.csv")