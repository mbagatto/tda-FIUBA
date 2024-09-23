# Un camino hamiltoniano, es un camino de un grafo, que visita todos los vértices del grafo una sola vez.
# Implementar un algoritmo por backtracking que encuentre un camino hamiltoniano de un grafo dado.

def camino_hamiltoniano(grafo):
    camino = []
    visitados = set()
    for v in grafo.obtener_vertices():
        if camino_hamiltoniano_dfs(grafo, camino, visitados, v):
            return camino
    return None

def camino_hamiltoniano_dfs(grafo, camino, visitados, v_actual):
    camino.append(v_actual)
    visitados.add(v_actual)
    if len(visitados) == len(grafo.obtener_vertices()):
        return True
    for w in grafo.adyacentes(v_actual):
        if w not in visitados:
            if camino_hamiltoniano_dfs(grafo, camino, visitados, w):
                return True
    visitados.remove(v_actual)
    camino.pop()
    return False
