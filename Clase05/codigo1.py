#%% figuritas.py
'''
Álbum con 670 figuritas.
Cada figurita se imprime en cantidades iguales y se distribuye aleatoriamente.
Cada paquete trae cinco figuritas
'''
import random as rd
import numpy as np
'''
Primera simplificacion:
Iniciamos con álbum vacío y sin haber comprado ninguna figurita.
Compramos figuritas (de a una) hasta llenar el álbum, ie, se repite la acción (el paso) de comprar y pegar figuritas mientras (while) el álbum está incompleto.
Al terminar nos interesa saber cuántas figuritas tuvimos que comprar para llenar el álbum.
'''
def crear_album(figus_total):
    '''Devuelve un álbum/vector vacío con figus_total espacios 
    para pegar figuritas.'''
    return np.zeros(figus_total)

aux=np.array([1,1,1])


def album_incompleto(A):
    '''Recibe un vector A y devuelve True si el álbum A no está completo y 
    False si está completo.'''
    return len(A[A==0])!=0
album_incompleto(aux)    

def comprar_figu(figus_total):
    '''Con el número total de figuritas que tiene el álbum (figus_total) 
    Devuelve entero aleatorio que representa la figurita que nos tocó'''
    return rd.randint(0,figus_total-1)
# %% 5.13
def cuantas_figus(figus_total):
    '''Dado el tamaño del album (figus_total), genera un album nuevo,
    simula el llenado y devuelve la cantidad de figuritas que se debieron
    comprar para completarlo'''
    album = crear_album(figus_total)
    compras=0
    while album_incompleto(album):
        album[comprar_figu(figus_total)]=1
        compras+=1
    return compras    

cuantas_figus(670)    
# %% 5.14
n_repeticiones =1000
compras = [cuantas_figus(figus_total=6) for _ in range(n_repeticiones)]

promedio = np.mean(compras)
print(f'En promedio, para completar el álbum de 6 hay que comprar {promedio} figuritas')

#%% 5.15
def experimento_figus(n_repeticiones, figus_total):
    '''Simula el llenado de n_repeticiones álbums de figus_total figuritas 
    Devuelve el número estimado de figuritas que hay que comprar, en promedio,
    para completar el álbum.'''
    
    compras = [cuantas_figus(figus_total) for _ in range(n_repeticiones)]
    promedio = np.mean(compras)
    print(f'Al realizar {n_repeticiones} experimentos, se estima que en promedio, para completar un álbum de {figus_total} figuritas hacen falta {promedio} compras')

    return promedio

#_=experimento_figus(100,670)
def main():
    # %% 5.18 Paquetes:
    
    def comprar_paquete(figus_total,figus_paquete):
        return np.array([comprar_figu(figus_total) for _ in range(figus_paquete)])
        
    def cuantos_paquetes(figus_total, figus_paquete):
        '''Dado el tamaño del álbum y la cantidad de figus por paquete, 
        genera un álbum nuevo, simule su llenado y devuelve cuántos 
        paquetes se debieron comprar para completarlo.'''
        cnt=0
        album = crear_album(figus_total)
        while album_incompleto(album):
            for elem in comprar_paquete(figus_total,figus_paquete):
                album[elem]=1
            cnt+=1    
        return cnt

    cuantos_paquetes(figus_total=670,figus_paquete=5)
    #%% 5.19 

    n_repeticiones =1000
    compras = np.array([cuantos_paquetes(figus_total=670,figus_paquete=5) for _ in range(n_repeticiones)])

    promedio = np.mean(compras)
    print(f'Al realizar {n_repeticiones} experimentos, se estima que en promedio, para completar un álbum de 670 figuritas hacen se deben comprar {promedio} paquetes')

    #%% 
    import matplotlib.pyplot as plt 
    def calcular_historia_figus_pegadas(figus_total, figus_paquete):
        album = crear_album(figus_total)
        historia_figus_pegadas = [0]
        while album_incompleto(album):
            paquete = comprar_paquete(figus_total, figus_paquete)
            for elem in paquete:
                album[elem]=1
            figus_pegadas = (album>0).sum()
            historia_figus_pegadas.append(figus_pegadas)
        return historia_figus_pegadas

    figus_total = 670
    figus_paquete = 5

    plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
    plt.xlabel("Cantidad de paquetes comprados.")
    plt.ylabel("Cantidad de figuritas pegadas.")
    plt.title("La curva de llenado se desacelera al final")
    plt.show()

    #%% 5.20
    '''Estimar la probabilidad de completar el álbum con 850 paquetes o menos'''

    n_repeticiones =100
    n_paq_completo = np.array([cuantos_paquetes(figus_total=670,figus_paquete=5) for _ in range(n_repeticiones)])

    promedio = np.mean(n_paq_completo)
    print(f'Al realizar {n_repeticiones} experimentos, se estima que en promedio, para completar un álbum de 670 figuritas hacen se deben comprar {promedio} paquetes.\n')

    probabilidad = (n_paq_completo <= 850).sum()/100
    print(f'La probabilidad de completar el album comprando menos de 850 paquetes es {probabilidad:.2f}%')

    # %% 5.21 Histograma
    import matplotlib.pyplot as plt
    plt.hist(n_paq_completo,bins=len(n_paq_completo))
    plt.show() 
    #%% 5.22
    '''Estimar cuántos paquetes habría que comprar para tener 
    una chance del 90% de completar el álbum.'''
    cnt=0
    album = crear_album(figus_total)
    while (len(album[album==1])/len(album))<=0.9:
        for elem in comprar_paquete(figus_total,figus_paquete):
            album[elem]=1
            cnt+=1    
    print(f'Para completar un 90% del album se necesitan alrededor de {cnt} paquetes')
    # %% 5.23
    '''Repetir suponiendo que no hay figuritas repetidas en un paquete. 
    ¿Cuánto cambian las probabilidades?'''
    '''Para laburar sin repeticiones redefino la funcion comprar paquete'''

    def comprar_paquete(figus_total,figus_paquete):
        return np.array(rd.sample(range(figus_total), figus_paquete))




    #5.22_bis
    '''Estimar cuántos paquetes habría que comprar para tener 
    una chance del 90% de completar el álbum.'''
    cnt=0
    album = crear_album(figus_total)
    while (len(album[album==1])/len(album))<=0.9:
        for elem in comprar_paquete(figus_total,figus_paquete):
            album[elem]=1
            cnt+=1    
    print(f'Para completar un 90% del album se necesitan alrededor de {cnt} paquetes')


    # %% 5.24 5.22
    '''Estimar cuántos paquetes habría que comprar para tener 
    una chance del 90% de completar el álbum.'''
    cnt=0
    album = crear_album(figus_total)
    while (len(album[album==1])/len(album))<=0.9:
        for elem in comprar_paquete(figus_total,figus_paquete):
            album[elem]=1
            cnt+=1    
    print(f'Para completar un 90% del album se necesitan alrededor de {cnt} paquetes')