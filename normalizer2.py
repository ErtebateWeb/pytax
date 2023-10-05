import json
import collections
import re

def normalize_json(input_json):
    def flat_map(result, root_key, input):
        if isinstance(input, list):
            for i, item in enumerate(input):
                flat_map(result, f'{root_key}[{i}]', item)
        elif isinstance(input, dict):
            for key, value in input.items():
                flat_map(result, f'{root_key}.{key}' if root_key else key, value)
        else:
            result[root_key] = input

    def normalize_text(text):
        if text is None or text == "":
            return "###"
        else:
            return re.sub(r'#', '##', text)

    def sort_key(item):
        return item[0]

    result = {}
    flat_map(result, None, input_json)
    sorted_result = collections.OrderedDict(sorted(result.items(), key=sort_key))
    normalized_values = [normalize_text(str(value)) for value in sorted_result.values()]
    return '#'.join(normalized_values)

# JSON نمونه
# sample_json = {
#     "k2": "v1",
#     "k4": "v2",
#     "k3": {
#         "k1": "v4",
#         "k5": "v5"
#     }
# }

data ={
    "header" :
    {
    "taxid": "AA56CD0E0620002F2B4E78",
    "indatim": "1655620821274",
    "indati2m": "1655620821274",
    "inty": 2,
    "inno" : "0002F2B4E7",
    "irtaxid" : None,  # به جای null از None استفاده شود
    "inp": 1,"ins" : 1,
    "tins" : "32652362589632",
    "tob" : 1,
    "bid" : None,
    "tinb" : None,
    "sbc" : None,
    "bpc" : None,
    "bbc" : None,
    "ft" : None,
    "bpn" : None,
    "scln" : None,
    "scc" : None,
    "crn" : None,
    "billid" : None,
    "tprdis" : 1000000,
    "tdis" : 0,
    "tadis" : 1000000,
    "tvam" : 90000,
    "todam" : 0,
    "tbill" : 1090000,
    "setm" : 1,
    "cap" : 90000,
    "insp" : 0,
    "tvop" : 90000,
    "dpvb" : None,
    "tax17" : None
    },
    "body" : [
    {
    "sstid" : 2153265989636,
    "sstt" : "پاستیل میوه ای شیبابا" ,
    "mu" : 96,
    "am" : 1,
    "fee" : 1000000,
    "cfee" :None,  # به جای null از None استفاده شود
    "cut" : None,
    "exr" : None,
    "prdis" : 1000000,
    "dis" : 0,
    "adis" : 1000000,
    "vra" : 0.09,
    "vam" : 90000,
    "odt" : None,
    "odr" : None,
    "odam" : None,
    "olt" : None,
    "olr" : None,
    "olam" : None,
    "consfee" : None,
    "spro" : None,
    "bros" : None,
    "tcpbs" : None,
    "cop" : 90000,
    "vop" : 90000,
    "bsrn" : None,
    "tsstam" : 1090000
    }
    ],
    "payments" : [
    {
    "iinn" : 5646556,
    "acn" : 5656565,
    "trmn" : 54554224,
    "trn" : 544542424,
    "pcn" : "6037-9972-9856-9865",
    "pid" : None,
    "pdt" : 1655620821274
    }
    ],
    "extension": [
    {
    "key" : None,
    "value" : None
    }
    ]
}


    
# نرمال‌سازی JSON
normalized_string = normalize_json(data)
print(normalized_string)
