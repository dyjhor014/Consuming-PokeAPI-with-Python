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