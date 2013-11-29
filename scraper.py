from lxml import html
import requests
import re

URL = 'http://www.animetake.com/'
DL_PAGE_LINK_XPATH = '//div[@class="updateinfo" and not(a[.="Announcment"])]/h4/a'
TORRENT_LINK_XPATH = '//li[@class="tor"]/a'
URLNAME_RE = r'^http://www\.animetake\.com/([^/]+)'

def parse_url(url):
    r = requests.get(url)
    return html.fromstring(r.text)

def to_tables(items):
    return { item.urlname: item for item in items }

def get_items():
    document = parse_url(URL)
    link_elems = document.xpath(DL_PAGE_LINK_XPATH)
    links = Link.lister(link_elems)
    items = Item.lister(links)
    return items

class Lister:
    @classmethod
    def lister(cls, elems):
        return [cls(el) for el in elems]

class Link(Lister):
    def __init__(self, element):
        self.name = element.text
        self.href = element.get('href')

    def parse_urlname(self):
        result = re.match(URLNAME_RE, self.href)
        if result:
            return result.group(1)
        return ""

class Item(Lister):
    def __init__(self, link):
        self.name = link.name
        self.href = link.href
        self.urlname = link.parse_urlname()

    def parse_torrents(self):
        page = parse_url(self.href)
        torrent_elems = page.xpath(TORRENT_LINK_XPATH)
        return Link.lister(torrent_elems)

if __name__ == "__main__":
    items = get_items()
    for item in items:
        print item.name
        # print [tor.href for tor in item.torrents]