import tkinter as tk
import time
import random
from algoritmo import planificar_trayectoria
from escenas import laberintos

class InterfazGrafica:
    def __init__(self, master, laberinto):
        self.master = master
        self.master.title("Planificación de Trayectorias")
        self.laberinto = laberinto
        self.dimension_x = len(laberinto)
        self.dimension_y = len(laberinto[0])

        self.inicio = None
        self.objetivo = None

        self.punto_tamano = 30 

        self.canvas = tk.Canvas(self.master, width=self.dimension_y * self.punto_tamano, height=self.dimension_x * self.punto_tamano, bg='white')
        self.canvas.pack()

        self.dibujar_laberinto()
        self.inicializar_puntos()

        self.dibujar_puntos()

        self.boton_planificar = tk.Button(self.master, text="Planificar Trayectoria", command=self.planificar_trayectoria)
        self.boton_planificar.pack()

        self.boton_reiniciar = tk.Button(self.master, text="Reiniciar", command=self.reiniciar)
        self.boton_reiniciar.pack()


    def inicializar_puntos(self):
        # Obtener todas las posiciones válidas en el laberinto
        posiciones_validas = [(i, j) for i in range(self.dimension_x) for j in range(self.dimension_y) if self.laberinto[i][j] != '#']

        # Seleccionar posiciones aleatorias para T y S
        self.inicio = random.choice(posiciones_validas)
        posiciones_validas.remove(self.inicio)
        self.objetivo = random.choice(posiciones_validas)

        if self.inicio is None or self.objetivo is None:
            raise ValueError("Error: No se encontraron los puntos de inicio (T) y/o salida (S) en el laberinto.")

    def dibujar_laberinto(self):
        for i in range(self.dimension_x):
            for j in range(self.dimension_y):
                if self.laberinto[i][j] == '#':
                    self.canvas.create_rectangle(j * self.punto_tamano, i * self.punto_tamano, (j + 1) * self.punto_tamano, (i + 1) * self.punto_tamano, fill='gray')

    def dibujar_puntos(self):
        x1, y1 = self.inicio
        x2, y2 = self.objetivo
        self.canvas.create_oval(y1 * self.punto_tamano, x1 * self.punto_tamano, (y1 + 1) * self.punto_tamano, (x1 + 1) * self.punto_tamano, fill='green')
        self.canvas.create_oval(y2 * self.punto_tamano, x2 * self.punto_tamano, (y2 + 1) * self.punto_tamano, (x2 + 1) * self.punto_tamano, fill='red')

    def planificar_trayectoria(self):
        trayectoria = planificar_trayectoria(self.inicio, self.objetivo, self.laberinto)

        if trayectoria:
            self.dibujar_trayectoria_animada(trayectoria)
            print("Coordenadas de la ruta:", trayectoria)
        else:
            print("No se encontró una trayectoria válida.")

    def dibujar_trayectoria_animada(self, trayectoria):
        for punto in trayectoria:
            x, y = punto
            self.canvas.create_rectangle(y * self.punto_tamano, x * self.punto_tamano, (y + 1) * self.punto_tamano, (x + 1) * self.punto_tamano, fill='blue')
            self.master.update()
            time.sleep(0.2)  # Retraso de 0.2 segundos entre cada movimiento

    def reiniciar(self):
        # Seleccionar un laberinto aleatorio
        nuevo_laberinto = random.choice(laberintos)
        self.laberinto = nuevo_laberinto

        # Actualizar dimensiones
        self.dimension_x = len(self.laberinto)
        self.dimension_y = len(self.laberinto[0])

        # Limpiar canvas
        self.canvas.delete("all")

        # Actualizar tamaño del lienzo
        self.canvas.config(width=self.dimension_y * self.punto_tamano, height=self.dimension_x * self.punto_tamano)

        # Inicializar puntos
        self.inicializar_puntos()

        # Dibujar nuevo laberinto y puntos
        self.dibujar_laberinto()
        self.dibujar_puntos()

