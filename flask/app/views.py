from app import app


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/some')
def some():
    return 'Some - Hello, World!'
