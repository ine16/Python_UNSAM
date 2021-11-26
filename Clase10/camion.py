# camion.py

class Camion:

    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self):
        return self.lotes.__iter__()

    def precio_total(self):
        return sum((l.costo() for l in self.lotes))

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for lote in self.lotes:
            cantidad_total[lote.nombre] += lote.cajones
        return cantidad_total
    
    def __contains__(self, nombre):
        return any([lote.nombre == nombre for lote in self.lotes])

    def __len__(self):
        return self.lotes.__len__()

    def __getitem__(self, a):
        return self.lotes.__getitem__(a)

    def __str__(self):
        contenido = f'Camion con {self.__len__()} lotes:'
        for item in self.lotes:
            contenido += f'\nLote de {item.cajones} cajones de {item.nombre}, pagados a ${item.precio} cada uno.'
        return contenido

    def __repr__(self):
        return f'Camion({self.lotes})'