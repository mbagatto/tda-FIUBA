# Dado un arreglo de n enteros (no olvidar que pueden haber números negativos), encontrar
# el subarreglo contiguo de máxima suma, utilizando División y Conquista.
# Indicar y justificar la complejidad del algoritmo. Ejemplos:
#
# [5, 3, 2, 4, -1] ->  [5, 3, 2, 4]
# [5, 3, -5, 4, -1] ->  [5, 3]
# [5, -4, 2, 4, -1] -> [5, -4, 2, 4]
# [5, -4, 2, 4] -> [5, -4, 2, 4]
# [-3, 4, -1, 2, 1, -5] -> [4, -1, 2, 1]

def max_subarray(arr):
    suma_max, inicio_max, fin_max = max_subarray_rec(arr, 0, len(arr) - 1)
    return arr[inicio_max : fin_max + 1]

def max_subarray_rec(arr, inicio, fin):
    if inicio == fin:
        return arr[inicio], inicio, fin

    medio = (inicio + fin) // 2

    suma_izq, inicio_izq, fin_izq = max_subarray_rec(arr, inicio, medio)
    suma_der, inicio_der, fin_der = max_subarray_rec(arr, medio + 1, fin)

    max_suma_izq = arr[medio]
    suma = 0
    for i in range(medio, inicio - 1, -1):
        suma += arr[i]
        max_suma_izq = max(max_suma_izq, suma)
        if suma == max_suma_izq:
            max_indice_izq = i

    max_suma_der = arr[medio + 1]
    suma = 0
    for i in range(medio + 1, fin + 1):
        suma += arr[i]
        max_suma_der = max(max_suma_der, suma)
        if suma == max_suma_der:
            max_indice_der = i

    suma_arr_entero = max_suma_izq + max_suma_der

    if suma_izq >= suma_der and suma_izq >= suma_arr_entero:
        return suma_izq, inicio_izq, fin_izq
    elif suma_der >= suma_izq and suma_der >= suma_arr_entero:
        return suma_der, inicio_der, fin_der
    else:
        return suma_arr_entero, max_indice_izq, max_indice_der
