# Implementar un algoritmo que reciba un grafo y un número n que, utilizando backtracking, indique si es posible pintar
# cada vértice con n colores de tal forma que no hayan dos vértices adyacentes con el mismo color.

def colorear(grafo, n):
    coloreados = {}
    vertices = grafo.obtener_vertices()
    return _colorear_bt(grafo, n, vertices, 0, coloreados)

def _colorear_bt(grafo, n, vertices, indice_actual, coloreados):
    if indice_actual == len(vertices):
        return True

    v = vertices[indice_actual]
    for color in range(n):
        if es_coloreo_compatible(grafo, v, color, coloreados):
            coloreados[v] = color
            if _colorear_bt(grafo, n, vertices, indice_actual + 1, coloreados):
                return True
            del coloreados[v]
    return False

def es_coloreo_compatible(grafo, vertice, color, coloreados):
    for w in grafo.adyacentes(vertice):
        if w in coloreados and coloreados[w] == color:
            return False
    return True
