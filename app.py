from flask import Flask

app = Flask(__name__)


@app.route('/hello')
def hello_world():

    return 'Hello World.'

@app.route('/welcome')
def welcome():

    return 'Welcome to new page.'

@app.route('/hello/<name>')
def hello_name(name):

    return 'Welcome %s.' %name

if __name__ == "__main__":

    app.run(debug=True)
