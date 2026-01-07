class Nodo:
    def __init__(self, identificador):
        self.id = identificador      # Identificador único del nodo
        self.propiedades = dict()    # Almacena los atributos del nodo

    def agregar_atributo(self, nombre, dato):
        self.propiedades[nombre] = dato
