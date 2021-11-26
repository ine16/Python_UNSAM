# vida.py

from datetime import datetime, timedelta

def vida_en_segundos(fecha_nac):
    '''
    A partir de una cadena en formato 'dd/mm/AAAA' 
    (día, mes y año, con 2, 2 y 4 dígitos, separados
    con barras normales) y devuelve un float.
    '''

    nacimiento = datetime.strptime(fecha_nac, '%d/%m/%Y')
    hoy = datetime.now()
    segundos_vividos = (hoy - nacimiento).total_seconds()
    return segundos_vividos
