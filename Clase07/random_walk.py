# random_walk.py

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    '''
    Devuelve de una caminata aleatoria del largo dado (es decir, el número de pasos)

    Pre: "largo" debe ser un entero positivo
    Pos: devuelve un array de NumPy de longitud "largo"
    '''
    pasos = np.random.randint(-1,2,largo)    
    return pasos.cumsum()


def f_principal(num_trayectorias):
    N_pasos = 100000

    fig = plt.figure()

    # Define la figura grande con las 12 caminatas
    plt.subplot(2, 1, 1)
    lista_caminatas = []
    for i in range(num_trayectorias):
        caminata = randomwalk(N_pasos)
        plt.plot(caminata)
        lista_caminatas.append(caminata)
    plt.xlabel("Tiempo")
    plt.ylabel("Distancia al origen")
    plt.ylim(-800, 800)
    plt.title(f"{num_trayectorias: d} caminatas al azar de {N_pasos} pasos de largo")

    
    # Guardamos en una lista lo máximo que se alejó cada caminata del origen. Esto está dado por el
    # valor absoluto porque no importa si va a la izquierda o derecha del origen sino cuanto se aleja
    lista_maximos = [max(abs(caminata)) for caminata in lista_caminatas]


    # Define la gráfica de abajo a la izq
    plt.subplot(2, 2, 3)
    indice_mas_alejada = np.argmax(lista_maximos) # devuelve el índice de la primer aparición del máximo
    caminata_mas_alejada = lista_caminatas[indice_mas_alejada]
    plt.plot(caminata_mas_alejada)
    plt.xlabel("Tiempo")
    plt.ylabel("Distancia al origen")
    plt.ylim(-800, 800)
    plt.title(f"La caminata que más se aleja")


    # Define la gráfica de abajo a la der
    plt.subplot(2, 2, 4) 
    indice_menos_alejada = np.argmin(lista_maximos) # análogo a argmax pero con el mínimo
    caminata_menos_alejada = lista_caminatas[indice_menos_alejada]
    plt.plot(caminata_menos_alejada)
    plt.xlabel("Tiempo")
    plt.ylabel("Distancia al origen")
    plt.ylim(-800, 800)
    plt.title(f"La caminata que menos se aleja")

    plt.show()

#VERSION ARREGLADA, NO HACE FALTA REENTREGAR
# f_principal(12)