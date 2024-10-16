import tkinter as tk

def lanzar_etiqueta():
    etiqueta = tk.Label(root, text="Has pulsado el botón!")
    etiqueta.pack()

#CREAMOS LA VENTANA PRINCIPAL
root = tk.Tk()
root.title("Ejercicio 2")
root.geometry("300x200")

#CREAMOS BOTÓN PARA LANZAR LA ETIQUETA
boton_mostrar = tk.Button(root, text="Pulse aquí!", command=lanzar_etiqueta)
boton_mostrar.pack(pady=20)

#CREAMOS BOTÓN PARA CERRAR LA APLICACIÓN
boton_cerrar = tk.Button(root, text="Cerrar ventana", command=root.quit)
boton_cerrar.pack(pady=10)
root.mainloop()