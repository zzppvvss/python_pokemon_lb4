import random
import requests
fun_fact_url = ""
def give_new_pokemon():
    idd = random.randrange(1, 400)
    api_pokemon = f"https://pokeapi.co/api/v2/pokemon/{idd}/"
    pokemon_response = requests.get(api_pokemon)
    global fun_fact_url
    fun_fact_url = f"https://pokeapi.co/api/v2/pokemon-species/{idd}/"
    if pokemon_response.status_code == 200:
        return pokemon_response.json()
    else:
        return "error #1 - can't find pokemon at all"
    return idd

def sprite_url(pokemon):
    pokemon_sprite = pokemon['sprites']
    pokemon_sprite_url = pokemon_sprite['front_default']
    return pokemon_sprite_url

def description():
    return fun_fact_url


