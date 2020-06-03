import json

def fetch_names(file):
    with open(file, 'r') as f:
        datastore = json.load(f)['tracks']
        roads= []
        for road in datastore:
            roads.append(road['name'])
            if(road['name'] == "basztowa-dunaj-cw"):
                break
        return roads


roads = [
    'bagatela-filharmonia-ccw',
    'filharmonia-gertrudy-ccw',
    'gertrudy-poczta-ccw',
    'gertrudy-poczta-cw',
    'westerplatte-right-ccw',
    'westerplatte-left-ccw',
    'westerplatte-right-cw',
    'westerplatte-left-cw',
    'basztowa-ccw',
    'basztowa-cw',
    'basztowa-dunaj-ccw',
    'basztowa-dunaj-cw'
]

intersections = [

    {
    "name": "bagatela",
    "option1":["dunaj-podwale-prosto","dunaj-karmelicka-skret"],
    "option2": ["karmelicka-podwale-skret",  "karmelicka-dunaj-skret", ]
    },

    {
    "name": "filharmonia",
    "option1": ["strasz-strasz-prosto"],
    "option2": [],
     "list": [ "zwierzyniecka-strasz-skret", "franc-strasz-skret", "strasz-franc-skret"]
    },

    {"name": "idziego",
     "list": ["idziego-gertrudy-skret", "idziego-stradom-prosto", "bernard-gertrudy-prosto", "gertrudy-stradom-skret","bernard-stradom-skret","stradom-gert-skret"]},

    {"name": "poczta",
     "list": ["gertrudy-westerplatte-prosto","gertrudy-staro-skret","gertrudy-sienna-skret","westerplatte-gertrudy-prosto"
              "westerplatte-sienna-skret","westerplatte-staro-skret","staro-sienna-prosto","staro-westerplatte-skret",
              "staro-gertrudy-skret","sienna-staro-prosto","sienna-gertrudy-skret","sienna-westerplatte-skret"]},

    {"name": "slowackiego",
     "list": ["basztowa-lubicz-prosto","basztowa-westerplatte-skret","westerplatte-pawia-prosto",
              "westerplatte-lubicz-skret","westerplatte-basztowa-skret","pawia-westerplatte-prosto",
              "pawia-basztowa-skret","lubicz-pawia-skret","lubicz-basztowa-prosto","lubicz-westerplatte-skret"]},

    {"name": "kleparz",
     "list": ["basztowa-ccw-basztowa-prosto", "basztowa-cw-basztowa-prosto", "dluga-basztowa-cw-skret", "dluga-basztowa-ccw-skret"]},

]




