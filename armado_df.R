# Carga de librerías
library (tidyverse)
library (readxl)

# Limpieza del entorno

rm (list = ls())

# Definición de escritorio de trabajo

setwd ("/home/ramiro/Documentos/repositorios/tablero_ipc")

# Actualización de base de IPC

download.file(
  "https://www.indec.gob.ar/ftp/cuadros/economia/sh_ipc_aperturas.xls",
  "sh_ipc_aperturas.xls")

print ("Archivo de IPC actualizado :: Descargado")

# Carga de base de IPC. 
# Cada mes hay que ampliar el rango una columna. Abril 2022 = BM

ipc_patagonico <- read_excel("sh_ipc_aperturas.xls", 
                             range = "A253:BM298")

# Definición de niveles (intermedios)

niveles <- c ("Nivel general", "Alimentos y bebidas no alcohólicas", 
              "Bebidas alcohólicas y tabaco", "Prendas de vestir y calzado", 
              "Vivienda, agua, electricidad y otros combustibles", 
              "Equipamiento y mantenimiento del hogar", "Salud", "Transporte", 
              "Comunicación", "Recreación y cultura", "Educación", 
              "Restaurantes y hoteles", "Bienes y servicios varios")

# Modificación del nombre de la primera variable

colnames (ipc_patagonico) [1] <- "nivel"


# Armado de DF

ipc_patagonico <- ipc_patagonico |> 
  filter (nivel %in% niveles) |> 
  mutate (across (!nivel, as.numeric)) |> 
  pivot_longer (!nivel, names_to = "periodo",
                values_to = "ipc_mensual") |> 
  mutate (periodo = as.integer (periodo)) |> 
  mutate (periodo = as.Date (periodo, origin = "1899-12-30"))

# Eliminar vector de niveles (ya usado)

rm (niveles)

# Armado de DF de nivel general

ipc_patagonico_nivel_gral <- ipc_patagonico |> 
  filter (nivel == "Nivel general")

# Exportación a CSV

write_csv(ipc_patagonico, "ipc_patagonico.csv")
write_csv(ipc_patagonico_nivel_gral, "ipc_patagonico_nivel_general.csv")

print ("Se generaron los dos archivos de IPC Patagónico. 
       Uno incluyendo todos los niveles y el otro solo nivel general")
