# lote.py

class Lote:
    def __init__(self, nombre, cajones, precio):
        self.nombre = nombre
        self.cajones = cajones
        self.precio = precio

    def costo(self):
        return self.cajones * self.precio

    def vender(self, num_cajones):
        self.cajones -= num_cajones

    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'


# Salida del ejercicio 9.9:
# [Lote(Lima, 100, 32.2), Lote(Naranja, 50, 91.1), Lote(Caqui, 150, 103.44), 
#     Lote(Mandarina, 200, 51.23), Lote(Durazno, 95, 40.37), Lote(Mandarina, 50, 65.1), 
#     Lote(Naranja, 100, 70.44)]