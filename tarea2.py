import os
os.system("clear")

url_pokeapi = "https://pokeapi.co/api/v2/generation/"

import requests

print("Bienvenido al programa para listar pokemons")
print("*"*45)
print("Opción 1:Listar pokemons por generación.")
print("Opción 2:Listar pokemons por forma.")
print("Opción 3:Listar pokemons por habilidad.")
print("Opción 4:Listar pokemons por habitat")
print("Opción 5:Listar pokemons por tipo.")

opcion = int(input("\nIngrese el número de opción: "))
if opcion == 1:
     
    def list_generation():
        g = str(input("\nIngrese el número de generación: "))
        #Haciendo el request (method: GET)
        response = requests.get(url_pokeapi + g )
        #Transformando respuesta de Json a Dict
        data_g = response.json()
        #Obteniendo pokemones de generacion ingresada:

        print(f"\nLos pokemones de la generación {g} son en total: {len(data_g['pokemon_species'])}")
           
    list_generation()