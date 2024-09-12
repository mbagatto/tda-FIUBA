# Implementar un algoritmo que, por división y conquista, permita obtener la parte entera de la
# raíz cuadrada de un número n, en tiempo O(log n). Por ejemplo, para n = 10 debe devolver 3,
# y para n = 25 debe devolver 5. Justificar el orden del algoritmo.

def parte_entera_raiz(n):
    return parte_entera_raiz_rec(n, 0, n)

def parte_entera_raiz_rec(n, inicio, fin):
    if inicio > fin:
        return fin
    medio = (inicio + fin) // 2
    medio_al_cuadrado = medio * medio
    if medio_al_cuadrado == n:
        return medio
    elif medio_al_cuadrado < n:
        return parte_entera_raiz_rec(n, medio + 1, fin)
    elif medio_al_cuadrado > n:
        return parte_entera_raiz_rec(n, inicio, medio - 1)


print(parte_entera_raiz(10))