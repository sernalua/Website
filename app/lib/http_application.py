from flask import Flask, Blueprint, current_app
from flask.ext.misaka import Misaka, markdown
import importlib
import os

class HTTPApplication(Flask):

    def __init__(self, import_name, static_path=None, static_url_path=None,
                 static_folder='static', template_folder='templates',
                 instance_path=None, instance_relative_config=False, 
                 markdown_folder='content'):
        result = (super(HTTPApplication, self)
                  .__init__(import_name, static_path, static_url_path, 
                           static_folder, template_folder, instance_path,
                           instance_relative_config))
        self.markdown_folder = os.path.join(os.getcwd(), markdown_folder)
        Misaka(result)
        return result

    def define_blueprints(self, path):
        directory = importlib.import_module(path)
        if hasattr(directory, '__all__'):
            for item in directory.__all__:
                self.define_blueprints('%s.%s' % (path, item))
        else:
            for item in dir(directory):
                attr = getattr(directory, item)
                if isinstance(attr, Blueprint):
                    self.register_blueprint(attr)

def render_markdown(name):
    f = open(os.path.join(current_app.markdown_folder, name))
    return markdown(f.read())
