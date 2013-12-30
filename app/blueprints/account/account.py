from flask import Blueprint, render_template, session, redirect
from app.lib.HttpApplication import render_markdown
import os

blueprint = Blueprint('account', __name__, url_prefix = '/account', template_folder = os.path.join(os.getcwd(), 'app', 'frontend', 'templates', 'account'))

@blueprint.route('/')
def index():
    return render_template('index.html', content = render_markdown('test.md'))

@blueprint.route('/login/')
def login():
    return render_template('index.html', content = render_markdown('account/login.md'))

@blueprint.route('/register/')
def register():
    return render_template('index.html', content = render_markdown('account/register.md'))

@blueprint.route('/logout/')
def logout():
    session.clear()
    return redirect('/')
