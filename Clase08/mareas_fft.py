from scipy import signal # para procesar señales
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def calcular_fft(y, frec_sampleo = 24.0):
    '''y debe ser un vector con números reales
    representando datos de una serie temporal.
    frec_sampleo está seteado para considerar 24 datos por unidad.
    Devuelve dos vectores, uno de frecuencias 
    y otro con la transformada propiamente.
    La transformada contiene los valores complejos
    que se corresponden con respectivas frecuencias.'''
    N = len(y)
    frec = np.fft.fftfreq(N, d = 1/frec_sampleo)[:N//2]
    tran = (np.fft.fft(y)/N)[:N//2]
    return frec, tran



df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], 
                 parse_dates=True)
inicio = '2014-01'
fin = '2014-06'
alturas_sf = df[inicio:fin]['H_SF'].to_numpy()
alturas_ba = df[inicio:fin]['H_BA'].to_numpy()


plt.figure(1)
freq_sf, fft_sf = calcular_fft(alturas_sf)
plt.plot(freq_sf, np.abs(fft_sf))
plt.xlabel("Frecuencia")
plt.ylabel("Potencia (energía)")
plt.xlim(0,4)
plt.ylim(0,20)
# Me quedo sólo con el último pico
pico_sf = signal.find_peaks(np.abs(fft_sf), prominence = 8)[0][-1]
# Es el pico a analizar, el de la onda de mareas
# Marco ese pico con un circulito rojo
plt.scatter(freq_sf[pico_sf], np.abs(fft_sf)[pico_sf], facecolor = 'r')
plt.title("Espectro de Potencias San Fernando")


plt.figure(2)
freq_ba, fft_ba = calcular_fft(alturas_ba)
plt.plot(freq_ba, np.abs(fft_ba))
plt.xlabel("Frecuencia")
plt.ylabel("Potencia (energía)")
plt.xlim(0,4)
plt.ylim(0,20)
# Me quedo sólo con el último pico
pico_ba = signal.find_peaks(np.abs(fft_ba), prominence = 8)[0][-1]
# Se grafican los picos como circulitos rojos
plt.scatter(freq_ba[pico_ba], np.abs(fft_ba)[pico_ba], facecolor='r')
plt.title("Espectro de Potencias Bs.As.")


altura_cero_sf = np.abs(fft_sf[0])
altura_cero_ba = np.abs(fft_ba[0])
# Desfasaje vertical entre los ceros de escala de los puertos analizados
diferencia_alturas = altura_cero_sf - altura_cero_ba
print(f'La diferencia de alturas entre puertos es de {diferencia_alturas:.2f} cm')


ang_ba = np.angle(fft_ba)[pico_ba]
freq = freq_ba[pico_ba]
ang2h = 24 / (2*np.pi*freq)
ang_sf = np.angle(fft_sf)[pico_sf]
desfasaje_horas = (ang_ba - ang_sf) * ang2h
desfasaje_minutos = desfasaje_horas * 60
print(f'La onda de mareas tarda aprox. {desfasaje_minutos:.2f} minutos')


# Figura del ejercicio 8.10
dh = df['12-25-2014':].copy()
# Como desfasaje_horas > 0, fase_sf = fase_ba + desfasaje_horas
# Con .shift(delta_t) paso de tiempo_sf a tiempo_sf + delta_t
delta_t = -int(round(desfasaje_horas))
pd.DataFrame([dh['H_SF'].shift(delta_t) - diferencia_alturas, dh['H_BA']]).T.plot()


# Ejercicio 8.13
df_za = pd.read_csv('../Data/OBS_Zarate_2013A.csv', index_col=['Time'], 
                 parse_dates=True)
inicio = '2012-08'
fin = '2013-02'
alturas_za = df_za[inicio:fin]['H_Zarate'].to_numpy()
frec_za, fft_za = calcular_fft(alturas_za)
# Me quedo sólo con el último pico
pico_za = signal.find_peaks(np.abs(fft_za), prominence = 4)[0][-1]
ang_za = np.angle(fft_za)[pico_za]
frec_za = frec_za[pico_za]
ang2h_za = 24 / (2*np.pi*frec_za)
ang_za = np.angle(fft_za)[pico_za]

# Consigo los datos para BA en los tiempos en que hay datos para Zárate
alturas_ba_za = df[inicio:fin]['H_BA'].to_numpy()
frec_ba_za, fft_ba_za = calcular_fft(alturas_ba_za)
# Me quedo sólo con el último pico
pico_ba_za = signal.find_peaks(np.abs(fft_ba_za), prominence = 8)[0][-1]
ang_ba_za = np.angle(fft_za)[pico_ba_za]
frec_ba_za = frec_ba_za[pico_ba_za]
ang2h_ba_za = 24 / (2*np.pi*frec_ba_za)
ang_ba_za = np.angle(fft_ba_za)[pico_ba_za]

# Calculo el desfasaje
desfasaje_ba_za = ang_za * ang2h_za - ang_ba_za * ang2h_ba_za
horas_de_desfasaje = int(abs(desfasaje_ba_za))
minutos_de_desfasaje = int(abs((desfasaje_ba_za - horas_de_desfasaje) * 60))
print(f'La onda de marea tarda aprox. {horas_de_desfasaje} horas con {minutos_de_desfasaje} minutos en llegar a Zárate')

plt.show()


# Obviamente la onda llega atenuada a Zárate. ¿Cómo se refleja esta atenuación en la transformada?
# Si dejamos prominence=8 como en los casos anteriores nos da array vacío