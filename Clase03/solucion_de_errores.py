#solucion_de_errores.py

#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de tipo semántico y estaba ubicado en la línea 8. El código tal como estaba sólo decía
#si el primer caracter era una "a", ya que devolvía False si esto no ocurría y salía de la función
#    Lo corregí sacando el "return False" del while
#    A continuación va el código corregido

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
        	return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: Los errores son de tipo sintácticos y estaban ubicados en las líneas 1, 4, 5 y 8.
#    En las líneas 1 y 4: agregué ":" al final
#    En la línea 5: como "=" corresponde a una asignación lo cambíe por "==", y agregué ":" al final
#    En la línea 8: "Falso" no es una palabra reservada en Python, queremos que devuelva el booleano falso ("False")

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a':
            return True
        i += 1
    return False

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de tiempo de ejecución y estaba ubicado en la línea 14 (la que le pasa a "tiene_uno"
#un entero como argumento).
#    Entiendo que el objetivo del código es indicar si una cadena de caracteres tiene un 1. Si es asi, se me ocurren
#2 posibles soluciones: o bien usar str() para forzar que la entrada sea un string o bien tratarlo como una excepción
#y pedir que el usuario reingrese el valor pero como cadena de caracteres. Implementé la segunda opción

def tiene_uno(expresion):
    tiene = False
    try:
        n = len(expresion)
        i = 0
        while (i<n) and not tiene:
            if expresion[i] == '1':
                tiene = True
            i += 1
        return tiene
    except TypeError:
        print(f'Error al ingresar {expresion}. Por favor ingresá una cadena de caracteres: ')
        entrada_usuario = input()
        reintento = tiene_uno(entrada_usuario)
        return reintento


tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)

#%%
#Ejercicio 3.4. Función suma()
#Comentario: El error era de tipo semántico y estaba "ubicado" en la línea 3 (o más bien, el problema era que no había nada en dicha línea).
#No poner nada al final de la función equivale a poner "return" solo y devuelve una variable de tipo None
#     Lo corregí pidiendo que la función devuelva c (es decir, el resultado de sumar a con b)

def suma(a,b):
    c = a + b
    return c

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.5. Función leer_camion()
#Comentario: Como se define registro={} fuera del for (en la línea 3), en cada iteración se actualizan los elementos
#del mismo. La lista "camion" posee como elementos al diccionario "registro", con lo que terminamos modificando en 
#consecuencia los elementos de "camion" en cada iteración. Un forma de evitar esto es creando el diccionario
#"registro" en cada iteración para que se le asigne un nuevo lugar de memoria cada vez y no "pise" lo anterior
#    Lo corregí definiendo "registro" en la línea 10 como primera instrucción a ejecutar en el for

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
        	registro={}
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)