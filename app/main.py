import os

import config
from initializer import create_app


app = create_app()


if __name__ == '__main__':
    app.run(host=config.SERVER_HOST, port=config.SERVER_PORT, dev=config.DEV, debug=config.DEBUG, workers=os.cpu_count())
