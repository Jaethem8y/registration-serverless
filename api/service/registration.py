from api.database import registration

# query table by table_name
async def get_all_registration_legacy(pool):
    return await registration.get_all_registration_legacy(pool)

async def get_all_registration_new(pool):
    return await registration.get_all_registration_new(pool)

async def get_filtered_registration_new(pool,filter):
    return await registration.get_filtered_registration_new(pool,filter)

async def get_filtered_registration_legacy(pool,filter):
    return await registration.get_filtered_registration_legacy(pool,filter)




