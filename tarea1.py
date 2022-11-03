import os
from csv import writer
import pandas as pd
os.system("clear")

#Cargamos el CSV con PANDAS
data = pd.read_csv('libros.csv', index_col='id_libro')

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
    
    def agregar_libro():
        print("Ingrese los datos para agregar libro")
        print("*"*50)
        # Lista para agregar al CSV
        new_libro = [len(data.index)+1,input("Ingresa el titulo del libro\n"),input("Ingresa el genero\n"),int(input("Ingresa el isbn\n")),input("Ingresa la editorial\n"),input("Ingresa el autor\n")]
        with open('libros.csv', 'a', newline='') as f_object:
            writer_object = writer(f_object)
            writer_object.writerow(new_libro)
            f_object.close()
        return print(f"\n{'*'*20}Se agregó el siguiente libro:{'*'*30}\nId: {new_libro[0]}\nTitulo: {new_libro[1]}\nGénero: {new_libro[2]}\nIsbn: {new_libro[3]}\nEditorial: {new_libro[4]}\nAutor: {new_libro[5]}")

    def mostrar_libro(self):
        return print(f"El libros es: {self.titulo}")

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
    
    def buscar_libro1():
        print("Buscar libro por isbn o titulo")
        buscar = input("Desea buscar por isbn (i) o por titulo (t)\n").lower()
        while buscar not in ("i","t"):
            buscar = input("Debes ingresar (i) por isbn  o (t) por titulo\n").lower()
        if buscar == "i":
            isbn = int(input("Ingresa el número de isbn\n"))
            buscar_isbn = data[data["isbn"] == isbn]
            return print(f"{'*'*30}\nEl libro buscado es:\n {buscar_isbn}\n")

        if  buscar == "t":
            titulo = input("Ingresa el titulo del libro\n")
            buscar_titulo = data[data["titulo"].str.contains(titulo)]
            return print(f"{'*'*30}\nEl libro buscado es:\n {buscar_titulo}\n")
    
    def ordenar_libros():
        return print(f"Libros ordenados por titulo:\n{'*'*30}\n{data.sort_values(by=['titulo'])}\n{'*'*30}")
    
    def buscar_libros2():
        print("Buscar libros por autor, editorial o género")
        buscar = input("Desea buscar por autor (a), editorial (e) o genero (g)\n").lower()
        while buscar not in ("a","e","g"):
            buscar = input("Debes ingresar (a) por autor, (e) por editorial  o (g) por genero\n\n").lower()
        if buscar == "a":
            autor = input("Ingresa el nombre del autor\n")
            buscar_autor = data[data["autor"].str.contains(autor)]
            print(autor)
            return print(buscar_autor)
        if buscar == "e":
            editorial = input("Ingresa el nombre de la editorial\n")
            buscar_editorial = data[data["editorial"].str.contains(editorial)]
            return print(buscar_editorial)
        if buscar == "g":
            genero = input("Ingresa el nombre del genero\n")
            buscar_genero = data[data["genero"].str.contains(genero)]
            return print(buscar_genero)
            
opcion_elegida = str(input("\nIngresa un número\n"))
while opcion_elegida not in ("1","2","3","4","5","6","7","8","9","10"):
    opcion_elegida = str(input("Debes ingresar uno de los números del menú del 1 al 10. Ingresa nuevamente tu respuesta\n"))
if opcion_elegida == "1":
    Libro.cargar_libros()
if opcion_elegida == "2":
    Libro.listar_libros()
if opcion_elegida == "3":
    Libro.agregar_libro()
if opcion_elegida == "4":
    id_eliminar = int(input("Ingresa el id del libro que deseas eliminar\n"))
    Libro.eliminar_libro(id_eliminar)
if opcion_elegida == "5":
    Libro.buscar_libro1()
if opcion_elegida == "6":
    Libro.ordenar_libros()
if opcion_elegida == "7":
    Libro.buscar_libros2()