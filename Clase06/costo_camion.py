# costo_camion.py

import informe_funciones

def costo_camion(nombre_archivo):
    dicc_camion = informe_funciones.leer_camion(nombre_archivo)
    costo_total = sum([ vegetal['cajones'] * vegetal['precio'] for vegetal in dicc_camion ])
    return costo_total


# import costo_camion
# costo_camion.costo_camion('../Data/camion.csv')