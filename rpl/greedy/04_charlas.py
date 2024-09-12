# Tengo una sala donde quiero dar charlas. Las charlas tienen horario de inicio y fin.
# Quiero utilizar la sala para dar la mayor cantidad de charlas.

INICIO = 0
FIN = 1

def ordenar_por_horario_fin(horarios):
    return sorted(horarios, key=lambda h: h[FIN])

def charlas(horarios):
    horarios_ordenados = ordenar_por_horario_fin(horarios)
    charlas_a_dar = []
    for horario in horarios_ordenados:
        if len(charlas_a_dar) == 0 or not hay_interseccion(charlas_a_dar[-1], horario):
            charlas_a_dar.append(horario)
    return charlas_a_dar

def hay_interseccion(anterior, nueva):
    return anterior[FIN] > nueva[INICIO]
