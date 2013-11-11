from flask import Blueprint

blueprint = Blueprint('pages', __name__)

@blueprint.route('/', defaults={'path': ''})
@blueprint.route('/<path:path>')
def page(path):
	return path

@blueprint.route('/')
def index():
    return "Hello, World! It works. Now Mike tests to make sure his server instance works."


@blueprint.route('/about')
def about():
    return "About Us"
