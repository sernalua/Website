from flask import Blueprint
from flask.ext.misaka import markdown

blueprint = Blueprint('pages', __name__)

@blueprint.route('/', defaults={'path': ''})
@blueprint.route('/<path:path>')
def page(path):
	#f = open('../../frontend/content/' + path + '.md')
	#return markdown(f.read())
	return os.getcwd()

@blueprint.route('/')
def index():
    return "Hello, World! It works. Now Mike tests to make sure his server instance works."


@blueprint.route('/about')
def about():
    return "About Us"
