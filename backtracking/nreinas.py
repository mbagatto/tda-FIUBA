# Dado un tablero de ajedrez n x n, implementar un algoritmo por backtracking que ubique (si es posible)
# a n reinas de tal manera que ninguna pueda comerse con ninguna.

from utils.Grafo import Grafo

def nreinas(n):
    grafo = generar_grafo(n)
    if len(grafo.obtener_vertices()) == 1:
        return [(0, 0)]
    return ubicacion(grafo, n)

def ubicacion(grafo, n):
    puestos = set()
    vertices = grafo.obtener_vertices()
    _ubicacion_bt(grafo, vertices, 0, puestos, n)
    return puestos

def _ubicacion_bt(grafo, vertices, indice , puestos, n):
    if len(vertices) == 1:
        return True
    if indice == len(vertices):
        return False
    if len(puestos) == n:
        return True

    v = vertices[indice]
    puestos.add(v)
    if es_compatible(grafo, puestos, v) and _ubicacion_bt(grafo, vertices, indice + 1, puestos, n):
        return True
    puestos.remove(v)
    return _ubicacion_bt(grafo, vertices, indice + 1, puestos, n)

def es_compatible(grafo, puestos, ultimo_puesto):
    for w in puestos:
        if ultimo_puesto == w: continue
        if grafo.estan_unidos(w, ultimo_puesto):
            return False
    return True

def generar_grafo(n):
    grafo = Grafo()
    for i in range(n):
        for j in range(n):
            grafo.agregar_vertice((i, j))

    # Agrego adyacencia por fila
    for i in range(n):
        for j in range(n):
            for k in range(j + 1, n):
                grafo.agregar_arista((i, j), (i, k))

    # Agrego adyacencia por columna
    for j in range(n):
        for i in range(n):
            for k in range(i + 1, n):
                grafo.agregar_arista((i, j), (k, j))

    # Agrego adyacencia por diagonales
    for i in range(n):
        for j in range(n):
            for k in range(i):
                if k < j:
                    grafo.agregar_arista((i, j), (i - k - 1, j - k - 1))
                if k + j + 1 < n:
                    grafo.agregar_arista((i, j), (i - k - 1, j + k + 1))
    return grafo
