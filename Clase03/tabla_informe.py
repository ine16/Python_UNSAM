# informe.py

import csv

def leer_camion(nombre_archivo):
    '''Abre y lee un archivo con el contenido de un camión. Devuelve una lista de diccionarios'''
    camion = []

    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for n_row, row in enumerate(rows, start=1):
            registro = dict(zip(headers, row))
            try:
                lote = {'nombre': registro['nombre'], 'cajones': int(registro['cajones']), 'precio': float(registro['precio'])}
                camion.append(lote)
            except ValueError:
                print(f'Error en fila {n_row} de {nombre_archivo}: No pude interpretar: {row}\n')
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
                print(f'Error en fila {n_row} de {nombre_archivo}: No pude interpretar: {row}\n')
    return dicc_precios

def balance_negocio(archivo_camion, archivo_precios):
    '''Calcula diferencia entre ingresos (para cada línea en archivo_camion calcula cajones*precio, con el precio segun
    archivo_precios, y suma todo) y gastos (usando la info de cada línea de archivo_camion calcula cajones*precio y suma)'''
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

def hacer_informe(lista_camion, dicc_precios):
    lista_informe = []
    for item in lista_camion:
        nombre_item = item['nombre']
        n_cajones = item['cajones']
        precio = item['precio']
        cambio = dicc_precios[nombre_item] - precio
        tupla_item = (nombre_item, n_cajones, precio, cambio)
        lista_informe.append(tupla_item)
    return lista_informe

def ejercicio_3_16():
    camion = leer_camion('../Data/camion.csv')
    precios = leer_precios('../Data/precios.csv')
    informe = hacer_informe(camion, precios)
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

    header_informe = ''
    separador_informe = ''
    separador = '-'*10 + ' ' #defino la "medida base" del separador que va debajo de cada título de columna
    for titulo in headers:
        header_informe += f'{titulo:>10s} '
        separador_informe += separador #por cada elemento en headers (es decir, cada columna) añado un separador "base" abajo
    print(header_informe)
    print(separador_informe)

    for nombre, cajones, precio, cambio in informe:
        precio_con_formato = '$'+str(precio)
        print(f'{nombre:>10s} {cajones:>10d} {precio_con_formato:>10s} {cambio:>10.2f}')



# SALIDA DEL EJERCICIO 3.13
# >>> camion = leer_camion('../Data/camion.csv')
# >>> precios = leer_precios('../Data/precios.csv')
# Error en fila 31 de ../Data/precios.csv: No pude interpretar: []

# >>> informe = hacer_informe(camion, precios)
# >>> for linea in informe:
# ...     print(linea)
# ...
# ('Lima', 100, 32.2, 8.019999999999996)
# ('Naranja', 50, 91.1, 15.180000000000007)
# ('Caqui', 150, 103.44, 2.019999999999996)
# ('Mandarina', 200, 51.23, 29.660000000000004)
# ('Durazno', 95, 40.37, 33.11000000000001)
# ('Mandarina', 50, 65.1, 15.790000000000006)
# ('Naranja', 100, 70.44, 35.84)