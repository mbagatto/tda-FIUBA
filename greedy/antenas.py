# Tenemos una ruta recta muy larga, de K kilómetros, sobre la cual hay casas dispersas. En dichas casas vive gente que usa mucho sus celulares.
# El intendente a cargo la ruta debe renovar por completo el sistema de antenas, teniendo que construir sobre la ruta nuevas antenas.
# Cada antena tiene un rango de cobertura de R kilómetros (valor constante conocido).Implementar un algoritmo Greedy
# que reciba las ubicaciones de las casas, en número de kilómetro sobre esta ruta (números reales positivos) desordenadas,
# y devuelva los kilómetros sobre los que debemos construir las antenas para que todas las casas tengan cobertura,
# y se construya para esto la menor cantidad de antenas posibles. Indicar y justificar la complejidad del algoritmo implementado.
# Justificar por qué se trata de un algoritmo greedy. ¿El algoritmo da la solución óptima siempre?

def cobertura(casas, R, K):
    casas_ordenadas = ordenar_casas(casas)
    antenas = []
    for casa in casas_ordenadas:
        if not antenas:
            if casa + R > K:
                antenas.append(K)
                continue
            antenas.append(casa + R)
        if casa - antenas[-1] > R:
            if casa + R > K:
                antenas.append(K)
            else:
                antenas.append(casa + R)
    return antenas

def ordenar_casas(casas):
    return sorted(casas)
