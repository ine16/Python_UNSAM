# canguros_buenos.py

class Canguro:
    def __init__(self, nombre, contenido = []):
        '''
        Atributos de la clase Canguro

        Pre:
        "nombre" es una cadena
        "contenido" (opcional) es una lista
        '''
        self.nombre = nombre
        self.contenido_marsupio = contenido.copy()

    def meter_en_marsupio(self, objeto):
        self.contenido_marsupio.append(objeto)

    def __str__(self):
        '''
        Cómo se debe imprimir un objeto de la clase Canguro

        '''
        en_marsupio = f'Contenido del marsupio de {self.nombre}:\n'
        for cosa in self.contenido_marsupio:
            en_marsupio += object.__str__(cosa) + '\n'
        return en_marsupio



#%%
# canguro_malo.py

"""Este código contiene un 
bug importante y difícil de ver
"""

# class Canguro:
#     """Un Canguro es un marsupial."""
    
#     def __init__(self, nombre, contenido=[]):
#         """Inicializar los contenidos del marsupio.

#         nombre: string
#         contenido: contenido inicial del marsupio, lista.
#         """
#         self.nombre = nombre
#         self.contenido_marsupio = contenido.copy()

#     def __str__(self):
#         """devuelve una representación como cadena de este Canguro.
#         """
#         t = [ self.nombre + ' tiene en su marsupio:' ]
#         for obj in self.contenido_marsupio:
#             s = '    ' + object.__str__(obj)
#             t.append(s)
#         return '\n'.join(t)

#     def meter_en_marsupio(self, item):
#         """Agrega un nuevo item al marsupio.

#         item: objecto a ser agregado
#         """
#         self.contenido_marsupio.append(item)

#%%
# madre_canguro = Canguro('Madre')
# cangurito = Canguro('gurito')
# madre_canguro.meter_en_marsupio('billetera')
# madre_canguro.meter_en_marsupio('llaves del auto')
# madre_canguro.meter_en_marsupio(cangurito)

# print(madre_canguro)
# print(cangurito)

# Al ejecutar este código todo parece funcionar correctamente.
# El problema era que, al hacer print(cangurito) resulta que cangurito tenía
#     en su marsupio lo mismo que madre_canguro.

# Probé de solucionarlo agregando un .copy() en la línea 36 y funcionó.
# Me sonaba a que tenía que ver con que al hacer 
#     self.contenido_marsupio = contenido hacía que ambos objetos referencien 
#     a lo mismo, pero no termino de entender.