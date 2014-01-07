from flask import Blueprint, redirect, request, session, render_template
from app.lib.http_application import render_markdown
from app.lib.user_context import UserContext
from app.lib.authorize import authorize
import os

blueprint = Blueprint('account', __name__, url_prefix = '/account',
                      template_folder = os.path.join(os.getcwd(),
                                                     'app', 'frontend', 
                                                     'templates', 'account'))

@blueprint.route('/')
def index():
    return render_template('index.html', content = render_markdown('test.md'))

@blueprint.route('/login/', methods=['POST', 'GET'])
def login():
    error = ''
    if request.method == 'POST':
        user = UserContext.login(request.form['username'], request.form['password'])
        if user is not None:
            return redirect('/')
        else:
            error = 'Invalid username or password'
    return render_template('login.html',
                            content = render_markdown('account/login.md'),
                            error = error,
                            path = 'account/login')

@blueprint.route('/register/', methods=['POST', 'GET'])
def register():
    error = ''
    if request.method == 'POST':
        pw = request.form['password']
        if pw == request.form['password_confirmation']:
            user = UserContext.register(request.form['username'], pw)
            session['username'] = user.username
            return redirect('/')
        else:
            error = 'Passwords do not match.'
    return render_template('login.html',
                            content = render_markdown('account/register.md'),
                            path = 'account/register')

@blueprint.route('/logout/')
@authorize()
def logout():
    UserContext.logout()
    return redirect('/')
