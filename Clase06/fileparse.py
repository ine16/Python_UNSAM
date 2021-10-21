# fileparse.py
import csv

def parse_csv(nombre_archivo, select = None, types = None, has_headers = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo, encoding='utf8') as f:
        filas = csv.reader(f)

        
        if has_headers:
            # Lee los encabezados del archivo
            encabezados = next(filas)

        # Si se indicó un selector de columnas,
        #    buscar los índices de las columnas especificadas.
        # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select and has_headers:
            # Convierte los nombres de las columnas listadas en select a índices
            #    (posiciones) de columnas en el archivo.
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for fila in filas:
            if not fila:    # Saltea filas vacías
                continue
            # Filtra la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices]

            if types:
                fila = [func(val) for func, val in zip(types, fila) ]
            # Arma el diccionario
            if has_headers:
                registro = dict(zip(encabezados, fila))
            else:
                registro = tuple(fila)
            registros.append(registro)



    return registros

