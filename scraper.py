from lxml import html

URL = 'http://www.animetake.com/'
DL_PAGE_LINK_XPATH = '//div[@class="updateinfo"]/h4/a'
TORRENT_LINK_XPATH = '//li[@class="tor"]/a'

document = html.parse(URL)

def parse_torrents(link):
    page = html.parse(link.href)
    torrent_elems = page.xpath(TORRENT_LINK_XPATH)
    return Link.lister(torrent_elems)

def get_items():
    link_elems = document.xpath(DL_PAGE_LINK_XPATH)
    links = Link.lister(link_elems)
    # items = Item.lister(links)
    # return items
    return links

class Lister:
    @classmethod
    def lister(cls, elems):
        return [cls(el) for el in elems]

class Link(Lister):
    def __init__(self, element):
        self.name = element.text
        self.href = element.get('href')

class Item(Lister):
    def __init__(self, link):
        self.name = link.name
        self.torrents = parse_torrents(link)

if __name__ == "__main__":
    items = get_items()
    for item in items:
        print item.name
        # print [tor.href for tor in item.torrents]