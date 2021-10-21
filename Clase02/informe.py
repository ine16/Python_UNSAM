# informe.py

import csv

def leer_camion(nombre_archivo):
    '''Abre y lee un archivo con el contenido de un camión. Devuelve la información como una lista de tuplas/diccionarios'''
    camion = []

    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                #lote = (row[0], int(row[1]), float(row[2])) #ejercicio 2.15
                lote = {'nombre': row[0], 'cajones': int(row[1]), 'precio': float(row[2])} #ejercicio 2.16
                camion.append(lote)
            except ValueError:
                print('Faltan datos en una línea, no se tendrá en cuenta\n')
    return camion


def leer_precios(nombre_archivo):
    '''A partir de un archivo dado como parámetro, arma un diccionario en el cual las claves son
    los nombres de frutas y verduras y los valores son los precios por cajón'''
    dicc_precios = {}
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        for row in rows:
            try:
                fruta = str(row[0])
                precio = float(row[1])
                dicc_precios[fruta] = precio
            except IndexError:
                print('Faltan datos en una línea, no se tendrá en cuenta\n')
    return dicc_precios

def balance_negocio(archivo_camion, archivo_precios):
    '''Calcula diferencia entre ingresos (usando archivo de precios) y gastos (usando archivo del camion)'''
    gastos = 0
    ingresos = 0
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)
    for s in camion:
        gastos += s['cajones'] * s['precio']
        ingresos += precios[s['nombre']] * s['cajones']
    balance = ingresos - gastos
    print(f'Costo camión: ${gastos:0.2f}')
    print(f'Ingresos ventas: ${ingresos:0.2f}')
    print(f'Balance total: ${balance:0.2f}')
    return balance

# balance = balance_negocio('../Data/camion.csv', '../Data/precios.csv')

#============== 
# SALIDA DEL EJERCICIO 2.18 (balance del negocio)
#
# PS C:\Users\Ine\Desktop\Doctorado\ejercicios_python\Clase02> python informe.py
# Faltan datos en una línea, no se tendrá en cuenta

# Costo camión: $47671.15
# Ingresos ventas: $62986.10
# Balance total: $15314.95
#
#============== 
# SALIDA DEL EJERCICIO 2.17
#
# PS C:\Users\Ine\Desktop\Doctorado\ejercicios_python\Clase02> python -i informe.py
# >>> precios = leer_precios('../Data/precios.csv')
# Warning: Línea con datos faltantes, no se tendrá en cuenta
# >>> precios['Naranja']
# 106.28
# >>> precios['Ajo']
# 15.19
#
#============== 
# SALIDA DEL EJERCICIO 2.16
#
# PS C:\Users\Ine\Desktop\Doctorado\ejercicios_python\Clase02> python -i informe.py
# >>> camion = leer_camion('../Data/camion.csv')
# >>> camion
# [{'nombre': 'Lima', 'cajones': 100, 'precio': 32.2}, {'nombre': 'Naranja', 'cajones': 50, 'precio': 91.1}, {'nombre': 'Caqui', 'cajones': 150, 'precio': 103.44}, {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}, {'nombre': 'Durazno', 'cajones': 95, 'precio': 40.37}, {'nombre': 'Mandarina', 'cajones': 50, 'precio': 65.1}, {'nombre': 'Naranja', 'cajones': 100, 'precio': 70.44}]
# >>> camion[0]['cajones']
# 100
# >>> camion[3]
# {'nombre': 'Mandarina', 'cajones': 200, 'precio': 51.23}
# >>> total = 0.0
# >>> for s in camion:
# ...     total += s['cajones']*s['precio']
# ...
# >>> print(total)
# 47671.15
# >>> from pprint import pprint
# >>> pprint(camion)
# [{'cajones': 100, 'nombre': 'Lima', 'precio': 32.2},
#  {'cajones': 50, 'nombre': 'Naranja', 'precio': 91.1},
#  {'cajones': 150, 'nombre': 'Caqui', 'precio': 103.44},
#  {'cajones': 200, 'nombre': 'Mandarina', 'precio': 51.23},
#  {'cajones': 95, 'nombre': 'Durazno', 'precio': 40.37},
#  {'cajones': 50, 'nombre': 'Mandarina', 'precio': 65.1},
#  {'cajones': 100, 'nombre': 'Naranja', 'precio': 70.44}]
#
#============== 
# SALIDA DEL EJERCICIO 2.15
#
# PS C:\Users\Ine\Desktop\Doctorado\ejercicios_python\Clase02> python -i informe.py
# >>> camion = leer_camion('../Data/camion.csv')
# >>> camion
# [('Lima', 100, 32.2), ('Naranja', 50, 91.1), ('Caqui', 150, 103.44), ('Mandarina', 200, 51.23), ('Durazno', 95, 40.37), ('Mandarina', 50, 65.1), ('Naranja', 100, 70.44)]
# >>> camion[0]
# ('Lima', 100, 32.2)
# >>> camion[2][2]
# 103.44
# >>> total = 0.0
# >>> for s in camion:
# ...     total += s[1] * s[2]
# ...
# >>> print(total)
# 47671.15