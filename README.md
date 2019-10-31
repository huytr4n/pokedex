# Public API for Pokedex

## Versioning

- Python 3.7
- Flask

## How to run

- Required install Docker.

- Build your first Python-Flask image using Docker.

    ```docker
    docker build -t flask-docker .
    ```

- Flask run.

    ```docker
    docker run -it --rm -e HOSTNAME=0.0.0.0 -p 5000:5000 flask-docker
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
                    "type": [
                        "Grass",
                        "Poison"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/001.png"
                },
                {
                    "id": 2,
                    "name": "Ivysaur",
                    "type": [
                        "Grass",
                        "Poison"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/002.png"
                },
                {
                    "id": 3,
                    "name": "Venusaur",
                    "type": [
                        "Grass",
                        "Poison"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/003.png"
                },
                {
                    "id": 4,
                    "name": "Charmander",
                    "type": [
                        "Fire"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/004.png"
                },
                {
                    "id": 5,
                    "name": "Charmeleon",
                    "type": [
                        "Fire"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/005.png"
                },
                {
                    "id": 6,
                    "name": "Charizard",
                    "type": [
                        "Fire",
                        "Flying"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/006.png"
                },
                {
                    "id": 7,
                    "name": "Squirtle",
                    "type": [
                        "Water"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/007.png"
                },
                {
                    "id": 8,
                    "name": "Wartortle",
                    "type": [
                        "Water"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/008.png"
                },
                {
                    "id": 9,
                    "name": "Blastoise",
                    "type": [
                        "Water"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/009.png"
                },
                {
                    "id": 10,
                    "name": "Caterpie",
                    "type": [
                        "Bug"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/010.png"
                },
                {
                    "id": 11,
                    "name": "Metapod",
                    "type": [
                        "Bug"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/011.png"
                },
                {
                    "id": 12,
                    "name": "Butterfree",
                    "type": [
                        "Bug",
                        "Flying"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/012.png"
                },
                {
                    "id": 13,
                    "name": "Weedle",
                    "type": [
                        "Bug",
                        "Poison"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/013.png"
                },
                {
                    "id": 14,
                    "name": "Kakuna",
                    "type": [
                        "Bug",
                        "Poison"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/014.png"
                },
                {
                    "id": 15,
                    "name": "Beedrill",
                    "type": [
                        "Bug",
                        "Poison"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/015.png"
                },
                {
                    "id": 16,
                    "name": "Pidgey",
                    "type": [
                        "Normal",
                        "Flying"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/016.png"
                },
                {
                    "id": 17,
                    "name": "Pidgeotto",
                    "type": [
                        "Normal",
                        "Flying"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/017.png"
                },
                {
                    "id": 18,
                    "name": "Pidgeot",
                    "type": [
                        "Normal",
                        "Flying"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/018.png"
                },
                {
                    "id": 19,
                    "name": "Rattata",
                    "type": [
                        "Normal"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/019.png"
                },
                {
                    "id": 20,
                    "name": "Raticate",
                    "type": [
                        "Normal"
                    ],
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
                    "type": [
                        "Water",
                        "Fairy"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/184.png"
                },
                {
                    "id": 298,
                    "name": "Azurill",
                    "type": [
                        "Normal",
                        "Fairy"
                    ],
                    "image_url": "https://raw.githubusercontent.com/fanzeyi/pokemon.json/master/images/298.png"
                }
            ]
        }
        ```
