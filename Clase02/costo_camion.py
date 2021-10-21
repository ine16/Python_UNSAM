# costo_camion.py

# Ejercicios 2.8 y 2.9 juntos
import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo, encoding='utf8')
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

costo = costo_camion('C:/Users/Ine/Desktop/Doctorado/ejercicios_python/Data/camion.csv')
print('Costo total:', costo)

#===============
# SALIDAS AL CORRER LA FUNCION DE FORMA INTERACTIVA
# PS C:\Users\Ine\Desktop\Doctorado\ejercicios_python\Clase02> python -i costo_camion.py
# Costo total: 47671.15
# >>> costo_camion('C:/Users/Ine/Desktop/Doctorado/ejercicios_python/Data/missing.csv')
# Warning: Línea con datos faltantes, no se tendrá en cuenta
# Warning: Línea con datos faltantes, no se tendrá en cuenta
# 30381.15
#
#===============
#
# Ejercicio 2.6
#
# def costo_camion(nombre_archivo):
#     f = open(nombre_archivo, 'rt', encoding='utf8')
#     headers = next(f)
#     costo_total = 0
#     for line in f:
#         row = line.split(',')
#         costo_total += int(row[1])*float(row[2])
#     f.close()
#     return costo_total
# costo = costo_camion('C:/Users/Ine/Desktop/Doctorado/ejercicios_python/Data/camion.csv')
# print('Costo total:', costo)
#
#===============
#
# Ejercicio 2.2
#
# f = open('C:/Users/Ine/Desktop/Doctorado/ejercicios_python/Data/camion.csv', 'rt', encoding='utf8')
# headers = next(f)
# costo_total = 0
# for line in f:
#     row = line.split(',')
#     costo_total += int(row[1])*float(row[2])
# f.close()
# print("Costo total", costo_total)