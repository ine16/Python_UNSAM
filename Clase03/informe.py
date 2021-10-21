# informe.py

import csv

def leer_camion(nombre_archivo):
    '''Abre y lee un archivo con el contenido de un camión. Devuelve la información como una lista de tuplas/diccionarios'''
    camion = []

    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        for n_fila, fila in enumerate(filas, start=1):
            registro = dict(zip(encabezados, fila))
            try:
                lote = {'nombre': registro['nombre'], 'cajones': int(registro['cajones']), 'precio': float(registro['precio'])}
                camion.append(lote)
            except ValueError:
                print(f'Fila {n_fila}: No pude interpretar: {fila}\n')
    return camion


def leer_precios(nombre_archivo):
    '''A partir de un archivo dado como parámetro, arma un diccionario en el cual las claves son
    los nombres de frutas y verduras y los valores son los precios por cajón'''
    dicc_precios = {}
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        for n_row, row in enumerate(rows, start=1):
            try:
                fruta = str(row[0])
                precio = float(row[1])
                dicc_precios[fruta] = precio
            except IndexError:
                print(f'Fila {n_row}: No pude interpretar: {row}\n')
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


# Probá correr el programa informe.py sobre el archivo Data/fecha_camion.csv y fijate si da la misma salida que antes
def ejercicio_3_9():
    balance = balance_negocio('../Data/fecha_camion.csv', '../Data/precios.csv')

#============== 
# SALIDA DEL EJERCICIO CON REPL (llamando a ejercicio_3_9)
#
# Fila 31: No pude interpretar: []
#
# Costo camión: $47671.15
# Ingresos ventas: $62986.10
# Balance total: $15314.95