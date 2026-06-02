from main import *

def MenuCascada():
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    archivo_menu = tk.Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Archivo", menu=archivo_menu)

    archivo_menu.add_command(label="Equipo")
    archivo_menu.add_separator()
    archivo_menu.add_command(label="Salir", command=root.quit)