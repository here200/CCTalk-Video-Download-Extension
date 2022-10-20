import json
import jsonpath

cache = None


def json_string2python_object(json_string):
    return json.loads(json_string)


def get_data(expression, obj=None):
    if obj is None:
        obj = cache
    return jsonpath.jsonpath(obj, expression)


def get_one_data(expression, obj=None):
    if obj is None:
        obj = cache
    return jsonpath.jsonpath(obj, expression)[0]
