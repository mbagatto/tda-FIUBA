# Se tiene un arreglo tal que [1, 1, 1, …, 0, 0, …] (es decir, unos seguidos de ceros).
# Se pide una función de orden O(log(n)) que encuentre el índice del primer 0.
# Si no hay ningún 0 (solo hay unos), debe devolver -1.

def indice_primer_cero(arr):
    if arr[0] == 0:
        return 0
    if arr[-1] == 1:
        return -1

    return indice_primer_cero_rec(arr, 0, len(arr) -1)

def indice_primer_cero_rec(arr, inicio, fin):
    medio = (inicio + fin) // 2
    if arr[medio] == 0 and arr[medio - 1] == 1:
        return medio
    if arr[medio] == 1:
        return indice_primer_cero_rec(arr, medio + 1, fin)
    return indice_primer_cero_rec(arr, 0, medio - 1)
