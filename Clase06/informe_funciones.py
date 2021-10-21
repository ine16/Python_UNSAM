# informe_funciones.py

from fileparse import parse_csv

def leer_camion(nombre_archivo):
    '''Abre y lee un archivo con el contenido de un camión. Devuelve una lista de diccionarios'''
    camion = parse_csv(nombre_archivo, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    return camion


def leer_precios(nombre_archivo):
    '''A partir de un archivo dado como parámetro, arma un diccionario en el cual las claves son
    los nombres de frutas y verduras y los valores son los precios por cajón'''
    tuplas_precios = parse_csv(nombre_archivo, types = [str, float], has_headers = False)
    dicc_precios = dict(tuplas_precios)
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

def imprimir_informe(informe):
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    print('%10s %10s %10s %10s'  % headers)
    print(('-' * 10 + ' ') * len(headers))
    for nombre, cajones, precio, cambio in informe:
        precio_con_formato = f'${precio:.2f}'
        print(f'{nombre:>10s} {cajones:>10d} {precio_con_formato:>10s} {cambio:>10.2f}')


def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    precios = leer_precios(nombre_archivo_precios)
    informe = hacer_informe(camion, precios)
    imprimir_informe(informe)

# informe_camion('../Data/camion.csv', '../Data/precios.csv')