import tkinter as tk

class NotasModel:
    def __init__(self):
        self.notas = []

    def agregar_notas(self,nueva_nota):

        self.notas.append(nueva_nota)

    def eliminar_nota(self,i):

       del self.notas[i]

    def obtener_notas(self):

        return self.notas

    def guardar_notas(self):
        with open('notas.txt' , 'w') as archivo:
            for nota in self.notas:
                archivo.write(nota + '\n')
        archivo.close()

    def cargar_notas(self):
        with open('notas.txt', 'r') as archivo:
            # Lee cada línea, aplicando strip() para eliminar el salto de línea
            self.notas = [linea.strip() for linea in archivo.readlines()]
        archivo.close()
