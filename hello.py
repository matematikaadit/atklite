from flask import Flask, render_template
from scraper import get_items

app = Flask(__name__)
app.debug = True

@app.route('/')
def index():
    items = get_items()
    return render_template('index.html', items=items)

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name="World"):
    return render_template('hello.html', name=name)

if __name__ == "__main__":
    app.run()