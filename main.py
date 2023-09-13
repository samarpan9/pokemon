from fastapi import FastAPI, Query

import db_helper

app = FastAPI()


@app.get("/api/v1/pokemons")
async def get_pokemons(
    name: str = Query(None),
    type: str = Query(None),
    limit: int = Query(None),
    page: int = Query(None),
):
    if name and type:
        ext_query = f""" WHERE name LIKE '%{name}%' and '{type}' LIKE \n
        ANY (poke_type)"""
    elif name:
        ext_query = f""" WHERE name LIKE '%{name}%'"""
    elif type:
        ext_query = f""" WHERE '{type}' LIKE ANY (poke_type)"""
    else:
        ext_query = ''

    page_query = ''
    if limit and page:
        start_index = (page - 1) * limit
        end_index = page * limit
        page_query = f""" LIMIT {end_index} OFFSET {start_index}"""

    ext_query += page_query
    data = await db_helper.get_pokemon_data(ext_query)
    return data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
