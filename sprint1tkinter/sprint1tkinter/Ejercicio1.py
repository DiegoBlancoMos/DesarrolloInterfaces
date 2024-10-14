import tkinter as tk

def cambiar_texto():
    etiqueta3.config(text="¡Texto cambiado!")

root = tk.Tk()
root.title("Ejericio 1")
root.geometry("300x200")
etiqueta = tk.Label(root, text="Bienvenido!")
etiqueta.pack()
etiqueta1 = tk.Label(root, text= "Diego Blanco Mosqueira")
etiqueta1.pack()
etiqueta3 = tk.Label(root, text="Texto inicial")
etiqueta3.pack(pady=10)

boton = tk.Button(root, text="Cambia el texto", command=cambiar_texto)
boton.pack(pady=20)

root.mainloop()