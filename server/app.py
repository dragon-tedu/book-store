import os

from server.config import app_config
from server.extensions import db, jwt,redis
from flask import Flask

def create_app(env_name):
    app = Flask(__name__)
    print(app_config[env_name])
    app.config.from_object(app_config[env_name])
    db.init_app(app)
    jwt.init_app(app)
    redis.init_app(app,config_prefix='CACHE' )

    app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024
    service_name = app.config["SERVICE_NAME"]
    base_prefix = "/" + service_name

    from server.routers.UserRouter import userRouter
    app.register_blueprint(userRouter, url_prefix=base_prefix+'/users')

    from server.routers.BookRooter import bookRouter
    app.register_blueprint(bookRouter, url_prefix=base_prefix+'/books')
    # app.register_error_handler(Exception, HandleError.handle)
    return app
