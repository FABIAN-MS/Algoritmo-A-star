import heapq
from Nodo import distancia_manhattan, Nodo

def obtener_vecinos(nodo, laberinto):
    vecinos = []
    direcciones = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in direcciones:
        x, y = nodo.x + dx, nodo.y + dy

        if 0 <= x < len(laberinto) and 0 <= y < len(laberinto[0]) and laberinto[x][y] != '#':
            vecinos.append(Nodo(x, y))

    return vecinos

def planificar_trayectoria(inicio, objetivo, laberinto):
    inicio_nodo = Nodo(inicio[0], inicio[1])
    objetivo_nodo = Nodo(objetivo[0], objetivo[1])

    lista_abierta = []
    lista_cerrada = set()

    heapq.heappush(lista_abierta, inicio_nodo)

    while lista_abierta:
        nodo_actual = heapq.heappop(lista_abierta)

        if nodo_actual.x == objetivo_nodo.x and nodo_actual.y == objetivo_nodo.y:
            trayectoria = []
            while nodo_actual:
                trayectoria.append((nodo_actual.x, nodo_actual.y))
                nodo_actual = nodo_actual.padre
            return trayectoria[::-1]

        lista_cerrada.add((nodo_actual.x, nodo_actual.y))

        vecinos = obtener_vecinos(nodo_actual, laberinto)

        for vecino in vecinos:
            if (vecino.x, vecino.y) in lista_cerrada:
                continue

            costo_movimiento = nodo_actual.g + 1

            if vecino not in lista_abierta or costo_movimiento < vecino.g:
                vecino.g = costo_movimiento
                vecino.h = distancia_manhattan(vecino, objetivo_nodo)
                vecino.padre = nodo_actual

                if vecino not in lista_abierta:
                    heapq.heappush(lista_abierta, vecino)

    return None