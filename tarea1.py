import os
import csv
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
while opcion_elegida not in ("1","2","3","4","5","6","7","8","9","10"):
    opcion_elegida = str(input("Debes ingresar números del 1 al 10. Ingrese nuevamente:\n"))



data = pd.read_csv('libros.csv', index_col = 'id_libro')




#Opcion 9
if opcion_elegida == "9":
    print("\nEdición y actualización de datos")
    print (data)
    id_e = int(input("\nIngrese el ID del libro a editar: "))
    print("\nQue dato del libro desea actualizar:\nTitulo -> t\nGénero -> g\nISBN -> i \nEditorial -> e \nAutor -> a")
    actualizar = input("Ingrese la letra minúscula correspondiente: ")
    if actualizar == "t":
        titulo_a = input("Ingrese el nuevo título: ")
        data.at[id_e,'titulo'] = titulo_a
        print("\n****Se ha actualizado el título con éxito****")
        print(data)

    elif actualizar == "g":
        genero_a = input("Ingrese el nuevo género: ")
        data.at[id_e,'genero'] = genero_a
        print("\nSe ha actualizado el género con éxito")
        print(data)

    elif actualizar == "i":
        genero_a = input("Ingrese el nuevo ISBN: ")
        data.at[id_e,'isbn'] = genero_a
        print("\nSe ha actualizado el ISN con éxito")
        print(data)

    elif  actualizar == "e":
        editorial_e = input("Ingrese la nueva editorial: ")
        data.at[id_e,'editorial'] = editorial_e
        print("\n****Se ha actualizado la editorial con éxito****")
        print(data)

    elif actualizar == "a":
        autor_e = input("Ingrese el nuevo autor(es): ")
        data.at[id_e,'autor'] = autor_e
        print("\n****Se ha actualizado el autor(es) con éxito****")
        print(data)



#Opcion 10
if opcion_elegida == "10":
    
    cantidad = int(input("Ingrese la cantidad de libros a guardar: "))
    with open ('libros.csv', 'a', newline='') as archivo_csv:
        writer = csv.writer(archivo_csv, delimiter=',')
        for i in range (cantidad):
            titulo_i = input("Ingrese el título del libro: ") 
            genero_i = input( "Ingrese el género del libro: ")
            isbn_i = input("Ingrese el ISBN del libro: ")
            editorial_i = input("Ingrese la editorial: ")
            autores_i = input("Ingrese el autor(es) del libro: ")
            lista_i = [len(data)+1, titulo_i, genero_i, isbn_i, editorial_i, autores_i]
            writer.writerow(lista_i)

    print(f"Se agregaron {cantidad} libro(s). ")
