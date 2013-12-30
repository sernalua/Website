import unittest
from app.bootstrap import create_app
from flask import Blueprint, url_for

class Test_run(unittest.TestCase):
    def test_run(self):
        app = create_app()
        bp = Blueprint('test', __name__)
        @bp.route('/')
        def home():
            return '/'

        application.register_blueprint(bp)
        self.assertIsNotNone(application.url_for('home'))

if __name__ == '__main__':
    unittest.main()
