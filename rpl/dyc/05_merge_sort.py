# Implementar Merge Sort. Justificar el orden del algoritmo mediante el teorema maestro.

def merge_sort(arr):
    return merge_sort_rec(arr, 0, len(arr) - 1)

def merge_sort_rec(arr, inicio, fin):
    if inicio >= fin:
        return arr
    medio = (inicio + fin) // 2
    merge_sort_rec(arr, inicio, medio)
    merge_sort_rec(arr, medio + 1, fin)
    merge(arr, inicio, medio, fin)
    return arr

def merge(arr, inicio, medio, fin):
    izq = arr[inicio:medio + 1]
    der = arr[medio + 1: fin + 1]

    i = 0
    j = 0
    k = inicio

    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            arr[k] = izq[i]
            i += 1
        else:
            arr[k] = der[j]
            j += 1
        k += 1

    if i < len(izq):
        arr[k: fin + 1] = izq[i:]
    if j < len(der):
        arr[k: fin + 1] = der[j:]
