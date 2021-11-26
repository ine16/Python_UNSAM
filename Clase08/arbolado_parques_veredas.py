import pandas as pd
import os
import matplotlib.pyplot as plt

def ejemplares(archivo, cols_sel, nomenclatura_especie):
    '''
    cols_sel: lista, su primer elemento indica la nomenclatura para el nombre científico en el archivo
    nomenclatura_especie: cadena

    '''
    directorio = '../Data'
    fname = os.path.join(directorio, archivo)
    df = pd.read_csv(fname)
    df_seleccion = df[df[cols_sel[0]] == nomenclatura_especie][cols_sel[1:]].copy()
    return df_seleccion


# 'altura_tot', 'diametro' y 'nombre_cie' para las alturas, diámetros y nombres científicos
cols_parques = ['nombre_cie', 'diametro', 'altura_tot']
# 'altura_arbol', 'diametro_altura_pecho' y 'nombre_cientifico' para esos datos
cols_veredas = ['nombre_cientifico', 'diametro_altura_pecho', 'altura_arbol']
# Nos queremos quedar con los datos que correspondan a tipas (Tipuana tipu)
df_tipas_parques = ejemplares('arbolado-en-espacios-verdes.csv', cols_parques, 'Tipuana Tipu')
df_tipas_veredas = ejemplares('arbolado-publico-lineal-2017-2018.csv', cols_veredas, 'Tipuana tipu')

df_tipas_veredas.rename(columns = {'diametro_altura_pecho': 'diametro', 
                        'altura_arbol': 'altura_tot'}, inplace=True)
df_tipas_parques['ambiente'] = len(df_tipas_parques) * ['parque']
df_tipas_veredas['ambiente'] = len(df_tipas_veredas) * ['vereda']
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
df_tipas.boxplot('diametro', by = 'ambiente')
df_tipas.boxplot('altura_tot', by = 'ambiente')
plt.show()


#=============
# ¿Qué tendrías que cambiar para repetir el análisis para otras especies?
# ¿Convendría definir una función?
#
# No sé si convenía definir una función pero ya habia definido una para hacer el ejercicio.
# Me pareció más cómodo y general definir una función