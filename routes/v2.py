from fastapi import FastAPI, Header
from starlette.status import HTTP_201_CREATED
from models.user import User


app_v2 = FastAPI(openapi_prefix='/v2')


@app_v2.post('/user', status_code=HTTP_201_CREATED)
async def post_user():
    return {'request body': 'it is version 2'}

