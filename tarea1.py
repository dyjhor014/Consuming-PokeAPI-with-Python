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
            

    def listar_autores(): #Opcion 8
        print("-------Listar libros por número de autores-------\n")         
        lista_libros = list(data['titulo']) #Convertir a lista la columna  titulo
        lista_autores = list(data['autor'])
        numero_autor = str(input("Ingrese el número de autores: "))
        tuplas_libros = list(zip(lista_libros,lista_autores)) #Lista de tuplas de libro : autor
        
        if numero_autor == "1":
            lista_filtrada = [tupla for tupla in tuplas_libros if tupla[1] .__contains__(",") is False ] #Crear lista de tuplas que no contengan el string ","
            print(f"\nLos libros con un autor son: {len(lista_filtrada)}\n")
            for key, value in lista_filtrada:
                print(key,":",value)

        elif numero_autor == "2":
            lista_filtrada = [tupla for tupla in tuplas_libros if tupla[1].__contains__(",") ] #Crear lista de tuplas que contengan el string ","
            print(f"\nLos libros con dos autores son: {len(lista_filtrada)}\n")
            for key, value in lista_filtrada:
                print(key,":",value)

        else:
            print(f"No se encontraron libros con {numero_autor} autores.")
            

    def editar_libros(): #Opcion 9
        print("Edición y Actualización de datos de libros")
        print(data)
        id_e = int(input("\nIngrese el ID del libro a editar: "))

        print("\nQue dato del libro desea actualizar:\nTitulo -> t\nGénero -> g\nISBN -> i \nEditorial -> e \nAutor -> a")
        actualizar = input("\nIngrese la letra minúscula correspondiente: ")

        if actualizar == "t":
            titulo_a = input("Ingrese el nuevo título: ")
            data.at[id_e,'titulo'] = titulo_a  
            print("****Se ha actualizado el título con éxito****")
            data.to_csv("libros.csv")
            print(data)
        
        elif actualizar == "g":
            genero_a = input("Ingrese el nuevo género: ")
            data.at[id_e,'genero'] = genero_a
            print("****Se ha actualizado el género con éxito****")
            data.to_csv("libros.csv")
            print(data)

        elif actualizar == "i":
            genero_a = input("Ingrese el nuevo ISBN: ")
            data.at[id_e,'isbn'] = genero_a
            print("****Se ha actualizado el ISN con éxito****")
            data.to_csv("libros.csv")
            print(data)

        elif  actualizar == "e":
            editorial_e = input("Ingrese la nueva editorial: ")
            data.at[id_e,'editorial'] = editorial_e
            print("****Se ha actualizado la editorial con éxito****")
            data.to_csv("libros.csv")
            print(data)

        elif actualizar == "a":
            autor_e = input("Ingrese el nuevo autor(es): ")
            data.at[id_e,'autor'] = autor_e
            print("****Se ha actualizado el autor(es) con éxito****")
            data.to_csv("libros.csv")
            print(data)


    def guardar_libros(): #Opcion10 
        print("Guardar libros en archivo local")
        cantidad = int(input("Ingrese la cantidad de libros a guardar: "))
        with open ('libros.csv', 'a', newline='') as f_object:
         for i in range (cantidad):
            titulo_i = input("Ingrese el título del libro: ") 
            genero_i = input( "Ingrese el género del libro: ")
            isbn_i = input("Ingrese el ISBN del libro: ")
            editorial_i = input("Ingrese la editorial: ")
            autores_i = input("Ingrese el autor(es) del libro: ")
            lista_i = [len(data)+1, titulo_i, genero_i, isbn_i, editorial_i, autores_i]
            writer_objetc = writer(f_object)
            writer_objetc.writerow(lista_i) 

        print(f"Se agregaron {cantidad} libro(s).")


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
while opcion_elegida not in ("1","2","3","4","5","6","7","8","9","10"):
    opcion_elegida = str(input("Debes ingresar números del 1 al 10. Ingrese nuevamente:\n"))

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
if opcion_elegida == "8":
    Libro.listar_autores()
if opcion_elegida == "9":
    Libro.editar_libros()
if opcion_elegida == "10":
    Libro.guardar_libros()
