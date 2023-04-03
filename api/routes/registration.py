from fastapi import APIRouter, Request
from api.service import registration
from api.schema.registrations import RegistrationNew, RegistrationLegacy

router = APIRouter()

@router.get(path="/legacy")
async def get_registrations_legacy(request:Request):
    return await registration.get_all_registration_legacy(request.state.pool)

@router.get(path="/new")
async def get_registrations_new(request:Request):
    print("ok")
    return await registration.get_all_registration_new(request.state.pool)

@router.post(path="/new/fitler")
async def get_filtered_registration_new(request:Request, filter:RegistrationNew):
    return await registration.get_filtered_registration_new(request.pool, filter)

@router.post(path="/legacy/filter")
async def get_filtered_registration_legacy(request:Request, filter:RegistrationLegacy):
    return await registration.get_filtered_registration_legacy(request.pool, filter)