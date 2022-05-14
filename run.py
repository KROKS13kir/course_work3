from flask import Flask

import logger
from api.api_main import api_blueprint
from main import main_blueprint


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


logger.create_logger()

app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)

app.run()
