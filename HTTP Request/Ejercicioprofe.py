import os
os.system("clear") # en windows usar "cls"
url_pokeapi = "https://pokeapi.co/api/v2/pokemon/"
import requests

def getPokemon(pokemon_name : str) -> None:
    # Haciendo el request (method: GET)
    response = requests.get(url_pokeapi + pokemon_name)
    # Transformando la respuesta de json a un diccionario:
    data = response.json()
    print(f"Nombre: {data['name']}")
    print(f"Peso: {data['weight']}")
    # Obteniendo lista de habilidades:
    lista_habilidades = [habilidad['ability']['name'] for habilidad in data['abilities']]
    # Obteniendo lista de estadisticas:
    dicc_estadisticas = {stat["stat"]["name"] : stat["base_stat"] for stat in data["stats"]}
    print(f"Habilidades: {lista_habilidades}")
    print(f"Estadisticas: {dicc_estadisticas}")
    print(f"Estadistica Ataque: {dicc_estadisticas['attack']}")


lista_pokemones = ["pikachu", "squirtle", "charmander"]

for pokemon in lista_pokemones:
    getPokemon(pokemon)
    print("-" * 20)
