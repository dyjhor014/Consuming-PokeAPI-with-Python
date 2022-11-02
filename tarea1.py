import os
from csv import writer
import pandas as pd
os.system("clear")

#Creamos la clase libro
class Libro:

    def __init__(self, id, titulo, genero, isbn, editorial, autor) -> None:
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.editorial = editorial
        self.autor = autor
    
    def registrar_libros(self):
        return print("Esta funcion registra libros")

    
# Menú interactivo
print("*"*50)
print("Bienvenido al programa de registro de libros:\n")
print("Opción (1): Cargar los tres primeros libros listados")
print("Opción (2): Listar libros.")
print("Opción (3): Agregar libros.")
print("Opción (4): Eliminar libro.")
print("Opción (5): Buscar libro por ISBN o por título.")
print("Opción (6): Ordenar libros por título.")
print("Opción (7): Buscar libros por autor, editorial o género.")
print("Opción (8): Buscar libros por número de autores.")
print("Opción (9): Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).")
print("Opción (10): Guardar libros en archivo local.")

opcion_elegida = str(input("\nIngrese el número acorde a su solicitud:\n"))

