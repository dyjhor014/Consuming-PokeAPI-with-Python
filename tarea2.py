import os
import requests
os.system("clear")

def run():
    listar(seleccion_menu)
    seleccion = str(input(f"Ingresa el numero del {seleccion_menu}\n"))
    listar_pokemon(seleccion, seleccion_menu, opcion)

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
    if opcion == "1" or opcion == "2" or opcion == "4":
        for i in range(0, len(data["pokemon_species"])):
            pokemon = data["pokemon_species"][i]["name"]
            url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
            response_pokemon = requests.get(url_pokemon)
            data_pokemon = response_pokemon.json()
            imagen = data_pokemon['sprites']['other']['home']['front_default']
            list_ability = [ability['ability']['name'] for ability in data_pokemon['abilities']]
            print(f"{'*'*50}\nPokemon: {pokemon}\nHabilidades: {list_ability}\nImagen: {imagen}")
    if opcion == "3" or opcion == "5":
        for i in range(0, len(data["pokemon"])):
            pokemon = data["pokemon"][i]["pokemon"]["name"]
            url_pokemon = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
            response_pokemon = requests.get(url_pokemon)
            data_pokemon = response_pokemon.json()
            imagen = data_pokemon['sprites']['other']['home']['front_default']
            list_ability = [ability['ability']['name'] for ability in data_pokemon['abilities']]
            print(f"{'*'*50}\nPokemon: {pokemon}\nHabilidades: {list_ability}\nImagen: {imagen}")
#Menu interactivo

print("Opción 1: Listar pokemons por generación. Se ingresa alguna generación (1, 2, 3, ..) y se listan todos los pokemon respectivos.")
print("Opción 2: Listar pokemons por forma. Se ingresa alguna forma (deben sugerir valores) y se listan todos los pokemons respectivos.")
print("Opción 3: Listar pokemons por habilidad. Se deben sugerir opciones a ingresar para interactuar.")
print("Opción 4: Listar pokemons por habitat. Se deben sugerir opciones a ingresar para interactuar.")
print("Opción 5: Listar pokemons por tipo. Se deben sugerir opciones a ingresar para interactuar.\n\n")


opcion = str(input("Ingresa una opción del Menu 1,2,3,4 o 5\n"))
while opcion not in ("1","2","3","4","5"):
    opcion = str(input("Debes ingresar una opción del 1 al 6\n"))
if opcion == "1":
    seleccion_menu = "generation"
    run()
if opcion =="2":
    seleccion_menu = "pokemon-shape"
    run()
if opcion == "3":
    seleccion_menu = "ability"
    run()
if opcion == "4":
    seleccion_menu = "pokemon-habitat"
    run()
if opcion == "5":
    seleccion_menu = "type"
    run()
