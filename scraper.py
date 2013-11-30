from lxml import html
import requests
import re

class List:
    @classmethod
    def list(cls, elems):
        return [cls(el) for el in elems]

class Box(List):
    DATE_XPATH = './span/text()[2]'
    LINK_XPATH = './h4/a'

    def __init__(self, box_element):
        self.element = box_element
        self.link = Link(self.get_link())
        self.date = Date(self.get_date())

    def get_link(self):
        return self.element.xpath(self.LINK_XPATH)[0]

    def get_date(self):
        return self.element.xpath(self.DATE_XPATH)[0]

class Date:
    def __init__(self, element):
        self.text = element.strip()

URL = 'http://www.animetake.com/'

class Link(List):
    URLNAME_RE = re.escape(URL) + r'([^/]+)'
    
    def __init__(self, element):
        self.name = element.text.strip()
        self.href = element.get('href').strip()

    def parse_urlname(self):
        result = re.match(self.URLNAME_RE, self.href)
        if result:
            return result.group(1)
        return ""

class Item(List):
    TORRENT_XPATH = '//li[@class="tor"]/a'

    def __init__(self, box):
        self.name = box.link.name
        self.href = box.link.href
        self.date = box.date.text
        self.urlname = box.link.parse_urlname()

    def parse_torrents(self):
        page = get_document(self.href)
        torrent_elems = page.xpath(self.TORRENT_XPATH)
        return Link.list(torrent_elems)

def get_document(url):
    r = requests.get(url)
    return html.fromstring(r.text)

BOX_XPATH = '//div[@class="updateinfo" and not(a[.="Announcment"])]'

def get_items():
    document = get_document(URL)
    box_elements = document.xpath(BOX_XPATH)
    boxs = Box.list(box_elements)
    items = Item.list(boxs)
    return items

def items_to_tables(items):
    return { item.urlname: item for item in items }

if __name__ == "__main__":
    items = get_items()
    for item in items:
        print item.name
