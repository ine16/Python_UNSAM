# arboles.py (Clase 4)
import csv


#==============
# Ejercicio 4.15

def leer_arboles(nombre_archivo):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        filas = csv.reader(f)
        encabezados = next(filas)
        lista_arboles = [dict(zip(encabezados, fila)) for fila in filas]
    return lista_arboles


#==============
# Ejercicio 4.18

def medidas_de_especies(especies,arboleda):
    # la columna 'altura_tot' contiene la altura de cada árbol del archivo
    diccionario_especies = { especie: [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie] for especie in especies }
    return diccionario_especies


#==============
# Ejercicios 4.16, 4.17 y parte del 4.18

if __name__=="__main__":
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    
    # Para el 4.16
    print('Para ver la lista de alturas del ejercicio 4.16 en modo interactivo, llamá a H_Jacarandas\n')
    H_Jacarandas = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']

    # Para el 4.17
    print('Para ver la lista de alturas y diámetros del ejercicio 4.17 en modo interactivo, llamá a alt_y_diam\n')
    alt_y_diam = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    
    # Para el 4.18
    print('A modo de control para el 4.18:')
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    diccionario = medidas_de_especies(especies,arboleda)
    num_eucaliptos = len(diccionario['Eucalipto'])
    num_palos = len(diccionario['Palo borracho rosado'])
    num_jacarandas = len(diccionario['Jacarandá'])
    print(f'Hay {num_eucaliptos} eucaliptos, {num_palos} palos borrachos rosados y {num_jacarandas} jacarandás')