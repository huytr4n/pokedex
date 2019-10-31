from flask import make_response, abort

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
        limit_copy = offset - 1
        obj['previous'] = url + '?offset=%d&limit=%d' % (offset_copy, limit_copy)

    # make next url
    if offset + limit > count:
        obj['next'] = ''
    else:
        offset_copy = offset + limit
        obj['next'] = url + '?offset=%d&limit=%d' % (offset_copy, limit)
        
    # finally extract result according to bounds
    obj['results'] = results[(offset - 1):(offset - 1 + limit)]
    return obj