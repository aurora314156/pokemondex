import json
from .Handler import Handler

class GetPokemonHandler(Handler):
    def __init__(self):
        pass
    def get_handler(self, pokemon_entity):
        # mapping to list
        mapping_id = self.get_mapping_info(pokemon_entity)
        # pokemon match or not
        if mapping_id == 'None':
            return self.miss_match(pokemon_entity)
        else:
            return self.match_pokemon(pokemon_entity, mapping_id)
    
    def get_mapping_info(self, pokemon_entity):
        # get mapping id
        with open('./Database/mapping_list.json') as mapping:
            mapping_dict = json.load(mapping)
            mapping_id = mapping_dict.get(pokemon_entity.get_identifier(), 'None')
        return mapping_id

    def miss_match(self, pokemon_entity):
        pokemon_entity.set_info('This pokemon not in database.')
        return 'This pokemon not in database.'

    def match_pokemon(self, pokemon_entity, mapping_id):
        # get pokemon information from db
        with open('./Database/category.json') as db:
            pokemon_list = json.load(db)
            pokemon_info = pokemon_list.get(pokemon_entity.get_identifier())
            pokemon_entity.set_info(pokemon_info)
        return 'Get your pokemon info success.'
    

