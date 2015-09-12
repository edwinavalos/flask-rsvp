from flask import Flask
import logging

def create_app(config_filename=None):
    app = Flask(__name__, instance_relative_config=True)
    if app.config.from_pyfile("settings.conf", silent=True):
        print "Settings loaded from local instance"
    if app.config.from_envvar("RSVP_CONF", silent=True):
        print "Settings loaded from ENVVAR"
    if app.config["DEBUG"]:
        app.debug = True

    log_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
    root_logger = logging.getLogger("werkzeug")
    if app.config["DEBUG"]:
        root_logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("{}/{}".format(app.config["LOGDIR"], "rsvp.log"))
    file_handler.setFormatter(log_formatter)
    root_logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    root_logger.addHandler(console_handler)

    from extensions import db
    import models
    db.init_app(app)
    models.create_all(app)

    from views import views_bp
    app.register_blueprint(views_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", debug=True)
