from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_name(name="World"):
    return render_template('hello.html', name=name)