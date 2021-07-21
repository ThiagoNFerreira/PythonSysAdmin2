import flask as f
import bson.json_util


def mkbsonresponse(data):
    bson_data = bson.json_util.dumps(data)
    headers = {"Content-Type": "application/json"}
    response = f.Response(bson_data, headers=headers)
    return response