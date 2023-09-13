import asyncio

import api_handler
import db_helper
import db_pool


async def main():
    database_pool = await db_pool.create_db_pool()

    await db_helper.create_pokemon_table(database_pool)

    await api_handler.fetch_pokemon_data(database_pool)

    await database_pool.close()

if __name__ == "__main__":
    asyncio.run(main())
