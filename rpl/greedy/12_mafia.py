# Trabajamos para el mafioso Arnook, que es quien tiene la máxima influencia y poder en la zona costera de Ciudad República. Allí reina el caos y la delincuencia,
# a tal punto que quien termina organizando las pequeñas mafias locales no es otro sino Arnook. En particular, nos vamos a centrar en unos pedidos que recibe de parte
# de dichos grupos por el control de diferentes kilómetros de la ruta costera. Cada pequeña mafia le pide a Arnook control sobre un rango de kilómetros
# (por ejemplo, la mafia nro 1 le pide del kilómetro 1 al 3.5, la mafia 2 le pide del 3.3333 al 8, etc. . . ).
# Si hay una mafia tomando control de algún determinado kilómetro, no puede haber otra haciendo lo mismo (es decir, no pueden solaparse).
# Cada mafia pide por un rango específico. Arnook no cobra por kilómetraje sino por “otorgar el permiso”, indistintamente de los kilómetros pedidos.
# Ahora bien, esto es una mafia, no una ONG, y no debe rendir cuentas con nadie, así lo único que es de interés es maximizar la cantidad de permisos otorgados
# (asegurándose de no otorgarle algún lugar a dos mafias diferentes). Implementar un algoritmo Greedy que reciba los rangos de kilómetros pedidos por cada mafia,
# y determine a cuáles se les otorgará control, de forma que no hayan dos mafias ocupando mismo territorio, y a su vez maximizando la cantidad de pedidos otorgados.
# Indicar y justificar la complejidad del algoritmo implementado. Justificar por qué el algoritmo planteado es Greedy. ¿El algoritmo da la solución óptima siempre?

IDX_INICIO = 0
IDX_FIN = 1

def asignar_mafias(pedidos):
    pedidos_ord = ordenar_pedidos_por_fin_intervalo(pedidos)
    pedidos_otorgados = []
    for p in pedidos_ord:
        if len(pedidos_otorgados) == 0 or not se_solapan(pedidos_otorgados[-1], p):
            pedidos_otorgados.append(p)

    return pedidos_otorgados

def se_solapan(anterior, nueva):
    return anterior[IDX_FIN] > nueva[IDX_INICIO]


def ordenar_pedidos_por_fin_intervalo(pedidos):
    return sorted(pedidos, key=lambda p: p[IDX_FIN])
