# En Wakanda, tenemos unos productos dados por un arreglo R, donde R[i] nos dice el precio
# del producto. Cada día podemos y debemos comprar uno (y sólo uno) de los productos, pero Wakanda
# está atravesando una era de deflación y los precios disminuyen a diario. El precio del producto
# i el día j+1 es exactamente la mitad del precio en el día j. El arreglo R[i] indica todos los precios
# del primer día. Si bien para reducir costos se debería esperar a que los productos sigan bajando,
# los tiempos de entrega no nos permiten esperar, y cada día debemos comprar uno de los productos.
# Implementar un algoritmo greedy que nos indique el precio mínimo al que podemos comprar
# todos los productos.

def ordenar_menor_a_mayor(precios):
    return sorted(precios)

def precios_deflacion(R):
    precios_ordenados = ordenar_menor_a_mayor(R)
    precio_minimo = 0

    for j in range(0, len(R)):
        precio_minimo += precios_ordenados[j] / (2 ** j)

    return precio_minimo