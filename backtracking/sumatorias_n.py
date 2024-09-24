# Escribir un algoritmo que, utilizando backtracking, dada una lista de enteros positivos L
# y un entero n devuelva todos los subconjuntos de L que suman exactamente n.

def sumatorias_n(lista, n):
    solucion_parcial = []
    resultado = []
    _sumatorias_n_bt(lista, n, 0, solucion_parcial, resultado)
    return resultado

def _sumatorias_n_bt(lista, n, indice_actual, solucion_parcial, resultado):
    if sum(solucion_parcial) == n:
        resultado.append(solucion_parcial.copy())
        return

    if sum(solucion_parcial) > n or indice_actual >= len(lista):
        return

    elemento = lista[indice_actual]
    solucion_parcial.append(elemento)
    _sumatorias_n_bt(lista, n, indice_actual + 1, solucion_parcial, resultado)
    solucion_parcial.pop()
    return _sumatorias_n_bt(lista, n, indice_actual + 1, solucion_parcial, resultado)

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = 12
    print(sumatorias_n(lista, n))
