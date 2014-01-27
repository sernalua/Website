from app.bootstrap import create_app
import sys
import os

sys.dont_write_bytecode = True
os.chdir(os.path.split(os.path.realpath(__file__))[0])

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
