# Importa las librerías necesarias
 
import requests # para la descarga del archivo
import pandas as pd # para la manipulación del DF

# Define la URL de descarga del archivo

url_descarga = 'https://www.indec.gob.ar/ftp/cuadros/economia/sh_ipc_aperturas.xls'

# Consulta la información del archivo de la URL de descarga

respuesta = requests.get(url_descarga)

# Escribe un archivo con los datos de la consulta

nombre_archivo = 'sh_ipc_aperturas.xls'

open(nombre_archivo, "wb").write(respuesta.content)

# Notifica la operación

print (f"Descarga finalizada. Archivo guardado en {nombre_archivo}")

# Armado de DF con parámetros tidy

ipc_patagonico = pd.read_excel(nombre_archivo, sheet_name = "Variación mensual aperturas", skiprows = 252, nrows=  45)

ipc_patagonico = ipc_patagonico.dropna ()

ipc_patagonico = ipc_patagonico.melt (id_vars=["Región Patagonia"], var_name= "Periodo",value_name="IPC")

ipc_patagonico.rename (columns = {"Región Patagonia" : "Nivel"}, inplace=True)

# Notifica el tipo de datos de cada columna

print (ipc_patagonico.dtypes)

# Exporta a un archivo csv

ipc_patagonico.to_csv ("ipc_patagonico.csv")