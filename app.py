from flask import Flask, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def home():
    return 'Welcome to home page.'

@app.route('/hello')
def hello_world():
    return 'Hello World.'

@app.route('/welcome')
def welcome():
    return 'Welcome to new page.'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Welcome %s.' %name

@app.route('/success/<name>')
def success(name):
    return 'Hi %s.' %name

@app.route('/login', methods=['POST' , 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))

    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))

if __name__ == "__main__":

    app.run(debug=True)
