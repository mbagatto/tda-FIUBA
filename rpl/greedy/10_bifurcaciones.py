# Una ruta tiene un conjunto de bifurcaciones para acceder a diferentes pueblos. El listado (ordenado por nombre del pueblo) contiene el número de kilómetro donde
# está ubicada cada una. Se desea ubicar la menor cantidad de policiales (en las bifurcaciones) de tal forma que no haya bifurcaciones con vigilancia a más de 50 km.
# Justificar que la solución es óptima. Indicar y justificar la complejidad del algoritmo implementado.
# Ejemplo:
#
# | Ciudad      | Bifurcación |
# |-------------|-------------|
# | Castelli    | 185         |
# | Gral Guido  | 242         |
# | Lezama      | 156         |
# | Maipú       | 270         |
# | Sevigne     | 194         |
#
# Si pongo un patrullero en la bifurcación de Lezama, cubro Castelli y Sevigne. Pero no Gral Guido y Maipú. Necesitaría en ese caso, poner otro.
# Agrego otro patrullero en Gral Guido. Con eso tengo 2 móviles policiales en bifurcaciones que cubren todas los accesos a todas las ciudades con distancia menor a 50km.
# En un caso alternativo donde solamente se consideren las bifurcaciones de Castelli, Gral Guido y Sevigne, la única solución óptima sería colocar un móvil policial en Sevigne.

IDX_KM = 1

def bifurcaciones_con_patrulla(ciudades):
    ciudades_ord = ordenar_ciudades_por_bifurcacion(ciudades)
    patrulleros = []
    ciudad_a_cubrir = 0
    for i in range(0, len(ciudades_ord) - 1):
        if (i + 1) == len(ciudades_ord) - 1 or ciudades_ord[i + 1][IDX_KM] - ciudades_ord[ciudad_a_cubrir][IDX_KM] > 50:
            patrulleros.append(ciudades_ord[i])
            ciudad_a_cubrir = determinar_ciudad_a_cubrir(ciudades_ord, i)
    return patrulleros

def determinar_ciudad_a_cubrir(ciudades, ultimo_patrullero):
    for i in range(ultimo_patrullero + 1, len(ciudades)):
        if ciudades[i][IDX_KM] - ciudades[ultimo_patrullero][IDX_KM] > 50:
            return i

def ordenar_ciudades_por_bifurcacion(ciudades):
    return sorted(ciudades, key=lambda c: c[IDX_KM])
