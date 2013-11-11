from flask import Blueprint
from flask.ext.misaka import markdown

blueprint = Blueprint('pages', __name__)

@blueprint.route('/', defaults={'path': ''})
@blueprint.route('/<path:path>')
def page(path):
	print '../../frontend/content/' + path + '.md'
	f = open('../../frontend/content/' + path + '.md')
	return markdown(f.read())

@blueprint.route('/')
def index():
    return "Hello, World! It works. Now Mike tests to make sure his server instance works."


@blueprint.route('/about')
def about():
    return "About Us"
