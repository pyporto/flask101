from flask import Flask, request, render_template
app = Flask('myapp')


@app.route('/')
def index():
    name = request.args.get('name')
    if name is None:
        name = 'world'
    text = 'Hello, {}'.format(name)
    return render_template('splash.html', text=text)


if __name__ == '__main__':
    app.run()
