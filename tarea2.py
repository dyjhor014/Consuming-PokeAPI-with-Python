import os
os.system("clear")

url_pokeapi = "https://pokeapi.co/api/v2/generation/"

import requests


print("Bienvenido al programa para listar pokemons")
print("*"*45)




def list_generation():
    g = str(input("Ingrese el número de generación: "))
    #Haciendo el request (method: GET)
    response = requests.get(url_pokeapi + g )
    #Transformando respuesta de Json a Dict
    data_g = response.json()
    #Obteniendo pokemones de generacion ingresada:

    print(f"Los pokemones de la generación {g} son: {len(data_g['pokemon_species'])}")
    # print(f"Nombre:)

   
    
list_generation()