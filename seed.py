import asyncio

import api_handler
import db_helper

async def main():
    db_pool = await db_helper.create_db_pool()
    
    await db_helper.create_pokemon_table(db_pool)
    
    await api_handler.fetch_pokemon_data(db_pool)
    
    await db_pool.close()

if __name__ == "__main__":
    asyncio.run(main())
