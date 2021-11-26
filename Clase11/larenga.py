# larenga.py

def pascal(n, k):
    '''
    Calcula el valor que se encuentra en la fila n y la columna k 
    del triángulo de Pascal
    '''
    if n == 0 or k%n == 0:
        valor = 1
    else:
        valor = pascal(n - 1, k - 1) + pascal(n - 1, k)
    return valor