# Un Vertex Cover de un Grafo G es un conjunto de vértices del grafo en el cual todas las aristas del grafo tienen al menos uno de sus extremos en dicho conjunto.
# Por ejemplo, el conjunto de todos los vértices del grafo siempre será un Vertex Cover.
# Implementar un algoritmo que dado un Grafo no dirigido nos devuelva un conjunto de vértices que representen un mínimo Vertex Cover del mismo.

from utils.Grafo import Grafo

def vertex_cover_min(grafo):
    vertices = grafo.obtener_vertices()
    sol_optima = set(vertices)
    solucion_parcial = set()
    return list(_vertex_cover_min_bt(grafo, vertices, 0, solucion_parcial, sol_optima))

def _vertex_cover_min_bt(grafo, vertices, indice_actual, solucion_parcial, sol_optima):
    if len(solucion_parcial) >= len(sol_optima):
        return sol_optima
    if es_vertex_cover(grafo, solucion_parcial):
        return set(solucion_parcial)
    if indice_actual == len(vertices):
        return sol_optima

    v = vertices[indice_actual]
    solucion_parcial.add(v)
    sol_optima = _vertex_cover_min_bt(grafo, vertices, indice_actual + 1, solucion_parcial, sol_optima)
    solucion_parcial.remove(v)

    return _vertex_cover_min_bt(grafo, vertices, indice_actual + 1, solucion_parcial, sol_optima)

def es_vertex_cover(grafo, conjunto):
    aristas = obtener_aristas(grafo)
    for u, v in aristas:
        if u not in conjunto and v not in conjunto:
            return False
    return True

def obtener_aristas(grafo):
    aristas = []
    vertices = grafo.obtener_vertices()
    for v in vertices:
        for w in grafo.adyacentes(v):
            if (w, v) not in aristas:
                aristas.append((v, w))
    return aristas
