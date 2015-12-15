from requests import get

FLATS_2_ROOM = "http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/krakow/v1c9008l3200208p1?pr=,1500&nr=2&fr=ownr"
STUDIO = "http://www.gumtree.pl/s-mieszkania-i-domy-do-wynajecia/krakow/v1c9008l3200208p1?pr=,1500&fr=ownr&nr=10"


def flats_2_room():
    return get(FLATS_2_ROOM).text.encode('utf-8', errors='ignore')


def studio():
    return get(STUDIO).text.encode('utf-8', errors='ignore')
