import httpx

import db_helper


async def fetch_pokemon_data(db_pool):
    # use the url witht the limit to fetch only that number of pokemons.\n
    # use the other one to fetch all the pokemons from the api.
    next_url = 'https://pokeapi.co/api/v2/pokemon?limit=10&offset=1'
    # next_url = 'https://pokeapi.co/api/v2/pokemon'

    async with httpx.AsyncClient() as client:
        # while next_url:
        response = await client.get(next_url)

        if response.status_code != 200:
            print(f"Request failed with status code: {response.status_code}")
            # break

        data = response.json()
        results = data.get('results', [])

        for result in results:
            pokemon_name = result['name']
            pokemon_url = result['url']

            detail_response = await client.get(pokemon_url)

            if detail_response.status_code != 200:
                print(f"Failed to fetch data for {pokemon_name}")

            pokemon_details = detail_response.json()

            image = pokemon_details['sprites']['other']['official-artwork']['front_default']
            poke_types = pokemon_details['types']
            type_list = []
            for poke_details in poke_types:
                poke_type = poke_details['type']['name']
                type_list.append(poke_type)
            print(f"""Pokemon data: {pokemon_name} collected""")
            await db_helper.insert_pokemon(
                db_pool, pokemon_name, image, type_list)

        # next_url = data.get('next')
