from api.database import sql_methods as sql

async def get_all_registration_legacy(pool):
    query = "SELECT * FROM registration_legacy"
    return await sql.get_multiple_rows(pool, query)

async def get_all_registration_new(pool):
    query = "SELECT * FROM registration_new"
    return await sql.get_multiple_rows(pool, query)

async def get_filtered_registration_new(pool,filter):
    query = "SELECT * FROM registration_new WHERE 1 == 1"
    if filter.term is not None:
        query += "AND term IN ("
        for i in filter.term:
            query += f"'{i}',"
        query += ")"
    if filter.subject is not None:
        query += "AND term IN ("
        for i in filter.subject:
            query += f"'{i}',"
        query += ")"
    if filter.section is not None:
        query += "AND term IN ("
        for i in filter.section:
            query += f"'{i}',"
        query += ")"
    if filter.campus is not None:
        query += "AND term IN ("
        for i in filter.campus:
            query += f"'{i}',"
        query += ")"
    if filter.credit is not None:
        query += "AND term IN ("
        for i in filter.credit:
            query += f"'{i}',"
        query += ")"
    if filter.title is not None:
        query += "AND term IN ("
        for i in filter.title:
            query += f"'{i}',"
        query += ")"
    if filter.days is not None:
        query += "AND term IN ("
        for i in filter.days:
            query += f"'{i}',"
        query += ")"
    if filter.time is not None:
        query += "AND term IN ("
        for i in filter.time:
            query += f"'{i}',"
        query += ")"
    if filter.instructor is not None:
        query += "AND term IN ("
        for i in filter.instructor:
            query += f"'{i}',"
        query += ")"
    if filter.attribute is not None:
        query += "AND term IN ("
        for i in filter.attribute:
            query += f"'{i}',"
        query += ")"
    query += ";"
    return await sql.get_multiple_rows(pool, query)
