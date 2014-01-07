from app.lib.http_application import HTTPApplication
from app.lib.user_context import UserContext
import os

def create_app():
    frontend = os.path.join(os.getcwd(), 'app', 'frontend')
    app = HTTPApplication(__name__, template_folder = os.path.join(frontend, 'templates'), static_folder = os.path.join(frontend, 'static'), markdown_folder = os.path.join(frontend, 'content'))
    app.config.from_object('app.settings')
    app.define_blueprints('app.blueprints')
    userContext = UserContext(app)
    return app