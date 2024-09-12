# Las bolsas de un supermercado se cobran por separado y soportan hasta un peso máximo P, por encima del cual se rompen.
# Implementar un algoritmo greedy que, teniendo una lista de pesos de n productos comprados, encuentre la mejor forma de distribuir
# los productos en la menor cantidad posible de bolsas. Realizar el seguimiento del algoritmo propuesto para bolsas con peso máximo 5
# y para una lista con los pesos: [ 4, 2, 1, 3, 5 ]. ¿El algoritmo implementado encuentra siempre la solución óptima? Justificar.
# Indicar y justificar la complejidad del algoritmo implementado.

def bolsas(capacidad, productos):
    productos_ord = ordenar_mayor_a_menor(productos)
    bolsas = []
    for p in productos_ord:
        guardado = False
        for bolsa in bolsas:
            if sum(bolsa) + p <= capacidad:
                bolsa.append(p)
                guardado = True
                break
        if not guardado:
            bolsas.append([p])
    return bolsas

def ordenar_mayor_a_menor(productos):
    return sorted(productos, reverse=True)
