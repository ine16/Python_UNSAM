# costo_camion.py

import informe_final


def costo_camion(nombre_archivo):
    dicc_camion = informe_final.leer_camion(nombre_archivo)
    costo_total = sum([ vegetal['cajones'] * vegetal['precio'] for vegetal in dicc_camion ])
    return costo_total

def f_principal(parametros):
    nombre_archivo_camion = parametros[1]
    costo_total = costo_camion(nombre_archivo_camion)
    print(f'Costo total: {costo_total:.2f}')

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion')
    f_principal(sys.argv)


# import costo_camion
# costo_camion.costo_camion('../Data/camion.csv')