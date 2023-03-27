from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/")
async def get_single_table(request:Request):
    pass

    