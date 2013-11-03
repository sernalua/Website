from app import app

@app.route('/')
def index():
    return "Hello, World! It works"

@app.route('/about')
def about():
    return "About Us"
