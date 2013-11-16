from app.bootstrap import create_app

import sys

sys.dont_write_bytecode = True


app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
