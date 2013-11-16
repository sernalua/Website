from flask import Flask, Blueprint, abort
from flask.ext.misaka import markdown
from . import blueprints
import importlib
import os

content = Blueprint('content', __name__)


@content.route('/', defaults={'path': 'index'})
@content.route('/<path:path>')
def page(path):
    try:
        f = open('app/frontend/content/' + path + '.md')
        return markdown(f.read())
    except IOError:
        abort(404)


def create_app():

    app = Flask(__name__)
    app.config.from_object('app.settings')

    # Register content blueprint
    app.register_blueprint(content)

    # Register all blueprint packages
    for package_name in blueprints.__all__:
        package = importlib.import_module('app.blueprints.%s' % (package_name))
        for module_name in package.__all__:
            module = importlib.import_module(
                'app.blueprints.%s.%s' % (package_name, module_name))
            for item in dir(module):
                item = getattr(module, item)
                if isinstance(item, Blueprint):
                    app.register_blueprint(
                        item, url_prefix='/%s' % (package_name))

    return app
