from flask import session, Flask, current_app
from Crypto.Hash import SHA256
import binascii
import os

class IUser(object):
    """The IUser interface enforces the username, password, and
    seed properties of the User as well as the currently not
    implemented validate method.
    """

    def __init__(self, username='', password='', seed=''):
        self.username = username
        self.password = password
        self.seed = seed

    def validate():
        """Will return True if all properties meet validation
        criteria or False if any properties do not.
        """
        return NotImplementedError()

class TestUser(IUser, object):
    """An implementation of the IUser interface that forces 
    username to be between 5 and 20 characters long
    """

    def __init__(self, username='', password='', seed=''):
        return super(TestUser, self).__init__(username, password, seed)

    def validate():
        """Password cannot be valiated on the server since it is 
        hashed on the client before it is sent over. We may want
        to send the password as clear text during registration to
        validate on the server or we can provide client-side 
        validation for the password; however, it would be easy to
        override the client-side validation to provide a password
        that does not meet criteria.
        """
        return 5 < len(username) and len(username) < 20

class IUserDbContext(object):
    """The IUserDbContext is the interface that should be implemented to
    provide the UserContext implementation with the ability to save and
    retrieve users from the database.
    """
    
    def get_user(self, username):
        raise NotImplementedError()

    def set_user(self, User):
        raise NotImplementedError()

class TestUserDbContext(IUserDbContext, object):
    """The TestUserDbContext implements the IUserDbContext interface
    using local memory (a dictionary) as its storage mechanism.
    This UserDbContext will not preserve new users between runs!
    """

    def __init__(self, *args, **kwargs):
        self.users = {}
        rand = os.urandom(16)
        testpw = SHA256.new('test' + binascii.hexlify(rand)).digest()
        self.set_user(IUser('Cory', testpw, rand))
        return super(IUserDbContext, self).__init__(*args, **kwargs)

    def get_user(self, username):
        if username.lower() in self.users:
            return self.users[username.lower()]
        return IUser()

    def set_user(self, User):
        if isinstance(User, IUser):
            self.users[User.username.lower()] = User

class UserContext(object):
    """The UserContext class provides the primary interface for 
    authentication and user profile.

    The classmethods that provide the primary interface for
    logging in, logging out, registering, and retrieving users
    rely on the current_app global. The current_app global is 
    set by Flask and may point to another running application.
    (although it shouldn't)
    """

    def __init__(self, app=Flask(__name__), IUserDbContext=TestUserDbContext()):
        """
        """
        self.db = IUserDbContext
        app.user_context = self
        app.add_url_rule('/api/seed/', 'api.seed', self.seed, defaults={'username': None})
        app.add_url_rule('/api/seed/<username>/', 'api.userseed', self.seed)

    def seed(self, username=None):
        """The seed method is meant to be called from the browser
        via AJAX. It returns a generated seed value when no user
        argument is passed. It returns the user seed stored in the
        database if a username is passed.

        Due to the application wide-nature of the generated seed,
        it is best to consume the seed immediately after retrieving
        it; otherwise, there is a chance that the seed will no
        longer be valid by the time you use it.
        """
        if username is not None:
            return binascii.hexlify(self.db.get_user(username).seed)
        else:
            self.id = os.urandom(60)
            return binascii.hexlify(self.id)

    def _login(self, username, password):
        """The _login method of the UserContext logs the user in if 
        the user is in the database and the hashed passwords match.

        This method has several necessary side effects to ensure
        that the proper information is set:
            upon successful login the 'authenticated' session 
            variable is set to True and the 'username' is set
            to the value retrieved from the database.

        The function either returns the user object (descendant of
        IUser) or None if the user was not found or a username was
        not provided or the password was incorrect.
        """
        if len(username) > 0:
            user = self.db.get_user(username)
            pw = SHA256.new(binascii.hexlify(user.password) + binascii.hexlify(self.id))
            if pw.hexdigest() == password:
                session['authenticated'] = True
                session['username'] = user.username
                return user
        return None

    def _register(self, username, password):
        """The register method creates a User for the given username
        and password (hashed). It saves the current id as the seed for
        the user. This assumes that the application requests a seed,
        uses the seed to hash the password, and calls this method
        to save the user.

        This method then logs the newly created user in and returns
        the user object representing the new user.
        """
        user = IUser(username.title(), binascii.unhexlify(password), self.id)
        self.db.set_user(user)
        pw = SHA256.new(password + binascii.hexlify(self.id))
        user = self._login(username, pw.hexdigest())
        return user
    
    @classmethod
    def login(cls, username, password):
        """The login method is a classmethod to avoid naming 
        confusion. It is fairly easy to class UserContext.login()
        rather than dealing with the possible naming conflicts
        of importing a login function directly.
        """
        return current_app.user_context._login(username, password)

    @classmethod
    def register(cls, username, password):
        """see UserContext.login"""
        return current_app.user_context._register(username, password)

    @classmethod
    def logout(cls):
        """see UserContext.login"""
        session['authenticated'] = False

    @classmethod
    def get_user(cls):
        """The get_user method retrieves the currently logged in
        user. It relies on the Flask implementation of the session
        variable to control context.

        If the user is not logged in it returns None
        """
        if 'authenticated' in session and 'username' in session:
            if session['authenticated']:
                return current_app.user_context.db.get_user(session['username'])
        return None
