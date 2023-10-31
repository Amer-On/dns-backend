from sanic import Blueprint

from .status import STATUS_BP
from .v1 import V1_BP


API_BP = Blueprint.group(STATUS_BP, V1_BP, url_prefix='api')
