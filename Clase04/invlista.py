def invertir_lista(lista):
    invertida = []
    for e in lista: # Recorro la lista
        invertida.insert(0,e) #agrego el elemento e al principio de la lista invertida
    return invertida


# SALIDA DE CADA PRUEBA
# >>> invertir_lista([1, 2, 3, 4, 5])
# [5, 4, 3, 2, 1]
# >>> invertir_lista(['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'])
# ['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']