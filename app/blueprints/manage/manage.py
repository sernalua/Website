from flask import Blueprint
from app.lib.authorize import authorize

blueprint = Blueprint('manage', __name__, url_prefix = '/manage')

@blueprint.route('/')
@authorize(['Cory'])
def index():
    return 'test login'

@blueprint.route('/test/<value>')
@authorize()
def test(value):
    return 'test variable: ' + value;