from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from api.routes.registration import router
from api.db import host, port, user, password, database

import aiomysql

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*']
    )
]

app = FastAPI(
    title="Registration",
    description="registration app for CS191",
    version="0.0.1",
    middleware=middleware,
    root_path="/dev",
    docs_url='/docs',
    # openapi_url='/dev/openapi.json', 
    redoc_url=None
)

@app.on_event("startup")
async def _startup():
    app.state.pool = await aiomysql.create_pool(host=host, port=port, user=user, password=password, db=database)
    print("startup done")

@app.on_event("shutdown")
async def _shutdown():
    await app.state.pool.wait_closed()

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.pool = app.state.pool
    response = await call_next(request)
    return response

# Example route
@app.get("/")
async def root():
    return "Danner Danner Danner Danner"
app.include_router(router)

handler = Mangum(app)
