# Public API for Pokedex

## Versioning

- Python 3.7
- Flask

## How to run

Install dependencies

```markdown
pip install -r requirements.txt
```

Config and run Flask server

```markdown
export FLASK_APP=src/run.py
export FLASK_ENV=development

flask run
```

Check out your APIs at: http://localhost:5000/

## APIs sample

1. Get list pokedexes

    - URL: localhost:5000/pokedexes?start=1&limit=20
    - Response:

        ```json
        {
            "start": 1,
            "limit": 20,
            "count": 809,
            "previous": "",
            "next": "http://localhost:5000/pokedexes?start=21&limit=20",
            "results": [
                {
                    "id": 1,
                    "name": "Bulbasaur",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/001.png"
                },
                {
                    "id": 2,
                    "name": "Ivysaur",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/002.png"
                },
                {
                    "id": 3,
                    "name": "Venusaur",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/003.png"
                },
                {
                    "id": 4,
                    "name": "Charmander",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/004.png"
                },
                {
                    "id": 5,
                    "name": "Charmeleon",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/005.png"
                },
                {
                    "id": 6,
                    "name": "Charizard",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/006.png"
                },
                {
                    "id": 7,
                    "name": "Squirtle",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/007.png"
                },
                {
                    "id": 8,
                    "name": "Wartortle",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/008.png"
                },
                {
                    "id": 9,
                    "name": "Blastoise",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/009.png"
                },
                {
                    "id": 10,
                    "name": "Caterpie",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/010.png"
                },
                {
                    "id": 11,
                    "name": "Metapod",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/011.png"
                },
                {
                    "id": 12,
                    "name": "Butterfree",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/012.png"
                },
                {
                    "id": 13,
                    "name": "Weedle",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/013.png"
                },
                {
                    "id": 14,
                    "name": "Kakuna",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/014.png"
                },
                {
                    "id": 15,
                    "name": "Beedrill",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/015.png"
                },
                {
                    "id": 16,
                    "name": "Pidgey",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/016.png"
                },
                {
                    "id": 17,
                    "name": "Pidgeotto",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/017.png"
                },
                {
                    "id": 18,
                    "name": "Pidgeot",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/018.png"
                },
                {
                    "id": 19,
                    "name": "Rattata",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/019.png"
                },
                {
                    "id": 20,
                    "name": "Raticate",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/020.png"
                }
            ]
        }
        ```

2. Filter list pokedexes by name

    - URL: localhost:5000/pokedexes?query=zu
    - Response:

        ```json
        {
            "start": 1,
            "limit": 20,
            "count": 2,
            "previous": "",
            "next": "",
            "results": [
                {
                    "id": 184,
                    "name": "Azumarill",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/184.png"
                },
                {
                    "id": 298,
                    "name": "Azurill",
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/298.png"
                }
            ]
        }
        ```
