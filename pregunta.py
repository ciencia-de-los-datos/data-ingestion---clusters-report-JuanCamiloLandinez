"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

import re

#Depuración
def depurar(line):
    
    primer=r"^(\d+)\s+(\d+)\s+(\d+)([,.])(\d+)([ ,.%]+)(.+)"
    segundo = r"\s{2,5}"
    d = re.search(primer, line)
    line = d.group(1) + ';' + d.group(2) + ';' + d.group(3) + '.' + d.group(5) + ';' + d.group(7)
    line = re.sub(segundo, ' ', line)
    return line

def ingest_data():
    with open('clusters_report.txt', 'r') as file:
        dataset = file.readlines()
    texto = dataset[:2]
    data = dataset[4:]
    data = [line.replace('\n', "") for line in data]
    data = [line.strip() for line in data]  

    list_1 = []
    i = 0
    line = ""
    while i< len(data):
        if data[i] != "":
            line = line +' '+ data[i]
        else:
            list_1.append(line)
            line = ""
        i += 1
    data = [line.strip() for line in list_1]    
    
    data = list(map(depurar, data))
    data = [text.split(';') for text in data]
    data = [[int(i[0]), int(i[1]), float(i[2]), i[3].replace('.', '')] for i in data]
    
    texto = [line.replace('\n', "") for line in texto]
    texto = [line.lower() for line in texto]
    texto = [line.strip() for line in texto]  
    patron = r"\s{2,5}"
    texto = [re.sub(patron, ';', line) for line in texto]
    texto = '; '.join(texto)
    texto = texto.split(';') 
    texto = [texto[0], texto[1] + texto[4], texto[2] +" "+ texto[5], texto[3]]
    texto = [line.replace(' ', '_') for line in texto]

    df = pd.DataFrame(data, columns = texto)
    return df
