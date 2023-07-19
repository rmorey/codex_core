from flask import Flask, render_template

app = Flask(__name__)
app.codex_logger = print

@app.route('/')
def index():
    app.codex_logger('Hello, world!')
    return 'Hello, world!'

@app.route('/hello/<name>')
def hello(name):
    app.codex_logger(f'Saying hello to {name}')
    return render_template('hello.html', name=name)

@app.route('/overriden')
def overriden():
    app.codex_logger('Loading /overriden')
    return 'This page has not been overriden'

if __name__ == '__main__':
    app.run()