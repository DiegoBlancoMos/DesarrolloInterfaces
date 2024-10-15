import tkinter as tk

def mostrar_contenido():
    contenido = entry.get()
    etiqueta_mostrada.config(text=f"Contenido: {contenido}")

def borrar_contenido():
    entry.delete(0, tk.END)
    etiqueta_mostrada.config(text="")
    
root = tk.Tk()
root.title("Ejercicio 8")
root.geometry("400x250")

#CREAMOS EL FRAME SUPERIOR
frame_superior = tk.Frame(root)
frame_superior.pack(pady=10)

#ETIQUETAS EN EL FRAME SUPERIOR
etiqueta1 = tk.Label(frame_superior, text="Etiqueta 1:")
etiqueta1.pack(side=tk.LEFT)
etiqueta2 = tk.Label(frame_superior, text="Etiqueta 2:")
etiqueta2.pack(side=tk.LEFT)

#ENTRY EN EL FRAME SUPERIOR
entry = tk.Entry(frame_superior)
entry.pack(side=tk.LEFT)

#CREAMOS EL FRAME INFERIOR
frame_inferior = tk.Frame(root)
frame_inferior.pack(pady=10)

# Botones en el Frame inferior
boton_mostrar = tk.Button(frame_inferior, text="Mostrar", command=mostrar_contenido)
boton_mostrar.pack(side=tk.LEFT, padx=5)

boton_borrar = tk.Button(frame_inferior, text="Borrar", command=borrar_contenido)
boton_borrar.pack(side=tk.LEFT, padx=5)

# Etiqueta para mostrar el contenido
etiqueta_mostrada = tk.Label(root, text="")
etiqueta_mostrada.pack(pady=10)

# Iniciar el bucle principal de la interfaz
root.mainloop()