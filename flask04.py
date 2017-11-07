from flask import Flask, request
app = Flask('myapp')

@app.route('/')
def index():
    name = request.args.get('name')
    if name is None:
        name = 'world'
    return 'Hello, {}'.format(name)


if __name__ == '__main__':
    app.run()
