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
        query += "AND subject IN ("
        for i in filter.subject:
            query += f"'{i}',"
        query += ")"
    if filter.section is not None:
        query += "AND section IN ("
        for i in filter.section:
            query += f"'{i}',"
        query += ")"
    if filter.campus is not None:
        query += "AND campus IN ("
        for i in filter.campus:
            query += f"'{i}',"
        query += ")"
    if filter.credit is not None:
        query += "AND credit IN ("
        for i in filter.credit:
            query += f"'{i}',"
        query += ")"
    if filter.title is not None:
        query += "AND title IN ("
        for i in filter.title:
            query += f"'{i}',"
        query += ")"
    if filter.days is not None:
        query += "AND days IN ("
        for i in filter.days:
            query += f"'{i}',"
        query += ")"
    if filter.instructor is not None:
        query += "AND instructor IN ("
        for i in filter.instructor:
            query += f"'{i}',"
        query += ")"
    if filter.attribute is not None:
        query += "AND attribute IN ("
        for i in filter.attribute:
            query += f"'{i}',"
        query += ")"
    if filter.start_time is not None:
        query += "AND start_time >= " + filter.start_time 
    if filter.end_time is not None:
        query += "AND end_time <= " + filter.end_time;
    query += ";"
    print(query)
    return await sql.get_multiple_rows(pool, query)

async def get_filtered_registration_legacy(pool,filter):
    query = "SELECT * FROM registration_new WHERE 1 == 1"

    if filter.term is not None:
        query += "AND term IN ("
        for i in filter.term:
            query += f"'{i}',"
        query += ")"
    if filter.subject is not None:
        query += "AND subject IN ("
        for i in filter.subject:
            query += f"'{i}',"
        query += ")"
    if filter.title is not None:
        query += "AND title IN ("
        for i in filter.title:
            query += f"'{i}',"
        query += ")"
    if filter.campus is not None:
        query += "AND campus IN ("
        for i in filter.campus:
            query += f"'{i}',"
        query += ")"
    if filter.type is not None:
        query += "AND type IN ("
        for i in filter.type:
            query += f"'{i}',"
        query += ")"
    if filter.last_name is not None:
        query += "AND last_name IN ("
        for i in filter.last_name:
            query += f"'{i}',"
        query += ")"
    if filter.first_name is not None:
        query += "AND first_name IN ("
        for i in filter.first_name:
            query += f"'{i}',"
        query += ")"
    
    query += ";"
    print(query)
    return await sql.get_multiple_rows(pool, query)