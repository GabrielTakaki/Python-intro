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
with open("balneabilidade-6a68bb4061019473c86a2a1b32a03a7d.csv") as file:
    beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
    header, *data = beach_status_reader  # header, *data is used to separate the header from the remaining data

print(data)

a, b = "cd"
print(a)  # output: c
print(b)  # output: d
head, *tail = [1, 2, 3]
print(head)  # output: 1
print(tail)  # output: [2, 3]


# Read the data
with open("balneabilidade.csv") as file:
    beach_status_reader = csv.reader(file, delimiter=",", quotechar='"')
    header, *data = beach_status_reader

# group campaigns and its respective balneabilidades
bathing_by_campaign = {}
for row in data:
    campaign = row[6]
    bathing = row[2]
    if campaign not in bathing_by_campaign:
        bathing_by_campaign[campaign] = {
            "Própria": 0,
            "Imprópria": 0,
            "Muito Boa": 0,
            "Indisponível": 0,
            "Satisfatória": 0,
        }
    bathing_by_campaign[campaign][bathing] += 1

# Write a report in csv
# Open a file for writing
with open("report_por_campanha.csv", "w") as file:
    writer = csv.writer(file)

    # Write the header
    headers = [
        "Campanha",
        "Própria",
        "Imprópria",
        "Muito Boa",
        "Indisponível",
        "Satisfatória",
    ]
    writer.writerow(headers)

    # Write the lines of datas
    for campaign, bathing in bathing_by_campaign.items():
        # desempacota os valores de balneabilidade para formar uma linha
        # equivalente a
        # row = [campaign]
        # for value in bathing.values():
        #     row.append(value)
        row = [campaign, *bathing.values()]
        writer.writerow(row)
        