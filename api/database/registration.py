from sql_methods import get_multiple_rows

async def get_registration(pool):
  query = "SELECT * FROM registration"
  return await get_multiple_rows(pool, query)