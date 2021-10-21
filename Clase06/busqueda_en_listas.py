# busqueda_en_listas.py

def buscar_u_elemento(lista, elemento):
    '''
    Si "elemento" está en "lista" devuelve la posición de su última aparición,
    si no está en "lista" devuelve -1.
    '''
    if type(lista) != list:
        print('Error, no se ingresó una lista.')
        return
    if lista == []:
        print('Error, la lista ingresada está vacía.')
        return
    pos = -1
    for i, z in enumerate(lista):
        if z == elemento:
            pos = i
    return pos


def buscar_n_elemento(lista, elemento):
    '''
    Devuelva la cantidad de veces que "elemento" aparece en "lista".
    '''
    n = 0
    for z in lista:
        if z == elemento:
            n += 1
    return n


def maximo(lista):
    '''
    Devuelve el máximo de una lista, la lista debe ser no vacía.
    '''
    # m guarda el máximo de los elementos a medida que recorro la lista.

    m = lista[0] # Lo inicializo como el primer elemento de la lista
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e > m:
            m = e
    return m


def minimo(lista):
    '''
    Devuelve el mínimo de una lista, la lista debe ser no vacía.
    '''
    # m guarda el mínimo de los elementos a medida que recorro la lista.

    m = lista[0] # Lo inicializo como el primer elemento de la lista
    for e in lista: # Recorro la lista y voy guardando el mayor
        if e < m:
            m = e
    return m


def busqueda_lineal_lordenada(lista, e):
    '''
    Si e está en la lista devuelve su posición, de lo
    contrario devuelve -1. La lista debe estar ordenada de menor a mayor
    '''

    pos = -1  # comenzamos suponiendo que e no está
    for i, z in enumerate(lista): # recorremos la lista
        if z == e:   # si encontramos a e
            pos = i  # guardamos su posición
            break    # y salimos del ciclo
        if z > e:
            break
    return pos