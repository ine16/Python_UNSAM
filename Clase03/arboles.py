# arboles.py
import csv
from collections import Counter


#==============
# Ejercicio 3.18

def leer_parque(nombre_archivo, parque):
    with open(nombre_archivo, 'rt', encoding='utf8') as f:
        parque = parque.upper() 
        filas = csv.reader(f)
        encabezados = next(filas)
        lista_arboles = []
        for n_fila, fila in enumerate(filas, start=1):
            record = dict(zip(encabezados, fila))
            
            #los nombres de los parques mezclan mayus y minus a veces, entonces pongo el .lower() para que no haga problemas
            if record['espacio_ve'].lower() == parque.lower():
                
                #no lo dice el enunciado, pero voy a dejar en el dicc los datos sobre el árbol no relacionados al parque
                del record['espacio_ve'] #saco el nombre del parque del diccionario
                del record['ubicacion'] #saco la dirección del parque del diccionario
                lista_arboles.append(record)
        
        return lista_arboles

def ejercicio_3_18():
    print('EJERCICIO 3.18')
    parque_elegido = 'GENERAL PAZ'
    arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque_elegido)
    print(f'Número de árboles en el parque "{parque_elegido.lower()}": {len(arboles)}')


#==============
# Ejercicio 3.19

def especies(lista_arboles):
    especies = []
    for arbol in lista_arboles:
        especie = arbol['nombre_com']
        especies.append(especie)
    especies = set(especies)
    return especies

# A modo de chequeo para comparar despues:
#print(f'Número de especies en el parque "{parque_elegido.lower()}": {len(especies(arboles))}\n')


#==============
# Ejercicio 3.20

def contar_ejemplares(lista_arboles):
    ejemplares_especie = Counter()
    for ejemplares in lista_arboles:
        ejemplares_especie[ejemplares['nombre_com']] += 1
    return ejemplares_especie


#Pido que imprima esto como primer chequeo para ver si coincide con el de especies(arboles):
#print(f'Número de especies en el parque "{parque_elegido.lower()}": {len(num_ejemplares_parque)}\n')


# la lista con los parques a usar del 3.20 en adelante
lista_parques = ['GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO']

def ejercicio_3_20():
    print('EJERCICIO 3.20')
    for parque in lista_parques:
        lista_arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque)
        ejemplares = contar_ejemplares(lista_arboles)
        top5_ejemplares = ejemplares.most_common(5)
        print(f'Nombre del parque: {parque}')
        print(top5_ejemplares)
        print('\n')
    print('\n')


#==============
# Ejercicio 3.21

def obtener_alturas(lista_arboles, especie):
    lista_alturas = []
    for arbol in lista_arboles:
        if arbol['nombre_com'].lower() == especie.lower():
            lista_alturas.append(float(arbol['altura_tot']))
    print(f'Altura máxima de la especie {especie}: {max(lista_alturas):.2f}')
    altura_prom = sum(lista_alturas) / len(lista_alturas)
    print(f'Altura promedio de la especie {especie}: {altura_prom:.2f}')
    return

def ejercicio_3_21():
    print('EJERCICIO 3.21')
    for parque in lista_parques:
        lista_arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque)
        especie_buscada = 'Jacarandá'
        print(f'Nombre del parque: {parque}')
        obtener_alturas(lista_arboles, especie_buscada)
        print('\n')
    print('\n')


#==============
# Ejercicio 3.22

def obtener_inclinaciones(lista_arboles, especie):
    lista_inclinaciones = []
    for arbol in lista_arboles:
        if arbol['nombre_com'].lower() == especie.lower():
            lista_inclinaciones.append(float(arbol['inclinacio']))
    return lista_inclinaciones


#==============
# Ejercicio 3.23


def especimen_mas_inclinado(lista_arboles):
    dicc_especie_inclinacion = {}
    conjunto_especies = especies(lista_arboles)

    for especie in conjunto_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        inclinacion_maxima = max(inclinaciones)
        dicc_especie_inclinacion[especie] = inclinacion_maxima

    # Conseguimos la clave del dicc que tiene el máximo valor (sacado de https://www.kite.com/python/answers/how-to-find-the-max-value-in-a-dictionary-in-python)
    especie_mas_inclinada = max(dicc_especie_inclinacion, key=dicc_especie_inclinacion.get)
    
    return (especie_mas_inclinada, dicc_especie_inclinacion[especie_mas_inclinada])


def ejercicio_3_23():
    print('EJERCICIO 3.23')
    for parque in lista_parques:
        lista_arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque)
        print(f'Nombre del parque: {parque}')
        mas_inclinada, inclinacion = especimen_mas_inclinado(lista_arboles)
        print(f'Especie más inclinada: {mas_inclinada}')
        print(f'Inclinación: {inclinacion}')
        print('\n')
    print('\n')


#==============
# Ejercicio 3.24

def especie_promedio_mas_inclinada(lista_arboles):
    dicc_especie_inclinacion_prom = {}
    conjunto_especies = especies(lista_arboles)

    for especie in conjunto_especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, especie)
        inclinacion_promedio = sum(inclinaciones) / len(inclinaciones)
        dicc_especie_inclinacion_prom[especie] = inclinacion_promedio

    especie_mas_inclinada_prom = max(dicc_especie_inclinacion_prom, key=dicc_especie_inclinacion_prom.get)

    return (especie_mas_inclinada_prom, dicc_especie_inclinacion_prom[especie_mas_inclinada_prom])


def ejercicio_3_24():
    print('EJERCICIO 3.24')
    for parque in lista_parques:
        lista_arboles = leer_parque('../Data/arbolado-en-espacios-verdes.csv', parque)
        print(f'Nombre del parque: {parque}')
        mas_inclinada_prom, inclinacion_prom = especie_promedio_mas_inclinada(lista_arboles)
        print(f'Especie más inclinada en promedio: {mas_inclinada_prom}')
        print(f'Inclinación: {inclinacion_prom}')
        print('\n')
    print('\n')



#--SALIDA DEL CÓDIGO QUE RESPONDE LOS EJERCICIOS--

# >>> ejercicio_3_18()
# EJERCICIO 3.18
# Número de árboles en el parque "general paz": 690
# >>> ejercicio_3_20()
# EJERCICIO 3.20
# Nombre del parque: GENERAL PAZ
# [('Casuarina', 97), ('Tipa blanca', 54), ('Eucalipto', 49), ('Palo borracho rosado', 44), ('Fenix', 40)]


# Nombre del parque: ANDES, LOS
# [('Jacarandá', 117), ('Tipa blanca', 28), ('Ciprés', 21), ('Palo borracho rosado', 18), ('Lapacho', 12)]


# Nombre del parque: CENTENARIO
# [('Plátano', 137), ('Jacarandá', 45), ('Tipa blanca', 42), ('Palo borracho rosado', 41), ('Fresno americano', 38)]




# >>> ejercicio_3_21()
# EJERCICIO 3.21
# Nombre del parque: GENERAL PAZ
# Altura máxima de la especie Jacarandá: 16.00
# Altura promedio de la especie Jacarandá: 10.20


# Nombre del parque: ANDES, LOS
# Altura máxima de la especie Jacarandá: 25.00
# Altura promedio de la especie Jacarandá: 10.54


# Nombre del parque: CENTENARIO
# Altura máxima de la especie Jacarandá: 18.00
# Altura promedio de la especie Jacarandá: 8.96




# >>> ejercicio_3_22()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'ejercicio_3_22' is not defined
# >>> ejercicio_3_23()
# EJERCICIO 3.23
# Nombre del parque: GENERAL PAZ
# Especie más inclinada: Macrocarpa (Ciprés de Monterrey o Ciprés de Lambert)
# Inclinación: 70.0


# Nombre del parque: ANDES, LOS
# Especie más inclinada: Jacarandá
# Inclinación: 30.0


# Nombre del parque: CENTENARIO
# Especie más inclinada: Falso Guayabo (Guayaba del Brasil)
# Inclinación: 80.0




# >>> ejercicio_3_24()
# EJERCICIO 3.24
# Nombre del parque: GENERAL PAZ
# Especie más inclinada en promedio: No Determinable
# Inclinación: 25.0


# Nombre del parque: ANDES, LOS
# Especie más inclinada en promedio: Álamo plateado
# Inclinación: 25.0


# Nombre del parque: CENTENARIO
# Especie más inclinada en promedio: Rosa de Siria
# Inclinación: 25.0