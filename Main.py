from Modelos import *

# ============================
# MAIN – EJECUCIÓN DE MODELOS
# ============================

def main():

    """
    Descomenta el bloque del modelo que desees ejecutar.
    Todos son compatibles con Nodo, Arista, Grafo y algoritmos BFS / DFS.
    """

    # ----------------------------
    # Modelo Erdős–Rényi G(n, m)
    # ----------------------------
    """
    g = grafo_ErdosRenyi(500, 499)
    g.mostrar_grafo()
    g.exportar_a_gv("Grafo_ErdosRenyi_500.gv")
    """

    # ----------------------------
    # Modelo de Gilbert G(n, p)
    # ----------------------------
    """
    g = grafo_Gilbert(500, 15)
    g.mostrar_grafo()
    g.exportar_a_gv("Grafo_Gilbert_500.gv")
    """

    # --------------------------------
    # Modelo Dorogovtsev–Mendes
    # --------------------------------
    """
    g = grafo_DoroMendes(500)
    g.mostrar_grafo()
    g.exportar_a_gv("Grafo_DoroMendes_500.gv")
    """

    # ----------------------------
    # Modelo de Malla G(m, n)
    # ----------------------------
    """
    g = grafo_Malla(25, 20)
    g.mostrar_grafo()
    g.exportar_a_gv("Grafo_Malla_500.gv")
    """

    # --------------------------------
    # Modelo Barabási–Albert G(n, d)
    # --------------------------------
    """
    g = grafo_BarabasiAlbert(50, 5)
    g.mostrar_grafo()
    g.exportar_a_gv("Grafo_Barabasi_50.gv")
    """

    # --------------------------------
    # Modelo Geográfico Simple G(n, r)
    # --------------------------------
    g = grafo_Geografico(500, 0.2)
    g.mostrar_grafo()
    # g.exportar_a_gv("Grafo_Geografico_500.gv")

    # ----------------------------
    # BFS
    # ----------------------------
    # g.BFS(10)
    # g.exportar_a_gv_algoritmo("Grafo_Geografico_BFS_500.gv")

    # ----------------------------
    # DFS Recursivo
    # ----------------------------
    # arbol_dfs_r = g.DFS_recursiva(40)
    # g.exportar_arbol_dfs_a_gv(arbol_dfs_r, "Geografico_DFS_R_500.gv")

    # ----------------------------
    # DFS Iterativo
    # ----------------------------
    arbol_dfs_i = g.DFS_iterativa(10)
    g.exportar_arbol_dfs_a_gv(
        arbol_dfs_i,
        "Geografico_DFS_I_500.gv"
    )


# Punto de entrada estándar
if __name__ == "__main__":
    main()
