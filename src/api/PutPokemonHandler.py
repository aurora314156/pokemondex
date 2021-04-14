import json
from .Handler import Handler

class PutPokemonHandler(Handler):
    def __init__(self):
        pass
    def put_handler(self, pokemon_info):
        poke_number, poke_name, poke_types = pokemon_info["number"], pokemon_info["name"], pokemon_info["types"]
        # mapping to list
        mapping_id = self.get_mapping_info(poke_number)
        # pokemon match or not
        if mapping_id == 'None':
            return 'This pokemon not in database.'
        else:
            self.put_match_pokemon(poke_number, poke_name, poke_types)
            return 'Put pokemon info Success.'
    
    def get_mapping_info(self, poke_number):
        # get mapping id
        with open('./Database/mapping_list.json') as mapping:
            mapping_dict = json.load(mapping)
            mapping_id = mapping_dict.get(poke_number, 'None')
        return mapping_id

    def put_match_pokemon(self, poke_number, poke_name, poke_types):
        # update category_db
        category_db = json.load(open('./Database/category.json'))
        category_db[poke_number] = {
            "name":poke_name, 
            "types":poke_types
        }
        with open('./Database/category.json', 'w') as db:
            json.dump(category_db, db)

