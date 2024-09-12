# Tenemos tareas con una duración y un deadline (fecha límite), pero pueden hacerse en cualquier momento, intentando que se hagan antes del deadline.
# Una tarea puede completarse luego de su deadline, pero ello tendra una penalización de latencia.
# Para este problema, buscamos minimizar la latencia máxima en el que las tareas se ejecuten.
# Es decir, dados los arreglos de: T tiempo de duraciones de las tareas y L representando al deadline de cada tarea, si definimos que una tarea i empieza en S_i,
# entonces termina en F_i = S_i + T_i, y su latencia es L_i = F_i - D_i (si F_i > D_i, sino 0). Nuestra latencia máxima será aquella i que maximice el valor L_i.
# Implementar un algoritmo que defina en qué orden deben realizarse las tareas, sabiendo que al terminar una tarea se puede empezar la siguiente.
# Indicar y justificar la complejidad del algoritmo implementado.
# Devolver un arreglo de tuplas, una tupla por tarea, en el orden en que deben ser realizadas, y que cada tupla indique:
# (el tiempo de la tarea i T_tareas[i] y la latencia resultante L_i de esa tarea).

IDX_DEADLINE = 1

def ordenar_por_deadlines_ascendentemente(tareas):
    return sorted(tareas, key=lambda t: t[IDX_DEADLINE])

def minimizar_latencia(L_deadline, T_tareas):
    tareas = []
    for i in range(len(T_tareas)):
        tareas.append((T_tareas[i], L_deadline[i]))
    tareas_ord = ordenar_por_deadlines_ascendentemente(tareas)
    tiempo_actual = 0
    resultados = []
    for tiempo, deadline in tareas_ord:
        tiempo_final = tiempo_actual + tiempo
        if tiempo_final > deadline:
            resultados.append((tiempo, tiempo_final - deadline))
        else:
            resultados.append((tiempo, 0))
        tiempo_actual = tiempo_final
    return resultados
