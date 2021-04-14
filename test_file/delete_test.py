from requests import delete

delete('http://localhost:5000/delete_pokemon/0010').json()