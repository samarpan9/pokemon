import db_pool


async def create_pokemon_table(connection):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS pokemon_list (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        image VARCHAR(255),
        poke_type VARCHAR(255)[]
    )
    """
    await connection.execute(create_table_query)


async def insert_pokemon(connection, name, weight, poke_type):
    insert_query = "INSERT INTO pokemon_list (name, weight,poke_type) VALUES ($1, $2, $3);"
    await connection.execute(insert_query, name, weight, poke_type)


async def get_pokemon_data(ext_query):
    pool = await db_pool.create_db_pool()

    async with pool.acquire() as connection:
        query = f"""SELECT * FROM pokemon_list{ext_query};"""
        result = await connection.fetch(query)
        return result
