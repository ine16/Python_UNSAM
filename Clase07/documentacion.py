# documentacion.py

def valor_absoluto(n):
    '''
    Devuelve el valor absoluto de un número real n.
    '''
    if n >= 0:
        return n
    else:
        return -n

#%%
def suma_pares(l):
    '''
    Calcula la suma de los elementos pares de un iterable.

    Pre: el iterable debe contener números enteros
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
# res es el invariante de ciclo ya que contiene la suma de los números pares
#de la porción de lista ya recorrida


#%%
def veces(a, b):
    '''
    Devuelve el producto entre a y b

    Pre: b debe ser un número entero positivo, a puede ser de cualquier tipo
    '''
    res = 0
    nb = b

    # Hacer a*b equivale a sumar b veces el valor "a"
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
# nb * a + res es el invariante de ciclo


#%%
def collatz(n):
    '''
    Si n es par, se divide por 2. Si n es impar, se multiplica por 3 y se le suma 1. Al resultado
    se le aplican las mismas operaciones según si es par o impar y así sucesivamente.
    Devuelve el número de elementos en la secuencia generada (incluyendo al número n de partida).

    Pre: n es un número entero positivo
    '''

    res = 1

    # Según la conjetura de Collatz, el resultado de este algoritmo es 1 para todo n.
    #Para "chequearla", proponemos que n=1 sea la condición para salir del while
    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res