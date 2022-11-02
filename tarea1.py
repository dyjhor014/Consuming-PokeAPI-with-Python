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

    def cargar_libros():
        return print(data.iloc[0:3])

    def listar_libros():
        return print(data)

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

opcion_elegida = str(input("\nIngresa un número\n"))
while opcion_elegida not in ("1","2","3","4","5","6","7","8","9","10"):
    opcion_elegida = str(input("Debes ingresar uno de los números del menú del 1 al 10. Ingresa nuevamente tu respuesta\n"))
if opcion_elegida == "1":
    Libro.cargar_libros()
if opcion_elegida == "2":
    Libro.listar_libros()
if opcion_elegida == "4":
    id_eliminar = int(input("Ingresa el id del libro que deseas eliminar\n"))
    Libro.eliminar_libro(id_eliminar)