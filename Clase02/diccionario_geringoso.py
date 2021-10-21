# Ejercicio 2.14: Diccionario geringoso

def geringoso(cadena):
    capadepenapa = ''
    cadena = cadena.lower()
    for c in cadena:
        capadepenapa = capadepenapa + c
        if c in 'aeiou':
            vocal = c
            capadepenapa = capadepenapa + 'p' + vocal
    return capadepenapa

def dicc_geringoso(lista):
    'Devuelve el diccionario geringoso asociado a la lista de palabras que se pasa como argumento'
    dicc = {}
    for palabra in lista:
    	papalapabrapa = geringoso(palabra)
    	dicc[str(palabra)] = str(papalapabrapa)
    return dicc

# CORRO EL SCRIPT
# PS C:\Users\Ine\Desktop\Doctorado\ejercicios_python\Clase02> python -i diccionario_geringoso.py
# >>> a=dicc_geringoso(['banana', 'manzana', 'mandarina'])
# >>> a
# {'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}