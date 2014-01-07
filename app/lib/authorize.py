from app.lib.user_context import UserContext
from flask import redirect, url_for

def authorize(Users=[], Roles=[]):
    """The authorize decorator provides a simple way to 
    ensure that users are authorized to access pages in
    a Flask/Blueprint app.

    This will ensure that the user is logged in before 
    rendering the page. If the user is not logged in
    it will redirect to the login page.
    Example:
    @app.route('/')
    @authorize()
    def index():
        return 'test'

    This will ensure that the user is in the list of 
    Users able to access the page (passes:
    @app.route('/<var>')
    @authorize(['User1', 'User2'])
    def index(var):
        return 'test' + var
    """
    def decorator(fn):
        def tmp(*args, **kwargs):
            user = UserContext.get_user()
            if user is not None and (len(Users) == 0 or (user is not None and user.username in Users)):
                return fn(*args, **kwargs)
            else:
                return redirect(url_for('account.login'))
        tmp.__name__ = fn.__name__
        return tmp
    return decorator