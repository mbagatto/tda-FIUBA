# Se tiene un sistema monetario (ejemplo, el nuestro). Se quiere dar "cambio" de una
# determinada cantidad de plata. Implementar un algoritmo que devuelva el cambio pedido,
# usando la minima cantidad de monedas/billetes.

def ordenar_mayor_a_menor(monedas):
    return sorted(monedas, reverse=True)

def cambio(monedas, monto):
    monedas_ord = ordenar_mayor_a_menor(monedas)
    cambio_a_dar = []
    remanente = monto
    for moneda in monedas_ord:
        if moneda <= remanente:
            cambio_a_dar.append(moneda)
            remanente -= moneda
            while moneda <= remanente:
                cambio_a_dar.append(moneda)
                remanente -= moneda
    return cambio_a_dar
