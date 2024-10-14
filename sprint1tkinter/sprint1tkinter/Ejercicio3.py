import tkinter as tk

def saludar():
    nombre = entrada.get()
    saludo=tk.Label(root,text=f"Hola {nombre}")
    saludo.pack()

root =tk.Tk()
root.title("Ejercicio 3")
root.geometry("300x200")

etiqueta = tk.Label(root, text="Introduzca su nombre")
etiqueta.pack()

entrada = tk.Entry(root, width=30)
entrada.pack(pady = 5)

boton = tk.Button(root, text= "Aceptar", command=saludar)
boton.pack()


root.mainloop()