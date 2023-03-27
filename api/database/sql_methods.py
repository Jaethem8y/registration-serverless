import aiomysql

# query for one row
async def get_single_row(pool,query:str):
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(query)
            return await cur.fetchone()

# query for multiple rows
async def get_multiple_rows(pool,query:str):
    async with pool.acquire() as conn:
        async with conn.cursor(aiomysql.DictCursor) as cur:
            await cur.execute(query)
            return await cur.fetchall()