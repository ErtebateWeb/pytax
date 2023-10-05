import json
from collections import OrderedDict

def normalize_json(data):
    def flatten(d, parent_key=''):
        items = []
        for k, v in d.items():
            new_key = parent_key + '.' + k if parent_key else k
            if isinstance(v, dict):
                items.extend(flatten(v, new_key).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def flatten_list(data_list, parent_key):
        items = []
        for i, item in enumerate(data_list):
            flat_item = flatten(item, parent_key + f'[{i}]')
            items.extend(flat_item.items())
        return dict(items)

    if isinstance(data, str):
        data = json.loads(data)

    flattened_data = flatten(data)
    flattened_data = flatten_list(flattened_data.get('body', []), 'body')

    ordered_data = OrderedDict(sorted(flattened_data.items()))

    normalized = ''

    for k, v in ordered_data.items():
        if v is None:
            v = '###'
        elif isinstance(v, bool):
            v = str(v).lower()
        elif isinstance(v, float):
            v = str(v)
        elif isinstance(v, int):
            v = str(v)

        normalized += str(v) + '#'

    return normalized[:-1]

data = {
    "header": {
        "taxid": "AA56CD0E0620002F2B4E78",
        "indatim": "1655620821274",
        "indati2m": "1655620821274",
        "inty": 2,
        "inno": "0002F2B4E7",
        "irtaxid": None,
        "inp": 1, "ins": 1,
        "tins": "32652362589632",
        "tob": 1,
        "bid": None,
        "tinb": None,
        "sbc": None,
        "bpc": None,
        "bbc": None,
        "ft": None,
        "bpn": None,
        "scln": None,
        "scc": None,
        "crn": None,
        "billid": None,
        "tprdis": 1000000,
        "tdis": 0,
        "tadis": 1000000,
        "tvam": 90000,
        "todam": 0,
        "tbill": 1090000,
        "setm": 1,
        "cap": 90000,
        "insp": 0,
        "tvop": 90000,
        "dpvb": None,
        "tax17": None
    },
    "body": [
        {
            "sstid": 2153265989636,
            # "sstt": "پاستیل میوه ای شیبابا",
            "sstt": "pastil",
            "mu": 96,
            "am": 1,
            "fee": 1000000,
            "cfee": None,
            "cut": None,
            "exr": None,
            "prdis": 1000000,
            "dis": 0,
            "adis": 1000000,
            "vra": 0.09,
            "vam": 90000,
            "odt": None,
            "odr": None,
            "odam": None,
            "olt": None,
            "olr": None,
            "olam": None,
            "consfee": None,
            "spro": None,
            "bros": None,
            "tcpbs": None,
            "cop": 90000,
            "vop": 90000,
            "bsrn": None,
            "tsstam": 1090000
        }
    ],
    "payments": [
        {
            "iinn": 5646556,
            "acn": 5656565,
            "trmn": 54554224,
            "trn": 544542424,
            "pcn": "6037-9972-9856-9865",
            "pid": None,
            "pdt": 1655620821274
        }
    ],
    "extension": [
        {
            "key": None,
            "value": None
        }
    ]
}

print(normalize_json(json.dumps(data)))
