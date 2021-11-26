# ticker.py

from vigilante import vigilar
import csv
from formato_tabla import crear_formateador
import informe_final


def cambiar_tipo(rows, types):
    # for row in rows:
    #     yield [func(val) for func, val in zip(types, row)]
    con_tipos_nuevos = ((func(val) for func, val in zip(types, row)) for row in rows)
    return con_tipos_nuevos

def hace_dicts(rows, headers):
    for row in rows:
        yield dict(zip(headers, row))

def elegir_columnas(rows, indices):
    # for row in rows:
    #     yield [row[index] for index in indices]
    columnas = ((row[index] for index in indices) for row in rows)
    return columnas

def parsear_datos(lines):
    rows = csv.reader(lines)
    rows = elegir_columnas(rows, [0, 1, 2])
    rows = cambiar_tipo(rows, [str, float, int])
    rows = hace_dicts(rows, ['nombre', 'precio', 'volumen'])
    return rows

def filtrar_datos(rows, nombres):
    filas = (row for row in rows if row['nombre'] in nombres)
    return filas


def ticker(camion_file, log_file, fmt):
    '''
    Crea un indicador en tiempo real para un camión (camion_file),
    archivo log (log_file) y un dado formato de tabla de salida (fmt)

    Opciones para "fmt": 'txt', 'csv', 'html'

    '''
    camion = informe_final.leer_camion(camion_file)
    formateador = crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])

    rows = parsear_datos(vigilar(log_file))
    rows = filtrar_datos(rows, camion)
    for row in rows:
        nombre = row['nombre']
        precio = row['precio']
        volumen = row['volumen']
        rowdata = [nombre, f'{precio:0.2f}', f'{volumen:d}']
        formateador.fila(rowdata)

if __name__ == '__main__':
    lines = vigilar('../Data/mercadolog.csv')
    rows = parsear_datos(lines)
    for row in rows:
        print(row)
