# Implementar un algoritmo que, utilizando programación dinámica, obtenga el valor del n-ésimo número de fibonacci.
# Indicar y justificar la complejidad del algoritmo implementado.

def fibonacci(n):
    if n == 0:
        return 0
    M_FIB = [None] * (n+1)
    return _fibonacci_dinamico(n, M_FIB)

def _fibonacci_dinamico(n, M_FIB):
    if n <= 1:
        return 1

    if M_FIB[n-1] is None:
        M_FIB[n-1] = _fibonacci_dinamico(n-1, M_FIB)
    if M_FIB[n-2] is None:
        M_FIB[n-2] = _fibonacci_dinamico(n-2, M_FIB)
    M_FIB[n] = M_FIB[n-1] + M_FIB[n-2]
    return M_FIB[n]

if __name__ == '__main__':
    print(fibonacci(5))