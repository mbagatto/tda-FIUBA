# Tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio del producto.
# Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero vivimos en una
# era de inflación y los precios aumentan a diario. El precio del producto i el día j es
# R[i]^{j + 1} (j comenzando en 0). Implementar un algoritmo greedy que nos indique
# el precio mínimo al que podemos comprar todos los productos.
# Indicar y justificar la complejidad del algoritmo implementado.

def ordenar_mayor_a_menor(precios):
    return sorted(precios, reverse=True)

def precios_inflacion(R):
    precios_ord = ordenar_mayor_a_menor(R)
    precio_minimo = 0

    for j in range(0, len(R) - 1):
        precio_minimo += precios_ord[j] ** (j + 1)

    return precio_minimo
