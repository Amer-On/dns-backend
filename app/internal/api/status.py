from sanic import Blueprint, Request
from sanic.response import JSONResponse


STATUS_BP = Blueprint('Status')


@STATUS_BP.get('status')
async def status_handler(request: Request) -> JSONResponse:
    return JSONResponse(status=200, body={'status': 'ok'})
