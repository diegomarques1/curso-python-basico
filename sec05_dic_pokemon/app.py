pokemons = {
    "id": ["0025", "0004"],
    "nome": ["Pikachu", "Charmander"],
    "atributo": ["Elétrico", "Fogo"]
}

pokemons["fraqueza"] = ["Terrestre", "Água"]

print(pokemons)

del pokemons["id"]
del pokemons["fraqueza"]

print(pokemons)