from Nodo import Nodo
from Arista import Arista


# Clase Grafo (no dirigido)
class Grafo:
    def __init__(self):
        self.nodos = dict()      # id -> Nodo
        self.aristas = []        # lista de objetos Arista
        self.atributos = dict()  # atributos adicionales

    # ======================
    # MÉTODOS BÁSICOS
    # ======================
    def agregar_nodo(self, identificador):
        if identificador not in self.nodos:
            self.nodos[identificador] = Nodo(identificador)

    def agregar_arista(self, origen, destino):
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)

        arista = Arista(origen, destino)
        self.aristas.append(arista)

    def mostrar_grafo(self):
        print("Nodos:")
        for nodo in self.nodos.values():
            print(f"  Nodo {nodo.id}")

        print("\nAristas:")
        for arista in self.aristas:
            print(f"  {arista.nodo_inicio.id} -> {arista.nodo_fin.id}")

    # ======================
    # EXPORTACIÓN GRAPHVIZ
    # ======================
    def exportar_a_gv(self, nombre_archivo):
        with open(nombre_archivo, "w") as f:
            f.write("graph G {\n")

            usadas = set()
            nodos_con_arista = set()

            for arista in self.aristas:
                a = arista.nodo_inicio.id
                b = arista.nodo_fin.id

                if (b, a) not in usadas:
                    f.write(f"    {a} -- {b};\n")
                    usadas.add((a, b))

                nodos_con_arista.update((a, b))

            for nodo_id in self.nodos:
                if nodo_id not in nodos_con_arista:
                    f.write(f"    {nodo_id};\n")

            f.write("}\n")

    def exportar_a_gv_algoritmo(self, nombre_archivo):
        if not hasattr(self, "bfs_resultado"):
            print("Primero debes ejecutar BFS.")
            return

        padres = self.bfs_resultado["padres"]
        visitados = self.bfs_resultado["visitados"]

        with open(nombre_archivo, "w") as f:
            f.write("digraph G {\n")

            for nodo in visitados:
                f.write(f"    {nodo};\n")

            for hijo, padre in padres.items():
                f.write(f"    {padre} -> {hijo};\n")

            f.write("}\n")

        print(f"Grafo exportado a {nombre_archivo}")

    def exportar_arbol_dfs_a_gv(self, arbol_dfs, nombre_archivo):
        with open(nombre_archivo, "w") as f:
            f.write("digraph G {\n")

            usados = set()
            for a, b in arbol_dfs:
                f.write(f"    {a} -> {b};\n")
                usados.update((a, b))

            for nodo in self.nodos:
                if nodo not in usados:
                    f.write(f"    {nodo};\n")

            f.write("}\n")

    # ======================
    # BFS
    # ======================
    def BFS(self, s):
        print("Algoritmo BFS\n")

        if s not in self.nodos:
            print("El nodo no existe")
            return False

        capas = [[s]]
        visitados = [s]
        padres = {}

        nivel = 0
        while capas[nivel]:
            nueva_capa = []

            for u in capas[nivel]:
                for arista in self.aristas:
                    a = arista.nodo_inicio.id
                    b = arista.nodo_fin.id

                    if a == u and b not in visitados:
                        visitados.append(b)
                        nueva_capa.append(b)
                        padres[b] = u
                    elif b == u and a not in visitados:
                        visitados.append(a)
                        nueva_capa.append(a)
                        padres[a] = u

            capas.append(nueva_capa)
            nivel += 1

        if not capas[-1]:
            capas.pop()

        for i, capa in enumerate(capas):
            print(f"Capa {i}: {capa}")

        self.bfs_resultado = {
            "capas": capas,
            "padres": padres,
            "visitados": visitados
        }

        return self.bfs_resultado

    # ======================
    # DFS RECURSIVA
    # ======================
    def DFS_recursiva(self, s, explorados=None, arbol=None):
        if s not in self.nodos:
            print("El nodo no existe")
            return False

        if explorados is None:
            explorados = set()
        if arbol is None:
            arbol = []

        explorados.add(s)

        for arista in self.aristas:
            a = arista.nodo_inicio.id
            b = arista.nodo_fin.id

            if a == s and b not in explorados:
                arbol.append((s, b))
                self.DFS_recursiva(b, explorados, arbol)

            elif b == s and a not in explorados:
                arbol.append((s, a))
                self.DFS_recursiva(a, explorados, arbol)

        return arbol

    # ======================
    # DFS ITERATIVA
    # ======================
    def DFS_iterativa(self, s):
        if s not in self.nodos:
            print("El nodo no existe")
            return False

        visitados = set()
        arbol = []
        stack = [(s, None)]

        while stack:
            u, padre = stack.pop()

            if u not in visitados:
                visitados.add(u)

                if padre is not None:
                    arbol.append((padre, u))

                vecinos = []
                for arista in self.aristas:
                    a = arista.nodo_inicio.id
                    b = arista.nodo_fin.id

                    if a == u and b not in visitados:
                        vecinos.append(b)
                    elif b == u and a not in visitados:
                        vecinos.append(a)

                for v in reversed(vecinos):
                    stack.append((v, u))

        return arbol
