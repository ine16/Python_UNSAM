# bbin.py


def donde_insertar(lista, x):
    '''
    Recibe una lista ordenada y un elemento y devuelve la posición de ese elemento 
    en la lista (si se encuentra en la lista) o la posición donde se podría insertar 
    el elemento para que la lista permanezca ordenada (si no está en la lista).
    '''
    pos = 0 # Inicializo respuesta
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
            break
        if lista[medio] > x:
            if lista[medio-1] < x:
                pos = medio
                break
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    if lista[medio] < x:
    	pos = medio + 1
    return pos


def insertar(lista, x):
    pos = donde_insertar(lista, x)
    if lista[pos] != x:
        lista.insert(pos, x)
    return pos
