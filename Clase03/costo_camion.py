# costo_camion.py

import csv

def costo_camion(nombre_archivo):
    f = open(nombre_archivo, encoding='utf8')
    filas = csv.reader(f)
    encabezados = next(filas)
    costo_total = 0
    for n_fila, fila in enumerate(filas, start=1):
        record = dict(zip(encabezados, fila))
        try:
            ncajones = int(record['cajones'])
            precio = float(record['precio'])
            costo_total += ncajones * precio
        except ValueError:
            print(f'Fila {n_fila}: No pude interpretar: {fila}')
            continue
    f.close()
    return costo_total

#===============
# SALIDAS AL CORRER LA FUNCION DE FORMA INTERACTIVA
# >>> costo_camion('../Data/fecha_camion.csv')
# 47671.15
# >>> costo_camion('../Data/camion.csv')
# 47671.15
# >>> costo_camion('../Data/missing.csv')
# Fila 4: No pude interpretar: ['Mandarina', '', '51.23']
# Fila 7: No pude interpretar: ['Naranja', '', '70.44']
# 30381.15