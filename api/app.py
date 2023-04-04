from fastapi import FastAPI, Request
from fastapi.middleware import Middleware
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from api.routes.registration import router
import aiomysql

# environment variables for db connection
import os
from dotenv import load_dotenv
load_dotenv()
HOST = os.environ['HOST']
PORT = int( os.environ['PORT'] )
USER = os.environ['USER']
PASSWORD = os.environ['PASSWORD']
DATABASE = os.environ['DATABASE']

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
    # openapi_url='/dev/openapi.json', 
    root_path="/dev",
    redoc_url=None
)

async def get_db_pool():
    return await aiomysql.create_pool(host=HOST, port=PORT, user=USER, password=PASSWORD, db=DATABASE)

@app.on_event("startup")
async def _startup():
    print('app is starting up...')
    app.state.pool = await get_db_pool()
    print('db connection made.')
    app.include_router(router)

@app.on_event("shutdown")
async def _shutdown():
    print('app is shutting down...')
    app.state.pool.close()
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

handler = Mangum(app, lifespan="on")