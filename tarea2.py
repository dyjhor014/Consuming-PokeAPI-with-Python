import os
import requests
os.system("clear")

#Funcion para listar las opciones del menú
def listar(seleccion_menu: str) -> None:
        url = f"https://pokeapi.co/api/v2/{seleccion_menu}/"
        response = requests.get(url)
        data = response.json()
        print(f"{'*'*50}")
        print(f"Lista solicitada")
        print(f"{'*'*50}\n")
        for i in range(0, len(data["results"])):
            item = data["results"][i]["name"]
            print(f"{seleccion_menu} ({i+1}): {item}")
        print("\n")

#Funcion para listar los pokemons segun la opcion elegida
def listar_pokemon(seleccion, seleccion_menu, opcion: str) -> None:
    """ while seleccion not in ("1","2","3","4","5","6","7","8","9"):
        seleccion = str(input("Debes ingresar el numero del habitat\n")) """
    url = f'https://pokeapi.co/api/v2/{seleccion_menu}/{seleccion}/'
    response = requests.get(url)
    data = response.json()
    print(f"{'*'*50}\n")
    print(f"Lista de pokemons con el {seleccion_menu}: {seleccion}\n")
    print(f"{'*'*50}\n")
    if opcion == "1":
        for i in range(0, len(data["pokemon_species"])):
            pokemon = data["pokemon_species"][i]["name"]
            print(f"Pokemon ({i}): {pokemon}")
    if opcion == "4":
        for i in range(0, len(data["pokemon_species"])):
            pokemon = data["pokemon_species"][i]["name"]
            print(f"Pokemon ({i}): {pokemon}")
    if opcion == "5":
        for i in range(0, len(data["pokemon"])):
            pokemon = data["pokemon"][i]["pokemon"]["name"]
            print(f"Pokemon ({i}): {pokemon}")
    #print(data["pokemon"][0]["pokemon"]["name"])

opcion = str(input("Ingresa una opción del Menu 1,2,3,4 o 5\n"))
while opcion not in ("1","2","3","4","5"):
    opcion = str(input("Debes ingresar una opción del 1 al 6\n"))
if opcion == "1":
    seleccion_menu = "generation"
    listar(seleccion_menu)
    seleccion = str(input(f"Ingresa el numero del {seleccion_menu}\n"))
    listar_pokemon(seleccion, seleccion_menu, opcion)
if opcion == "4":
    seleccion_menu = "pokemon-habitat"
    listar(seleccion_menu)
    seleccion = str(input(f"Ingresa el numero del {seleccion_menu}\n"))
    listar_pokemon(seleccion, seleccion_menu, opcion)
if opcion == "5":
    seleccion_menu = "type"
    listar(seleccion_menu)
    seleccion = str(input(f"Ingresa el numero del {seleccion_menu}\n"))
    listar_pokemon(seleccion, seleccion_menu,opcion)