# Un set dominante (Dominating Set) de un grafo G es un subconjunto D de vértices de G, tal que para todo vértice de G:
#  o bien (i) pertenece a D; o bien (ii) es adyacente a un vértice en D.
# Implementar un algoritmo que reciba un Grafo, y devuelva un dominating set de dicho grafo con la mínima cantidad de vértices.

def dominating_set_min(grafo):
    vertices = grafo.obtener_vertices()
    solucion_parcial = set()
    sol_optima = set(vertices)
    return list(dominating_set_rec(grafo, vertices, 0, solucion_parcial, sol_optima))

def dominating_set_rec(grafo, vertices, indice, solucion_parcial, sol_optima):
    if len(solucion_parcial) >= len(sol_optima):
        return sol_optima
    if es_dominating_set(grafo, solucion_parcial):
        return set(solucion_parcial)
    if len(vertices) == indice:
        return sol_optima

    v = vertices[indice]
    solucion_parcial.add(v)
    sol_optima = dominating_set_rec(grafo, vertices, indice + 1, solucion_parcial, sol_optima)
    solucion_parcial.remove(v)

    return dominating_set_rec(grafo, vertices, indice + 1, solucion_parcial, sol_optima)

def es_dominating_set(grafo, solucion_parcial):
    for v in grafo.obtener_vertices():
        if v in solucion_parcial: continue
        tiene_adyacentes = False
        for w in grafo.adyacentes(v):
            if w in solucion_parcial:
                tiene_adyacentes = True
                break
        if not tiene_adyacentes: return False
    return True
