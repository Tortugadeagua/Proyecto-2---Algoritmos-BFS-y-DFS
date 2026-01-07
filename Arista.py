from Nodo import Nodo

# Clase que modela una conexión entre dos nodos
class Arista:
    def __init__(self, origen, destino):
        self.nodo_inicio = Nodo(origen)     # Nodo origen
        self.nodo_fin = Nodo(destino)       # Nodo destino
        self.conexion = (self.nodo_inicio, self.nodo_fin)  # Tupla que representa la arista
        self.propiedades = dict()            # Atributos adicionales de la arista

    def agregar_atributo(self, nombre, dato):
        self.propiedades[nombre] = dato
