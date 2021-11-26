from datetime import date, datetime, timedelta

def placa_cronica_primavera():
    '''
    Al correrla devuelve los días que faltan para la primavera desde el día de hoy.
    Si ya es primavera devuelve 0	
    '''
    hoy = date.today()
    # Si no cumple ninguna de las condiciones de los if es primavera y devuelve 0 días
    dias_para_primavera = 0

    if hoy.month == 12 and hoy.day >= 21:
        anio = hoy.year + 1
        primavera = date(year = anio, month = 9, day = 21)
        dias_para_primavera = primavera - hoy

    if hoy.month <= 9 and hoy.day <= 21:
        primavera = date(year = hoy.year, month = 9, day = 21)
        dias_para_primavera = primavera - hoy

    return dias_para_primavera.days


def dias_habiles(inicio, fin, feriados):
    '''
    Tiene como argumentos el día inicial, el día final, y una lista
    con las fechas correspondientes a los feriados que haya en ese lapso.
    Devuelve una lista con las fechas de días hábiles del período, 
    incluyendo la fecha inicial y la fecha final indicadas.

    Todas las fechas son cadenas en formato 'dd/mm/AAAA'
    '''

    lista_habiles = []

    # Voy aumentando de a un día y chequeando que no sea feriado ni día laboral
    dia_string = inicio
    while dia_string != fin:
        dia_fecha = datetime.strptime(dia_string, '%d/%m/%Y')
        if dia_string not in feriados and dia_fecha.weekday() <= 4:
            lista_habiles.append(dia_string)
        dia_fecha = dia_fecha + timedelta(days = 1)
        dia_string = dia_fecha.strftime('%d/%m/%Y')
    fin_fecha = datetime.strptime(fin, '%d/%m/%Y')
    if fin not in feriados and fin_fecha.weekday() <= 4:
        lista_habiles.append(fin)
    return lista_habiles



def ejercicio_8_4():
    feriados = ['12/10/2020', '23/11/2020', '07/12/2020', '08/12/2020', '25/12/2020']
    inicio = '20/09/2020'
    fin = '10/10/2020'
    print(f'Lista de días hábiles entre el {inicio} y {fin}:\n')
    print(dias_habiles(inicio, fin, feriados))
    inicio = '10/10/2020'
    fin = '31/12/2020'
    print(f'Lista de días hábiles entre el {inicio} y {fin}:\n')
    print(dias_habiles(inicio, fin, feriados))


import pandas as pd
import os

directorio = '../Data'
archivo = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)
cant_ejemplares = df['nombre_com'].value_counts()
print(len(cant_ejemplares.index))