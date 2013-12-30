from flask import Blueprint, abort, render_template
from app.lib.HttpApplication import render_markdown

blueprint = Blueprint('pages', __name__)

@blueprint.route('/', defaults={'path': 'index'})
@blueprint.route('/<path:path>')
def page(path):
    try:
        return render_template('default.html', content = render_markdown(path.strip(' /') + '.md'), title = path)
    except IOError, e:
        abort(404)
