# Importa la librería para descargar el archivo
 
import requests

# Define la URL de descarga del archivo

url_descarga = 'https://www.indec.gob.ar/ftp/cuadros/economia/sh_ipc_aperturas.xls'

# Consulta la información del archivo de la URL de descarga

respuesta = requests.get(url_descarga)

# Escribe un archivo con los datos de la consulta

nombre_archivo = 'sh_ipc_aperturas.xls'

open(nombre_archivo, "wb").write(respuesta.content)

# Notifica la operación

print (f"Descarga finalizada. Archivo guardado en {nombre_archivo}")