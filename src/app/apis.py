import json
from flask import Flask, Response, abort, request

from app import app
from app.utils import (
    JSON_MIME_TYPE, 
    search_pokedexes_by_name, 
    get_paginated_list
)
from app.database import init_app

pokedexes = init_app()

@app.route('/pokedexes')
def list_pokedexes():
    """
    List all pokedexes with pagination.
    Can filter the list by name with args is query.
    """

    query = request.args.get('query', '')
    results = pokedexes
    url = request.host_url + 'pokedexes'

    if query:
        results = search_pokedexes_by_name(pokedexes, query)

    pokedexes_paginated = get_paginated_list(
        results, 
        url, 
        start=request.args.get('start', 1), 
        limit=request.args.get('limit', 20)
    )
    response = Response(
        json.dumps(pokedexes_paginated), 
        status=200, 
        mimetype=JSON_MIME_TYPE
    )

    return response