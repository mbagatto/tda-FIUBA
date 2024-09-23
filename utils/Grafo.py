import random

class Grafo:
    def __init__(self, dirigido=False, vertices_init=[]):
        self.dirigido = dirigido
        self.adj = {}
        for v in vertices_init:
            self.agregar_vertice(v)

    def agregar_vertice(self, v):
        if v not in self.adj:
            self.adj[v] = {}

    def borrar_vertice(self, v):
        if v in self.adj:
            del self.adj[v]
            for u in self.adj:
                if v in self.adj[u]:
                    del self.adj[u][v]

    def agregar_arista(self, v, w, peso=1):
        if v not in self.adj:
            self.agregar_vertice(v)
        if w not in self.adj:
            self.agregar_vertice(w)
        self.adj[v][w] = peso
        if not self.dirigido:
            self.adj[w][v] = peso

    def borrar_arista(self, v, w):
        if v in self.adj and w in self.adj[v]:
            del self.adj[v][w]
        if not self.dirigido and w in self.adj and v in self.adj[w]:
            del self.adj[w][v]

    def estan_unidos(self, v, w):
        return w in self.adj.get(v, {})

    def peso_arista(self, v, w):
        return self.adj[v][w] if self.estan_unidos(v, w) else None

    def obtener_vertices(self):
        return list(self.adj.keys())

    def vertice_aleatorio(self):
        return random.choice(self.obtener_vertices()) if self.adj else None

    def adyacentes(self, v):
        return list(self.adj.get(v, {}).keys())
