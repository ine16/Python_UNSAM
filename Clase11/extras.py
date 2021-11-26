# Ejercicios de recursión

def triangular(n):
    res = n
    if n > 1:
        res += triangular(n-1)
    return res

def cant_digitos(n):
    '''
    Devuelve el número de dígitos de n, que debe ser positivo
    '''
    res = n//1
    digitos = 0
    if res != 0:
        digitos += cant_digitos(n//10)
        digitos += 1
    return digitos

def es_potencia(n, b):
    '''
    Recibe 2 enteros, n y b, y devuelve True si n es potencia de b y False en caso contrario.
    n y b deben ser positivos
    '''
    n_es_potencia = False
    res = n//b
    if res*b == n and res >= 1:
        n_es_potencia = es_potencia(res,b)
        if res == 1:
            n_es_potencia = True
    return n_es_potencia

# otra forma (la hizo benja, le agregue cosas, falta probarla):
def es_potencia(n, b):
    '''
    Recibe 2 enteros, n y b, y devuelve True si n es potencia de b y False en caso contrario.
    n y b deben ser positivos
    '''
    res = n==b
    if n > b:
        res = es_potencia(n/b,b)
    return res

def par(n):
    es_par = False
    if n>1 and impar(n-1):
        es_par = True
    return es_par

def impar(n):
    es_impar = False
    if n==1:
        es_impar = True
    elif n>1 and par(n-1):
        es_impar = True
    return es_impar

def maximo(lista):
    valor_maximo = lista[0]
    n = 1
    if len(lista)==1:
        valor_maximo = lista[0]
    elif valor_maximo <= lista[0]:
        valor_maximo = maximo(lista[1:])
    # TERMINAR