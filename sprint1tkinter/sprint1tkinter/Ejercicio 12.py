import tkinter as tk
from tkinter import messagebox

def registrar_usuario():
    nombre = entry_nombre.get()
    edad = scale_edad.get()
    genero = var_sexo.get()

    if not nombre or genero == "":
        messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")
        return

    usuario_info = f"{nombre}, Edad: {edad}, Género: {genero}"
    listbox.insert(tk.END, usuario_info)  # Añadir usuario a la lista
    #UNA VEZ AÑADIMOS USUARIO A LA LISTA VACIAMOS LAS VARIABLES PARA ASÍ PODER METER OTRO NUEVO
    entry_nombre.delete(0, tk.END)  # Limpiar el campo de nombre
    scale_edad.set(0)  # Reiniciar la edad
    var_sexo.set(None)  # Reiniciar el género

def actualizar_edad(valor):
    etiqueta_edad.config(text=f"Edad seleccionada: {valor}")#ACTUALIZAMOS EL VALOR DEL LABEL QUE INDICA LA EDAD

def borrar_user():
    selected_user_index = listbox.curselection() #COGEMOS EL ÍNDICE DEL USUARIO SELECCIONADO
    if selected_user_index:
        listbox.delete(selected_user_index)#LO BORRAMOS DE LA LISTA
    else:
        messagebox.showwarning("Advertencia", "Seleccione un usuario para eliminar.")

def salir():
    root.quit()

def guardar_lista():
    messagebox.showinfo("Guardar Lista", "La lista ha sido guardada.")

def cargar_lista():
    messagebox.showinfo("Cargar Lista", "La lista ha sido cargada.")

# Crear la ventana principal
root = tk.Tk()
root.title("Ejercicio 12")
root.geometry("700x500")

#ENTRY PARA INTRODUCIR EL NOMBRE
etiqueta_nombre=tk.Label(root, text="Introduzca su nombre")
etiqueta_nombre.pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

#SCALE PARA INDICAR LA EDAD
scale_edad = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, command=actualizar_edad)
scale_edad.pack(pady=20)
etiqueta_edad=tk.Label(root, text="Edad: 0")
etiqueta_edad.pack()

#VARIABLE CREADA PARA EL RADIOBUTTON, LA INICIMAOS SIN NINGUNA SELECCIÓN Y LE INDICAMOS QUE LA VARIABLE SERÁ DE TIPO STRING
var_sexo = tk.StringVar()
var_sexo.set(None)

#CREAR EL RADIOBUTTON
radio_masc = tk.Radiobutton(root, text="Masculino", variable=var_sexo, value="Masculino")
radio_masc.pack()
radio_fem = tk.Radiobutton(root, text="Femenino", variable=var_sexo, value="Femenino")
radio_fem.pack()
radio_otro = tk.Radiobutton(root, text="Otro", variable=var_sexo, value="Otro")
radio_otro.pack()

#CREAR BOTÓN PARA AÑADIR AL USUARIO A LA LISTA
boton = tk.Button(root, text="Añadir Usuario", command=registrar_usuario)
boton.pack()

#CREAMOS UN FRAME PARA METER LA LISTBOX Y LA SCROLLBAR
frame_lista = tk.Frame(root)
frame_lista.pack(pady=5)

#CREAMOS LA LISTBOX
tk.Label(frame_lista, text="Usuarios Registrados:").pack(pady=5)
listbox = tk.Listbox(frame_lista, width=50, height=10)
listbox.pack(side=tk.LEFT)

#CREAMOS LA SCROLLBAR
scrollbar = tk.Scrollbar(frame_lista,command=listbox.yview)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

#BOTÓN PARA BORRAR USUARIO
boton_borrar = tk.Button(root, text="Borrar Usuario Seleccionado", command=borrar_user)
boton_borrar.pack()

#BOTÓN PARA CERRAR LA VENTANA
boton_salir = tk.Button(root, text="Salir", command=salir)
boton_salir.pack(side=tk.RIGHT)

#CREAR BARRA DEL MENÚ
menu_barra = tk.Menu(root)
root.config(menu=menu_barra)
# CREAMOS DENTRO DEL MENÚ OTRO
menu = tk.Menu(menu_barra, tearoff=0)
menu_barra.add_cascade(label="Lista", menu=menu)
menu.add_command(label="Guardar Lista", command=guardar_lista)
menu.add_separator()
menu.add_command(label="Cargar Lista", command=cargar_lista)

# Iniciar el bucle principal de la interfaz
root.mainloop()
