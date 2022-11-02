import os
from csv import writer
import pandas as pd
os.system("clear")

#Cargamos el CSV con PANDAS
data = pd.read_csv('libros.csv', index_col='id_libro')
new_data = data

#Creamos la clase libro#
class Libro:

    def __init__(self, id, titulo, genero, isbn, editorial, autor) -> None:
        self.id = id
        self.titulo = titulo
        self.genero = genero
        self.isbn = isbn
        self.editorial = editorial
        self.autor = autor

    def agregar_libro(self):
        return print("Agregar libro")

    def eliminar_libro(self):
        answer_pos = data[data.index == id_eliminar]
        answer_list = list(answer_pos.index)
        confirma = input(f"¿Está seguro que desea eliminar el siguiente libro?:\n{'*'*90}\n{answer_pos}\n{'*'*90}\nIngresa S o N (Si/No)").lower()
        index_answer = int(answer_list[0])
        if confirma == "s":
            new_data = data.drop(index_answer)
            new_data.to_csv("libros.csv", index=True)
            return print(new_data)
        else:
            return print("Cancelaste la operacion")

#FUNCIONES DEL PROGRAMA
def leer_archivo():
    return print(data.iloc[0:3])
    
def listar_libros():
    return print(data)

def buscar_libro_isbn_titulo():
    return print("Buscar libro por ISBN o por título. Se debe sugerir las opciones y listar el resultado")

def ordenar_libros():
    return print("Ordenar libros por título.")

def buscar_libro_autor_editorial_genero():
    return print("Buscar libros por autor, editorial o género. Se deben sugerir las opciones y listar los resultados.")

def buscar_libro_num_autores():
    return print("Buscar libros por número de autores. Se debe ingresar un número por ejemplo 2 (hace referencia a dos autores) y se deben listar todos los libros que contengan 2 autores.")

def actualizar_datos_libro():
    return print("Editar o actualizar datos de un libro (título, género, ISBN, editorial y autores).")

def guardar_libro():
    return print("Guardar libros en archivo de disco duro (.txt o csv).")

libro = Libro(2,"la ciudad y los perros","novela",987654321,"la imprenta","Mario Vargas Llosa")
id_eliminar = int(input("Ingresa el id del libro que deseas eliminar\n"))
Libro.eliminar_libro(id_eliminar)