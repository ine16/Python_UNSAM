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

    def proximo(self):
        '''Devuelve el próximo elemento sin desencolar
        Requiere que la cola no sea vacía'''
        return self.items[0]

    def desencolar(self):
        '''Elimina el primer elemento de la cola
        y devuelve su valor.
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def largo_cola(self):
        '''Devuelve el largo de la cola.'''
        return len(self.items)

    def esta_vacia(self):
        '''Devuelve
        True si la cola esta vacia,
        False si no.'''
        return self.largo_cola() == 0

    def imprimir(self):
        res = "<"
        res += ", ".join(self.items)
        res += ">"
        if not self.esta_vacia():
            res += "\n"
            res += f"Prox: {self.proximo()}"
        res += "\n"
        print(res)


class TorreDeControl:
    '''Simula el modelo de trabajo de una torre de contro
    de un aeropuerto con una pista de aterrizaje.'''
    def __init__(self):
        '''Crea dos listas donde se añadirán los aviones que estén por
        arribar o por partir.'''
        self.aviones_por_aterrizar = []
        self.aviones_por_despegar = []

    def nuevo_arribo(self, x):
        '''Añade un avión a la lista de aviones por aterrizar.'''
        self.aviones_por_aterrizar.append(x)

    def nueva_partida(self, x):
        '''Añade un avión a la lista de aviones por despegar.'''
        self.aviones_por_despegar.append(x)

    def asignar_pista(self):
        '''
        Elimina el primer elemento de una de las listas de aviones.
        Los aviones que están esperando para aterrizar tienen prioridad
        sobre los que están esperando para despegar.
        Si las listas están vacías, se nos informá al respecto.
        '''
        # Booleanos en caso de que alguna lista esté vacía
        no_aviones_aterrizar = len(self.aviones_por_aterrizar) == 0
        no_aviones_despegar = len(self.aviones_por_despegar) == 0
        
        # Si no hay ningún avión en espera...
        if no_aviones_aterrizar and no_aviones_despegar:
            print('No hay vuelos en espera.')
        # Si no hay aviones en espera por aterrizar...
        elif no_aviones_aterrizar:
            print(f'El vuelo {self.aviones_por_despegar[0]} despegó con éxito.')
            self.aviones_por_despegar.pop(0)
        # Si hay tanto aviones por aterrizar como por despegar en espera...
        else:
            print(f'El vuelo {self.aviones_por_aterrizar[0]} aterrizó con éxito.')
            self.aviones_por_aterrizar.pop(0)

    def ver_estado(self):
        l_aterrizar = ", ".join(self.aviones_por_aterrizar)
        l_despegar = ", ".join(self.aviones_por_despegar)
        print(f'Vuelos esperando para aterrizar: {l_aterrizar}')
        print(f'Vuelos esperando para despegar: {l_despegar}')


'''
>>> torre = torre_control.TorreDeControl()
>>> torre.nuevo_arribo('AR156')
>>> torre.nueva_partida('KLM1267')
>>> torre.nuevo_arribo('AR32')
>>> torre.ver_estado()
Vuelos esperando para aterrizar: AR156, AR32
Vuelos esperando para despegar: KLM1267
>>> torre.asignar_pista()
El vuelo AR156 aterrizó con éxito.
>>> torre.asignar_pista()
El vuelo AR32 aterrizó con éxito.
>>> torre.asignar_pista()
El vuelo KLM1267 despegó con éxito.
>>> torre.asignar_pista()
No hay vuelos en espera.
'''