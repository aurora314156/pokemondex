
from .Handler import Handler
import json

class PostPokemonHandler(Handler):
    def __init__(self):
        pass

    def post_handler(self, pokemon_info):
        poke_number, poke_name, poke_types = pokemon_info["number"], pokemon_info["name"], pokemon_info["types"]
        # pokemon exist do nothing
        if self.get_mapping_info(poke_number, poke_name):
            return 'This pokemon already exist.'
        # otherwise create new pokemon
        return self.create_new_pokemon(poke_number, poke_name, poke_types)
   
    def create_new_pokemon(self, poke_number, poke_name, poke_types):
        # update mapping db
        mapping_db = json.load(open('./Database/mapping_list.json'))
        mapping_db[poke_number] = poke_number
        mapping_db[poke_name] = poke_number
        with open('./Database/mapping_list.json', 'w') as db:
            json.dump(mapping_db, db) 
        
        # update category db
        category_db = json.load(open('./Database/category.json'))
        category_db[poke_number] = {
            "number":poke_number,
            "name":poke_name, 
            "types":poke_types
        }
        with open('./Database/category.json', 'w') as db:
            json.dump(category_db, db)
        
        return 'Post pokemon success.'

    def get_mapping_info(self, poke_number, poke_name):
        # get mapping id and name
        with open('./Database/mapping_list.json') as mapping:
            mapping_dict = json.load(mapping)
        return (poke_number in mapping_dict) and (poke_name in mapping_dict)
