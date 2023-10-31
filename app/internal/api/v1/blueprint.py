from sanic import Blueprint

from .status import STATUS_BP


V1_BP = Blueprint.group(STATUS_BP, url_prefix='v1')
