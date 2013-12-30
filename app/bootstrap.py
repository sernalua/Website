from app.lib.HttpApplication import HttpApplication
import os

def create_app():
    frontend = os.path.join(os.getcwd(), 'app', 'frontend')
    app = HttpApplication(__name__, template_folder = os.path.join(frontend, 'templates'), static_folder = os.path.join(frontend, 'static'), markdown_folder = os.path.join(frontend, 'content'))
    app.config.from_object('app.settings')
    app.define_blueprints('app.blueprints')
    return app