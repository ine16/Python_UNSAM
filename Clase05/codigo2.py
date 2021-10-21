#figuritas.py
import random
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total):
    return np.zeros(figus_total)

def album_incompleto(A):
    if 0 in A:
        return True
    return False

def comprar_figu(figus_total):
    return random.randint(0,figus_total)

def cuantas_figus(figus_total):
    albumNUEVO = crear_album(figus_total)
    cantidadFIGUScompradas = 0
    while album_incompleto(albumNUEVO) == True:
        figurita = comprar_figu(figus_total-1)
        albumNUEVO[figurita] = 1
        cantidadFIGUScompradas +=1
    return cantidadFIGUScompradas

def experimento_figus(n_repeticiones, figus_total):
    veces = []
    for i in range(n_repeticiones):
        veces.append(cuantas_figus(figus_total)) 
    prob = np.mean(veces)
    return prob

def comprar_paquete(figus_total,figus_paquete):
    paquete = []
    for i in range(figus_paquete):
        paquete.append(random.randint(0,figus_total-1))
    return paquete

def cuantos_paquetes(figus_total,figus_paquete):
    albumNUEVO = crear_album(figus_total)
    cantPAQUETES = 0
    while album_incompleto(albumNUEVO) == True:
        paquete = comprar_paquete(figus_total,figus_paquete)
        for figu in paquete:
            albumNUEVO[figu] = 1
        cantPAQUETES +=1
    return cantPAQUETES

def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)
    historia_figus_pegadas = [0]
    while album_incompleto(album):
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

def ejercicio520():
    figus_total = 670
    figus_paquete = 5
    n = 100
    lista = []

    for i in range(n):
        lista.append(cuantos_paquetes(figus_total,figus_paquete))

    n_paquetes_hasta_llenar=np.array(lista)
    
    prob = (n_paquetes_hasta_llenar <= 850).sum() / n
    
    print(f'La probabilidad de completar el album con 850 paquetes es de {prob}')
        
def ejercicio521():
    figus_total = 670
    figus_paquete = 5
    n = 100
    lista = []

    for i in range(n):
        lista.append(cuantos_paquetes(figus_total,figus_paquete))
    
    print(lista)
    plt.hist(lista,bins=100)
    plt.show()
    
def ejercicio522():
    figus_total = 670
    figus_paquete = 5
    album = crear_album(figus_total)
    figus_pegadas = 0
    cant_paquetes = 0
    while figus_pegadas < 600:
        paquete = comprar_paquete(figus_total, figus_paquete)
        cant_paquetes+=1
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()
        
    print(f'Habia que comprar {cant_paquetes} para completar el 90%')

def comprar_paquete_sin_repetir(figus_total,figus_paquete):
    opciones = [i for i in range(figus_total)]
    paquete = random.sample(opciones,k=5)
    return paquete
            
def ejercicio523():
    figus_total = 670
    figus_paquete = 5
    album = crear_album(figus_total)
    figus_pegadas = 0
    cant_paquetes = 0
    while figus_pegadas < 600:
        paquete = comprar_paquete_sin_repetir(figus_total, figus_paquete)
        cant_paquetes+=1
        while paquete:
            album[paquete.pop()] = 1
        figus_pegadas = (album>0).sum()     
    print(f'Habia que comprar {cant_paquetes} con figuritas sin repetir para completar el 90%')