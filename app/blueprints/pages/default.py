from flask import Blueprint

blueprint = Blueprint('content', __name__)


@blueprint.route('/')
def index():
    return "Hello, World! It works"


@blueprint.route('/about')
def about():
    return "About Us"
