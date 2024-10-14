import tkinter as tk

def lanzar_etiqueta():
    etiqueta = tk.Label(root, text="Has pulsado el botón!")
    etiqueta.pack()

root = tk.Tk()
root.title("Ejercicio 2")
root.geometry("300x200")

boton_mostrar = tk.Button(root, text="Pulse aquí!", command=lanzar_etiqueta)
boton_mostrar.pack(pady=20)

boton_cerrar = tk.Button(root, text="Cerrar ventana", command=root.quit)
boton_cerrar.pack(pady=10)
root.mainloop()