import os 
import requests
os.system('cls') #Limpoia la pantalla
#Haciendo el request (Metodo: GET)
url_pokeapi= " https://pokeapi.co/api/v2/pokemon/"
def getPokemon(pokemon_name):
    info= requests.get(url_pokeapi)
    data = info.json()
    print(f"Nombre : {data['name']}")
    print(f"Nombre : {data['weight']}")
    #Obteniendo lista de habilidades
    lista_habilidades = [habilidad['ability']['name'] for habilidad  in data ['abilities']]
    #Obteniendo Stats
    dicc_stats ={stat["stat"]["name"] : stat["base_stat"] for stat in data["stats"]}
    # for stat in data["stats"]:
    #     dicc_stats[stat["stat"]["name"]]= stat["base_stat"]  

    print(f"Habilidades: {lista_habilidades}")

getPokemon("pikachu")
print('-' * 20)



