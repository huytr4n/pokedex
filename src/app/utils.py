from flask import Flask, make_response, request, current_app, abort
from datetime import timedelta
from functools import update_wrapper

JSON_MIME_TYPE = 'application/json'


def search_pokedexes_by_name(pokedexes, query):
    return [pokedex for pokedex in pokedexes if query in pokedex['name']]


def json_response(data='', status=200, headers=None):
    headers = headers or {}
    if 'Content-Type' not in headers:
        headers['Content-Type'] = JSON_MIME_TYPE

    return make_response(data, status, headers)


def get_paginated_list(results, url, offset, limit):
    offset = int(offset)
    limit = int(limit)
    count = len(results)
    obj = {}

    if count == 0:
        obj['offset'] = offset
        obj['limit'] = limit
        obj['count'] = count
        obj['previous'] = None
        obj['next'] = None
        obj['results'] = results
        return obj

    if count < offset or limit < 0:
        abort(404)

    # make response
    obj['offset'] = offset
    obj['limit'] = limit
    obj['count'] = count

    # make URLs
    # make previous url
    if offset == 1:
        obj['previous'] = None
    else:
        offset_copy = max(1, offset - limit)
        obj['previous'] = url + '?offset=%d&limit=%d' % (offset_copy, limit)

    # make next url
    if offset + limit > count:
        obj['next'] = None
    else:
        offset_copy = offset + limit
        obj['next'] = url + '?offset=%d&limit=%d' % (offset_copy, limit)
        
    # finally extract result according to bounds
    obj['results'] = results[(offset - 1):(offset - 1 + limit)]
    return obj


def crossdomain(origin=None, methods=None, headers=None, max_age=21600, attach_to_all=True, automatic_options=True):  
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, str):
        headers = ', '.join(x.upper() for x in headers)
    if not isinstance(origin, str):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)
    return decorator