import tkinter as tk
import random
from interfaz import InterfazGrafica
from escenas import laberintos

if __name__ == "__main__":
    laberinto_seleccionado = random.choice(laberintos)
    root = tk.Tk()
    app = InterfazGrafica(root, laberinto_seleccionado)
    root.mainloop()