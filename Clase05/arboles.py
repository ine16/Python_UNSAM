# arboles.py (Clase 4)
import csv
import matplotlib.pyplot as plt
import numpy as np
import os


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
# Ejercicio 5.25

def ejercicio_5_25(altos):
    arboleda = leer_arboles('../Data/arbolado-en-espacios-verdes.csv')
    altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    #plt.figure(4)
    plt.hist(altos, bins=30)
    plt.xlabel("Número de árboles")
    plt.ylabel("Alto (m)")
    plt.title("Histograma de las alturas de los Jacarandás")
    plt.show()


#==============
# Ejercicio 5.26

def scatter_hd(lista_de_pares):
    # Convierto la lista de tuplas en un array de 2 ejes
    vector_de_pares = np.array(lista_de_pares)
    h = vector_de_pares[:,0]
    d = vector_de_pares[:,1]
    #plt.figure(3)
    plt.scatter(d,h, alpha=0.3)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandás")
    plt.show()


#==============
# Ejercicio 5.27

def ejercicio_5_27():
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
    arboleda = leer_arboles(nombre_archivo)
    especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
    medidas = medidas_de_especies(especies, arboleda)
    for i, especie in enumerate(especies):
        vector_de_pares = np.array(medidas[especie])
        h = vector_de_pares[:,0]
        d = vector_de_pares[:,1]
        plt.figure(i)
        plt.scatter(d,h, alpha=0.3)
        plt.legend(str(especie))
        plt.xlabel("diametro (cm)")
        plt.ylabel("alto (m)")
        plt.title('Relación diámetro-alto para '+str(especie))
        plt.xlim(-5,310) 
        plt.ylim(-1,55)
    plt.show()


#==============
# Ejecución de ejercicios 5.25, 5.26 y 5.27

if __name__=="__main__":
    # Para el 5.25
    nombre_archivo = os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv') #porque según el OS va barra o barra invertida
    arboleda = leer_arboles(nombre_archivo)
    altos = [float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    ejercicio_5_25(altos)

    # Para el 5.26
    alt_y_diam = [(float(arbol['altura_tot']), float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    scatter_hd(alt_y_diam)

    # Para el 5.27
    ejercicio_5_27()
    # Coloqué el plt.show() al final para que muestre todos los gráficos juntos,
    # sino desde consola se corta la ejecución hasta que no se cierra
    #plt.show()