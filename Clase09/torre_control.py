# torre_control.py

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0


class TorreDeControl:
    def __init__(self):
        '''
        partidas y arribos contendrán los aviones que despegan y que llegan

        '''
        self.partidas = Cola()
        self.arribos = Cola()
    
    def nuevo_arribo(self, avion):
        '''
        Guarda el avión en la cola de aviones que quieren aterrizar
        
        Parámetros
        avion: string
        '''
        self.arribos.encolar(avion)
    
    def nueva_partida(self, avion):
        '''
        Guarda el avión en la cola de aviones que quieren despegar
        
        Parámetros
        avion: string
        '''
        self.partidas.encolar(avion)
    
    def ver_estado(self):
        para_aterrizar = f'Vuelos esperando para aterrizar: ' + ', '.join(self.arribos.items)
        para_despegar = f'\nVuelos esperando para despegar: ' + ', '.join(self.partidas.items)
        print(para_aterrizar + para_despegar)

    def asignar_pista(self):
        '''
        Los aviones que están esperando para aterrizar tienen prioridad 
        sobre los que están esperando para despegar. Se asigna pista
        a los aviones de ambas colas teniendo en cuenta esto.
        '''

        # Mientras hayan aviones esperando aterrizar se les asigna pista primero según orden de llegada.
        if not self.arribos.esta_vacia():
            print(f'El vuelo {self.arribos.desencolar()} aterrizó con éxito.')
        
        # Una vez agotados se pasa a los aviones esperando despegar.
        elif not self.partidas.esta_vacia():
            print(f'El vuelo {self.partidas.desencolar()} despegó con éxito.')
        
        # Si arribos y partidas están vacías significa que no hay aviones en espera
        else:
            print('No hay vuelos en espera.')