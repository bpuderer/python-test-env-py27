import json

from google.protobuf import json_format

from services.doubler.doubler_pb2 import Number


def build_number_from_dict(d):
    json_str = json.dumps(d)
    return json_format.Parse(json_str, Number())

def build_number_from_file(filename):
    with open(filename) as f:
        json_str = f.read()
    return json_format.Parse(json_str, Number())
