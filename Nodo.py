import heapq

class Nodo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.padre = None
        self.g = 0
        self.h = 0

    def __lt__(self, otro):
        return (self.g + self.h) < (otro.g + otro.h)

def distancia_manhattan(nodo_actual, nodo_siguiente):
    return abs(nodo_actual.x - nodo_siguiente.x) + abs(nodo_actual.y - nodo_siguiente.y)