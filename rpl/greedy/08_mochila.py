# Tenemos una mochila con una capacidad W (peso, volumen). Hay elementos a guardar.
# Cada elemento tiene un peso y un valor. Queremos maximizar el valor de lo que nos llevamos
# sin pasarnos de la capacidad.

IDX_VALOR = 0
IDX_PESO = 1

def ordenar_por_mayor_relacion_valor_peso(elementos):
    return sorted(elementos, key=lambda e: e[IDX_VALOR]/e[IDX_PESO], reverse=True)

def mochila(elementos, W):
    elementos_ord = ordenar_por_mayor_relacion_valor_peso(elementos)
    elementos_guardados = []
    capacidad_usada = 0
    for elem in elementos_ord:
        if elem[IDX_PESO] + capacidad_usada > W:
            continue
        capacidad_usada += elem[IDX_PESO]
        elementos_guardados.append(elem)
    return elementos_guardados
