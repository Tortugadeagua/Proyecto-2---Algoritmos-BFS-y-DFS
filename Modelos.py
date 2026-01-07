from Grafo import Grafo
import random
import math


# =========================
# Modelo Erdős–Rényi G(n, m)
# =========================
def grafo_ErdosRenyi(n, m, dirigido=False):
    g = Grafo()

    for nodo_id in range(n):
        g.agregar_nodo(nodo_id)

    pares_posibles = [
        (i, j) for i in range(n) for j in range(i + 1, n)
    ]
    aristas_elegidas = random.sample(pares_posibles, m)

    for origen, destino in aristas_elegidas:
        g.agregar_arista(origen, destino)

    return g


# ======================
# Modelo de Gilbert G(n, p)
# ======================
def grafo_Gilbert(n, p, dirigido=False):
    g = Grafo()

    for nodo_id in range(n):
        g.agregar_nodo(nodo_id)

    for i in range(n):
        for j in range(i + 1, n):
            if random.random() <= p / 100:
                g.agregar_arista(i, j)

    return g


# ============================
# Grafo Geográfico Aleatorio
# ============================
def grafo_Geografico(n, r, dirigido=False):
    g = Grafo()
    coordenadas = {}

    for nodo_id in range(1, n + 1):
        g.agregar_nodo(nodo_id)
        coordenadas[nodo_id] = (random.random(), random.random())

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            x1, y1 = coordenadas[i]
            x2, y2 = coordenadas[j]

            if math.hypot(x2 - x1, y2 - y1) <= r:
                g.agregar_arista(i, j)

    return g


# ============================
# Modelo Barabási–Albert
# ============================
def grafo_BarabasiAlbert(n, d, dirigido=False):
    g = Grafo()
    grados = {i: 0 for i in range(1, n + 1)}

    for nodo_id in range(1, n + 1):
        g.agregar_nodo(nodo_id)

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if grados[i] < d and grados[j] < d:
                probabilidad = min(
                    1 - grados[i] / d,
                    1 - grados[j] / d
                )
                if random.random() < probabilidad:
                    g.agregar_arista(i, j)
                    grados[i] += 1
                    grados[j] += 1

    return g


# ============================
# Modelo Dorogovtsev–Mendes
# ============================
def grafo_DoroMendes(n, dirigido=False):
    g = Grafo()

    # Triángulo inicial
    for nodo_id in range(1, 4):
        g.agregar_nodo(nodo_id)

    lista_aristas = [(1, 2), (2, 3), (3, 1)]
    for a, b in lista_aristas:
        g.agregar_arista(a, b)

    for nuevo_nodo in range(4, n + 1):
        g.agregar_nodo(nuevo_nodo)
        u, v = random.choice(lista_aristas)

        g.agregar_arista(nuevo_nodo, u)
        g.agregar_arista(nuevo_nodo, v)

        lista_aristas.append((nuevo_nodo, u))
        lista_aristas.append((nuevo_nodo, v))

    return g


# ============================
# Grafo de Malla (Grid m x n)
# ============================
def grafo_Malla(m, n):
    g = Grafo()
    mapa_nodos = {}
    identificador = 1

    for fila in range(m):
        for columna in range(n):
            mapa_nodos[(fila, columna)] = identificador
            g.agregar_nodo(identificador)
            identificador += 1

    for fila in range(m):
        for columna in range(n):
            actual = mapa_nodos[(fila, columna)]

            if columna + 1 < n:  # vecino derecho
                g.agregar_arista(actual, mapa_nodos[(fila, columna + 1)])

            if fila + 1 < m:  # vecino inferior
                g.agregar_arista(actual, mapa_nodos[(fila + 1, columna)])

    return g