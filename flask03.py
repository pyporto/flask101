from flask import Flask
app = Flask('myapp')

@app.route('/')
def index():
    return 'Hello world'


@app.route('/<name>')
def hello_name(name):
    return 'Hello, {}'.format(name)


if __name__ == '__main__':
    app.run()
