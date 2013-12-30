from app.bootstrap import create_app
import sys
import os

sys.dont_write_bytecode = True
os.chdir(os.path.dirname(__file__))

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
