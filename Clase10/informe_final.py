# informe_funciones.py

from fileparse import parse_csv
from lote import Lote
import formato_tabla
from camion import Camion


def leer_camion(nombre_archivo):
    '''Abre y lee un archivo con el contenido de un camión. Devuelve una lista de diccionarios'''
    with open(nombre_archivo, 'rt', encoding = 'utf8') as filas:
        camion_dicts = parse_csv(filas, select = ['nombre', 'cajones', 'precio'], types = [str, int, float])
    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camion_dicts]
    return Camion(camion)


def leer_precios(nombre_archivo):
    '''A partir de un archivo dado como parámetro, arma un diccionario en el cual las claves son
    los nombres de frutas y verduras y los valores son los precios por cajón'''
    with open(nombre_archivo, 'rt', encoding='utf8') as filas:
        tuplas_precios = parse_csv(filas, types = [str, float], has_headers = False)
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
        gastos += s.costo()
        ingresos += precios[s.nombre] * s.cajones
    balance = ingresos - gastos
    print(f'Costo camión: ${gastos:0.2f}')
    print(f'Ingresos ventas: ${ingresos:0.2f}')
    print(f'Balance total: ${balance:0.2f}')
    return balance


def hacer_informe(lista_camion, dicc_precios):
    lista_informe = []
    for item in lista_camion:
        nombre_item = item.nombre
        n_cajones = item.cajones
        precio = item.precio
        cambio = dicc_precios[nombre_item] - precio
        tupla_item = (nombre_item, n_cajones, precio, cambio)
        lista_informe.append(tupla_item)
    return lista_informe


def imprimir_informe(data_informe, formateador):
    '''
    Imprime una tabla prolija desde una lista de tuplas
    con (nombre, cajones, precio, diferencia) 
    '''
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}']
        formateador.fila(rowdata)


def informe_camion(archivo_camion, archivo_precios, fmt = 'txt'):
    '''
    Crea un informe con la carga de un camión
    a partir de archivos camion y precio.
    El formato predeterminado de la salida es .txt
    Alternativas: .csv o .html

    Opciones para "fmt": 'txt', 'csv', 'html'
    '''
    # Lee archivos de datos
    camion = leer_camion(archivo_camion)
    precios = leer_precios(archivo_precios)

    # Crea la data del informe
    data_informe = hacer_informe(camion, precios)

    # Imprime el informe
    formateador = formato_tabla.crear_formateador(fmt)
    imprimir_informe(data_informe, formateador)


# informe_camion('../Data/camion.csv', '../Data/precios.csv')

def f_principal(parametros):
    nombre_archivo_camion = parametros[1]
    nombre_archivo_precios = parametros[2]

    # El parámetro que indica el formato de salida de la tabla es opcional, entonces
    #     separamos el caso con 4 parámetros (indicando formato) del de 3 ('txt' por defecto)
    if len(parametros) == 4:
        formato_salida = parametros[3]
        informe_camion(nombre_archivo_camion, nombre_archivo_precios, formato_salida)
    else:
        informe_camion(nombre_archivo_camion, nombre_archivo_precios)


if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} archivo_camion archivo_precios (opcional: formato_salida)')
    f_principal(sys.argv)