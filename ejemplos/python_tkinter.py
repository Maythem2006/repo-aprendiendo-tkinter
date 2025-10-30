# OBLIGATORIO: Importar la libreria tkinter
from tkinter import *
from tkinter import ttk
# OBTENER LA RUTA DEL SCRIPT DE PYTHON
import os

# Ruta de nuestro script
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

#OBLIGATORIO: Inicializar TKINTER
root = Tk = Tk()

# Configuracion general
root.title("TI3021-P13-C3")
icon = PhotoImage(
        file=os.path.join(script_dir, "icon.png")
    )
root.iconphoto(True, icon)

# Crear un lienzo. Contexto, estilizacion.
frame1: Frame = ttk.Frame( root, padding=10 )

# OBLIGATORIO: Mantener el ciclo de vida
root.mainloop()