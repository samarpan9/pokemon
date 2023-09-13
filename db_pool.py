import asyncpg


async def create_db_pool():
    conn = await asyncpg.create_pool(
        host="localhost",
        port=5432,
        user="postgres",
        password="000",
        database="pokemon",
    )
    return conn