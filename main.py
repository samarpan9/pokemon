from fastapi import FastAPI, Query
from pydantic import BaseModel

import db_helper

app = FastAPI()

class Pokemon(BaseModel):
    name: str
    image: str
    poke_type: list[str]


@app.get("/api/v1/pokemons", response_model=list[Pokemon])
async def get_pokemons(
    name: str = Query(None),
    type: str = Query(None),
):
    if name and type:
        ext_query = f""" WHERE name LIKE '%{name}%' and '{type}' LIKE ANY (poke_type)"""
    elif name:
        ext_query = f""" WHERE name LIKE '%{name}%'"""
    elif type:
        ext_query = f""" WHERE '{type}' LIKE ANY (poke_type)"""
    else:
        ext_query = ''

    data = await db_helper.get_pokemon_data(ext_query)
    return data


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
