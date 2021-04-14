from flask import Flask, request, render_template, url_for, redirect
from flask_restful import Api, Resource, reqparse
from entity.PokemonEntity import PokemonEntity
from api.GetPokemonHandler import GetPokemonHandler
from api.PostPokemonHandler import PostPokemonHandler
from api.PutPokemonHandler import PutPokemonHandler
from api.DeletePokemonHandler import DeletePokemonHandler

app = Flask(__name__)
api = Api(app)

@app.route("/index", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

parser = reqparse.RequestParser()
parser.add_argument("number")
parser.add_argument("name")
parser.add_argument("types", action='append')

class GetApi(Resource):
    def get(self, pokemon_entity):
        pokemon = PokemonEntity(pokemon_entity)
        # check pokemon in the category or not
        get_pokemon_handler = GetPokemonHandler()
        get_result = get_pokemon_handler.get_handler(pokemon)
        print(get_result)
        return {"Get result:":get_result}

class PostApi(Resource):      
    def post(self):
        args = parser.parse_args()
        post_data = {
            "number":args["number"],
            "name":args["name"],
            "types":args["types"]
        }
        pokemon = PokemonEntity(identifier = post_data["number"], info = post_data)
        post_pokemon_handler = PostPokemonHandler()
        post_result = post_pokemon_handler.post_handler(pokemon.get_info())
        print(post_result)
        return {"Post result:":post_result}

class PutApi(Resource):
    def put(self):
        args = parser.parse_args()
        put_data = {
            "number":args["number"],
            "name":args["name"],
            "types":args["types"]
        }
        pokemon = PokemonEntity(identifier = put_data["number"], info = put_data)
        # check pokemon in the category or not
        put_pokemon_handler = PutPokemonHandler()
        put_result = put_pokemon_handler.put_handler(pokemon.get_info())
        print(put_result)
        return {"Put result":put_result}

class DeleteApi(Resource):
    def delete(self, pokemon_entity):
        pokemon = PokemonEntity(pokemon_entity)
        delete_pokemon = DeletePokemonHandler()
        delete_result = delete_pokemon.delete_handler(pokemon)
        print(delete_result)
        return {"Delete result":delete_result}

# get api
api.add_resource(GetApi,'/pokemondex/<string:pokemon_entity>')
# put api
api.add_resource(PutApi,'/put_pokemon')
# post api
api.add_resource(PostApi,'/post_pokemon')
# delete api
api.add_resource(DeleteApi,'/delete_pokemon/<string:pokemon_entity>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)