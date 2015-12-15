from iot.github.morgaroth.flat.finder.requets import flats_2_room
from iot.github.morgaroth.utils.ModuleLoad import MyModuleLoadError

try:
    from bs4 import BeautifulSoup
except:
    raise MyModuleLoadError("beatifulsoup4")


class Ogloszenie(object):
    def __init__(self, id, price, link):
        super().__init__()
        self.link = link
        self.price = price
        self.id = id

    def __repr__(self, *args, **kwargs):
        return "%s %s %s\n" % (self.id, self.price, self.link)


def load_floats_list():
    p = BeautifulSoup(flats_2_room(), "html.parser")
    gt_li = p.findAll('li', attrs={'class': 'result pictures'})
    results = []
    for elem in gt_li:
        results.append(Ogloszenie(
                elem.get('data-adid'),
                elem.find('span', attrs={'class': 'amount'}).contents[0],
                elem.find('a', attrs={'class': 'href-link'}).contents[0]
        ))
    return results


def test_this_script():
    print(load_floats_list())


test_this_script()
