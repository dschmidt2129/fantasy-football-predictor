from flask import Flask

def init_app():
# creates the base localhost to start the app
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile('../config.py')

    from controllers import ScrapeController
    app.register_blueprint(ScrapeController.sc) # controller for scraping methods
    app.add_url_rule('/', endpoint='index')
    
    return app

app = init_app()