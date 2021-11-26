import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def desplazamiento_promediado(df):
    mitad = len(df)//2
    despl_max = int((np.argmax(dh['H_BA'][:mitad]) - 
    	         np.argmax(dh['H_SF'][:mitad]) +
    	         np.argmax(dh['H_BA'][mitad:]) - 
    	         np.argmax(dh['H_SF'][mitad:]))/2)
    despl_min = int((np.argmin(dh['H_BA'][:mitad]) - 
    	         np.argmin(dh['H_SF'][:mitad]) +
    	         np.argmin(dh['H_BA'][mitad:]) - 
    	         np.argmin(dh['H_SF'][mitad:]))/2)
    return (despl_max + despl_min)//2


df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv', index_col=['Time'], 
                 parse_dates=True)
dh = df['12-25-2014':].copy()

# Tiempo que tarda la marea entre ambos puertos
delta_t = desplazamiento_promediado(dh)
# Diferencia de los ceros de escala entre ambos puertos
delta_h = (max(dh['H_SF']) - max(dh['H_BA']) + 
           min(dh['H_SF']) - min(dh['H_BA']))/2

pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()
plt.show()