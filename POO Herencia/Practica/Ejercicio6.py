import requests
class RickAndMortyCharacter:
    def __init__(self, name, status, specie, gender):
        self.name = name
        self.status =  status
        self.specie =  specie
        self.gender = gender

    def saludar(self):
        print(f'Hola soy {self.name}, y mis tados son los siguientes: ',
        f'\nEstado : {self.status}'
        f'\n ')

url_api = 'https://rickandmortyapi.com/api/character/1,2,3,4,5'
response =  requests.get(url_api)

data = response.json()

