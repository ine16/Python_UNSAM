# fileparse.py

import csv


def parse_csv(iterable, select = None, types = None, has_headers = True, silence_errors = False):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''

    if select and not has_headers:
        raise RuntimeError("Para seleccionar, necesito encabezados.")

    
    filas = csv.reader(iterable)

        
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
    for i, fila in enumerate(filas):
        if not fila:    # Saltea filas vacías
            continue
        # Filtra la fila si se especificaron columnas
        if indices:
            fila = [fila[index] for index in indices]

        if types:
            try:
                fila = [func(val) for func, val in zip(types, fila) ]
            except ValueError as e:
                if not silence_errors:
                    print(f"Fila {i}: No pude convertir {fila}")
                    print(f"Fila {i}: Motivo: {e}")
                continue
        # Arma el diccionario
        if has_headers:
            registro = dict(zip(encabezados, fila))
        else:
            registro = tuple(fila)
        registros.append(registro)

    return registros