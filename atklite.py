from flask import Flask, render_template, abort, url_for
from scraper import get_items, items_to_tables
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    items = get_items()
    today = date.today().strftime("%A %B %d, %y")
    # %A: Weekday full: Saturday
    # %B: Month full: November
    # %d: day
    # %y: year
    return render_template('index.html', items=items, today=today)

@app.route('/item/<urlname>')
def item(urlname=None):
    if urlname is None:
        abort(401)
    items = get_items()
    tables = items_to_tables(items)
    if urlname not in tables:
        abort(404)
    item = tables[urlname]
    torrents = item.parse_torrents()
    return render_template('item.html', item=item, torrents=torrents)

if __name__ == "__main__":
    app.run(debug=True)