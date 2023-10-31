from sanic import Blueprint, HTTPResponse, Request


STATUS_BP = Blueprint('V1Status')


@STATUS_BP.get('status')
async def status(request: Request) -> HTTPResponse:
    return HTTPResponse(status=200)
