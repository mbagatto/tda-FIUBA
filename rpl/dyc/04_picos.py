# Se tiene un arreglo de N >= 3 elementos en forma de pico, esto es: estrictamente creciente
# hasta una determinada posición p, y estrictamente decreciente a partir de ella
# (con 0 < p < N - 1). Por ejemplo, en el arreglo [1, 2, 3, 1, 0, -2] la posición del pico es p = 2.
# Se pide:
# Implementar un algoritmo de división y conquista de orden O(log n) que encuentre la posición p
# del pico: func PosicionPico(v []int, ini, fin int) int. La función será invocada inicialmente como:
# PosicionPico(v, 0, len(v)-1), y tiene como pre-condición que el arreglo tenga forma de pico.
#
# Justificar el orden del algoritmo mediante el teorema maestro.

def posicion_pico(v, ini, fin):
    medio = ((ini + fin) - 1) // 2

    if v[medio - 1] > v[medio] > v[medio + 1]:
        return posicion_pico(v, ini, medio)
    elif v[medio - 1] < v[medio] < v[medio + 1]:
        return posicion_pico(v, medio + 1, fin)
    return medio
