from sanic import Sanic

import config
from config.logging import LOGGING
from internal.api import API_BP


def add_blueprints(app: Sanic):
    app.blueprint(API_BP, url_prefix=config.APP_URL_PREFIX)


def add_exception_handlers(app: Sanic):
    pass


def configure_openapi(app: Sanic):
    app.config.OAS_UI_REDOC = False
    app.config.OAS_UI_DEFAULT = 'swagger'


def create_app() -> Sanic:
    app = Sanic('DnsShopBackend', log_config=LOGGING)
    configure_openapi(app)
    add_blueprints(app)
    add_exception_handlers(app)
    return app
