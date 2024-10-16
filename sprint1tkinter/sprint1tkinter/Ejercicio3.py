import tkinter as tk

#FUNCIÓN QUE NOS COGE EL NOMBRE INTRODUCIDO EN EL ENTRY y realiza un saludo
def saludar():
    nombre = entrada.get()
    saludo=tk.Label(root,text=f"Hola {nombre}")
    saludo.pack()

#CREAMOS LA VENTANA PRINCIPAL
root =tk.Tk()
root.title("Ejercicio 3")
root.geometry("300x200")

#CREAMOS LA ETIQUETA
etiqueta = tk.Label(root, text="Introduzca su nombre")
etiqueta.pack()

#CREAMOS EL ENTRY
entrada = tk.Entry(root, width=30)
entrada.pack(pady = 5)

#CREAMOS BOTÓN PARA INICIAR EL SALUDO
boton = tk.Button(root, text= "Aceptar", command=saludar)
boton.pack()

#INICIAR EL BUCLE PRINCIPAL
root.mainloop()