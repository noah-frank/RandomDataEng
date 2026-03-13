import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        # print("Data retrieved!")
        pokemon_data = response.json() # Dict
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

    # print(response) # Returns something like <Response [200]>

# pokemon_name = "pikachu"
pokemon_name = input("Enter a Pokemon name: ").lower()
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"ID: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")