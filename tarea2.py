import os
import requests
os.system("clear")

#Funcion para la opcion 4
def listar_habitat(url: str) -> None:

        response_habitat = requests.get(url)
        data_habitat = response_habitat.json()
        for i in range(0, len(data_habitat["results"])):
            habitat = data_habitat["results"][i]["name"]
            print(f"Habitat ({i+1}): {habitat}")
#Funcion para listar los pokemons segun el habitat elegido
def listar_pokemon_habitat(seleccion_habitat: str) -> None:
    while seleccion_habitat not in ("1","2","3","4","5","6","7","8","9"):
        seleccion_habitat = str(input("Debes ingresar el numero del habitat\n"))
    url = f'https://pokeapi.co/api/v2/pokemon-habitat/{seleccion_habitat}/'
    response_habitat = requests.get(url)
    data_habitat = response_habitat.json()
    print(data_habitat["pokemon_species"][0]["name"])
    print(f"Lista de pokemons con el habitat{seleccion_habitat}")
    for i in range(0, len(data_habitat["pokemon_species"])):
        pokemon_specie = data_habitat["pokemon_species"][i]["name"]
        print(f"Pokemon ({i+1}): {pokemon_specie}")

opcion = str(input("Ingresa una opción del Menu 1,2,3,4 o 5\n"))
while opcion not in ("1","2","3","4","5"):
    opcion = str(input("Debes ingresar una opción del 1 al 6\n"))
if opcion == "4":
    url = 'https://pokeapi.co/api/v2/pokemon-habitat/'
    listar_habitat(url)
    seleccion_habitat = str(input("Ingresa el numero del habitat\n"))
    listar_pokemon_habitat(seleccion_habitat)