from requests import post

post_data = {
    "number": "0010",
    "name": "test0010",
    "types": [
        "Grass",
        "Poison" 
    ]
}

post('http://localhost:5000/post_pokemon', data=post_data).json()