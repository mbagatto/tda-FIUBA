# Implementar una función (que utilice división y conquista) de orden O(n logn) que dado un arreglo de n números enteros devuelva
# true o false según si existe algún elemento que aparezca más de la mitad de las veces. Justificar el orden de la solución.

def mas_de_la_mitad(arr):
    return mas_de_la_mitad_rec(arr, 0, len(arr) - 1) is not None

def mas_de_la_mitad_rec(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio]

    medio = (inicio + fin) // 2

    izq = mas_de_la_mitad_rec(arr, inicio, medio)
    der = mas_de_la_mitad_rec(arr, medio + 1, fin)

    count_i = count_d = 0
    for i in range(inicio, fin + 1):
        if arr[i] == izq:
            count_i += 1
        if arr[i] == der:
            count_d += 1

    if count_i > (fin - inicio + 1) // 2:
        return izq
    if count_d > (fin - inicio + 1) // 2:
        return der
    return None
