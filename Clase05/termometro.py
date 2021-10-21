import random
import numpy as np

def medir_temp(n):
    lista_medidas = [round(37.5 + random.normalvariate(0,0.2), 2) for i in range(n)]
    np.save('../Data/vector_temps', np.array(lista_medidas))
    return lista_medidas


def resumen_temp(n):
    '''
    Realiza una simulación de n temperaturas y devuelve una tupla con el valor máximo,
    el mínimo, el promedio y la mediana (en ese orden) de estas n mediciones.
    '''
    temperaturas_simulacion = medir_temp(n)
    print(temperaturas_simulacion)
    maximo = max(temperaturas_simulacion)
    minimo = min(temperaturas_simulacion)
    promedio = sum(temperaturas_simulacion) / n
    temperaturas_simulacion.sort()
    if n%2 == 0:
        mediana = (temperaturas_simulacion[int(n/2)] + temperaturas_simulacion[int(n/2) - 1]) / 2
    else:
        mediana = temperaturas_simulacion[int(n/2)]
    return (maximo, minimo, round(promedio, 2), mediana)

def ejercicio_5_8():
    medir_temp(999)