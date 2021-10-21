# camion_commandline.py

import csv
import sys

def costo_camion(nombre_archivo):
    'Se ingresa el nombre del archivo (incluyendo la extension) como string. Busca archivos en la carpeta Data'
    f = open('C:/Users/Ine/Desktop/Doctorado/ejercicios_python/Data/'+nombre_archivo, 'rt', encoding='utf8')
    rows = csv.reader(f)
    headers = next(rows)
    costo_total = 0
    for row in rows:
        try:
            costo_total += int(row[1])*float(row[2])
        except ValueError:
            print('Warning: Línea con datos faltantes, no se tendrá en cuenta')
            continue
    f.close()
    return costo_total


if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = 'camion.csv'

costo = costo_camion(nombre_archivo)
print('Costo total:', costo)


# CORRIDAS DEL SCRIPT DESDE LINEA DE COMANDOS, PASANDO DISTINTOS ARCHIVOS COMO ARGUMENTO:
# PS C:\Users\Ine\Desktop\Doctorado\ejercicios_python\Clase02> python camion_commandline.py camion.csv
# Costo total: 47671.15
# PS C:\Users\Ine\Desktop\Doctorado\ejercicios_python\Clase02> python camion_commandline.py missing.csv
# Warning: Línea con datos faltantes, no se tendrá en cuenta
# Warning: Línea con datos faltantes, no se tendrá en cuenta
# Costo total: 30381.15
# PS C:\Users\Ine\Desktop\Doctorado\ejercicios_python\Clase02> python camion_commandline.py
# Costo total: 47671.15