import requests
import json


def download_image(url,name):
    data = requests.get(url).content
    f = open("images/{}.png".format(name),'wb')
    f.write(data)
    f.close()

def get_poke_img(data):
    img = data['sprites']['other']['official-artwork']['front_default']
    return img

def get_pokename(data):
    forms = data['forms']
    for x in range(len(forms)):
        pokename = forms[x]['name']
    return pokename

def get_poke_abilities(data):
    abilities = data['abilities']
    poke_abilities = []
    for x in range(len(abilities)):
        poke_abilities.append(abilities[x]['ability']['name'])
    return poke_abilities

def get_poke_type(data):
    types = data['types']
    for x in range(len(types)):
        type = types[x]['type']['name']
    return type

def get_pokestats(data):
    stats = data['stats']
    poke_dict = {}
    for x in range(len(stats)):
        stat_name = stats[x]['stat']['name']
        stat_values =stats[x]['base_stat']
        poke_dict[stat_name]= stat_values  
    return poke_dict
       
            
                      
               


def poke_data(poke_name):
        response = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(poke_name))
       

        if response.status_code == 200:
            print("sucessfully fetched the data")
            data = response.json()
            return data
        else:
            print(f"Hello person, there's a {response.status_code} error with your request")