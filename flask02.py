from flask import Flask
app = Flask('myapp')

@app.route('/')
def index():
    return 'Hello world'


@app.route('/roman')
def hello_roman():
    return 'Hello, Roman'


if __name__ == '__main__':
    app.run()
