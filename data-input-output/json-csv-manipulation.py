# CSV
import csv
# JSON
import json

with open('pokemons.json') as pokemons_file:
    pokemon_list = json.load(pokemons_file)['results']
    for pokemon in pokemon_list:
        print(pokemon['name'])


# Reading all the Pokémon
with open("pokemons.json") as file:
    pokemons = json.load(file)["results"]

# Separate only the grass type
grass_type_pokemons = [
    pokemon for pokemon in pokemons if "Grass" in pokemon["type"]
]

# Open file to write only the grass type Pokémon
with open("grass_pokemons.json", "w") as file:
    json_to_write = json.dumps(
        grass_type_pokemons
    )  # Python conversion to json format (str)
    file.write(json_to_write)


# CSV
