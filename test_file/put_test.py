from requests import put

put_data = {
    "number": "0010",
    "name": "juice",
    "types":{"Fire","Posion"}
}

put('http://localhost:5000/put_pokemon', data=put_data).json()