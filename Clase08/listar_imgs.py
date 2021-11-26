# listar_imgs.py

import os
from pprint import pprint

def archivos_png(directorio):
    '''
    Dado un directorio, imprime en pantalla los nombres de todos los archivos .png 
    que se encuentran en algún subdirectorio del él. Puede ejecutarse desde la línea 
    de comandos recibiendo como parámetro el directorio a leer.
    '''
    lista_png = []

    for root, dirs, files in os.walk(directorio):
        for name in files:
            if '.png' in name:
                lista_png.append(name)

    pprint(lista_png)



if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} directorio')
    archivos_png(sys.argv[1])