from flask import Flask, render_template, abort, url_for
from scraper import get_items, items_to_tables
from datetime import date

app = Flask(__name__)

@app.route('/')
def index():
    items = get_items()
    t = date.today()
    today = "{0:%A} {0:%B} {1}, {0:%Y}".format(t,ordinal(t.day))
    # %A: Weekday full: Saturday
    # %B: Month full: November
    # %d: day: 30
    # %Y: full year: 2013
    return render_template('index.html', items=items, today=today)

def ordinal(day):
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = 'th'
    else:
        suffix = ['st','nd','rd'][day % 10 - 1]
    return str(day)+suffix

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