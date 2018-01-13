import json

from services.doubler.doubler_pb2 import Number

def build_number(val):
    return Number(value=val)

def build_number_from_file(filename):
    with open(filename) as f:
        req_json = json.load(f)
    return build_number(req_json['value'])
