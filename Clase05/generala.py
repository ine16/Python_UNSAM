import random
from collections import Counter

# Ejercicio 5.1

def tirar(num_dados=5):
    '''
    Devuelve una lista de resultados al tirar num_dados dados. Por defecto se usan 5 dados, puede modificarse
    '''
    tirada=[]
    for i in range(num_dados):
        tirada.append(random.randint(1,6)) 
    return tirada


def es_generala(tirada):
    primer_dado = tirada[0]
    respuesta = False
    i = 1
    # Compara el valor de cada dado con el primer dado hasta que alguno sea distinto y en ese caso devuelve False.
    # Si recorrió toda la lista de tiradas sin que el while se rompa quiere decir que en todos salió el mismo número,
    while primer_dado == tirada[i]:
        i += 1
        if i==len(tirada): # este valor ya se fue del rango de índices de la lista, con lo que terminó de recorrerla
    	    respuesta = True
    	    break
    return respuesta


def ejercicio_5_1():
    # Corro esto 5 veces con N=100000 y 5 con N=1000000 para ver cómo varían los resultados
    intentos = [100000]*5 + [1000000]*5
    for N in intentos:
        G = sum([es_generala(tirar()) for i in range(N)])
        prob = G/N
        print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
        print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')


# Ejercicio 5.2

def simulo_una_mano(no_guardo_ninguno=False):
    '''
    Simula un turno en el juego de la generala si quien juega busca solamente sacar generala.
    Por defecto, se guarda uno de los dados si salen 5 números distintos (no_guardo_ninguno=False).
    Con no_guardo_ninguno=True, tira todos de nuevo si todos son distintos
    '''
    # Primera tirada
    i = 1
    dados = tirar()
    
    generala = es_generala(dados)
    # Si no fue generala servida entra al while a partir de la segunda tirada
    while not generala and i<3:

        if len(set(dados))==5 and no_guardo_ninguno==True:
            dados = tirar()
            
        else:
            # Obtengo diccionario del número de apariciones de cada valor
            dicc_repeticiones = Counter(dados)
            
            # Guardo el dado que más se repite y el número de veces que aparece.
            # Si ninguno se repite devuelve el primer valor que aparece en orden ascendente
            dado_repetido = max(dicc_repeticiones, key=dicc_repeticiones.get)
            dado_repetido_repeticiones = dicc_repeticiones[dado_repetido]

            # Armo lista con dados repetidos
            repetidos = [dado_repetido]*dado_repetido_repeticiones
            
            nuevos = tirar(5 - dado_repetido_repeticiones)
            
            dados = repetidos + nuevos
            
        generala = es_generala(dados)
        i += 1

    return generala



def prob_generala(N):
    # Devuelve una estimación de la probabilidad de sacar generala si al salir dados diferentes
    # se guarda uno y se tiran los 4 restantes
    G = sum([simulo_una_mano() for i in range(N)])
    prob = G/N
    return prob


def prob_generala_extra(N):
    # Devuelve una estimación de la probabilidad de sacar generala si al salir dados diferentes
    # se tiran todos nuevamente
    G = sum([simulo_una_mano(no_guardo_ninguno=True) for i in range(N)])
    prob = G/N
    return prob


# Extra:
# Según los resultados, parece ser más probable sacar generala al tirar todos los dados de nuevo.
# Promediando los resultados, es 0.0460013... para prob_generala y 0.046061 para prob_generala_extra
# Sin embargo no hice la cuenta exacta como para verificar esto

# >>> prob_generala(1000)
# 0.04
# >>> prob_generala_extra(1000)
# 0.048
# >>> prob_generala(10000)
# 0.0452
# >>> prob_generala_extra(10000)
# 0.0478
# >>> prob_generala(100000)
# 0.04661
# >>> prob_generala_extra(100000)
# 0.04616
# >>> prob_generala(1000000)
# 0.046139
# >>> prob_generala_extra(1000000)
# 0.046141
# >>> prob_generala(1000000)
# 0.045846
# >>> prob_generala_extra(1000000)
# 0.046291
# >>> prob_generala(1000000)
# 0.045945
# >>> prob_generala_extra(1000000)
# 0.045719