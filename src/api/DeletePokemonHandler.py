from .Handler import Handler
import json

class DeletePokemonHandler(Handler):
    def __init__(self):
        pass

    def delete_handler(self, pokemon_entity):
        # mapping to list
        mapping_id = self.get_mapping_info(pokemon_entity)
        # pokemon match or not
        if mapping_id == 'None':
            return self.miss_match(pokemon_entity)
        else:
            return self.delete_match_pokemon(mapping_id)

    def get_mapping_info(self, pokemon_entity):
        # get mapping id
        with open('./Database/mapping_list.json') as mapping:
            mapping_dict = json.load(mapping)
            mapping_id = mapping_dict.get(pokemon_entity.get_identifier(), 'None')
        return mapping_id
    
    def miss_match(self, pokemon_entity):
        return 'This pokemon not in database.'

    def delete_match_pokemon(self, mapping_id):
        # delete match pokemon both on mapping_list db and category db            
        # update mapping db
        mapping_db = json.load(open('./Database/mapping_list.json'))
        mapping_db_keys = mapping_db.keys()
        delete_list = []
        for key in mapping_db_keys:
            if mapping_db[key] == mapping_id:
                delete_list.append(key)
        for delete_key in delete_list:
            del mapping_db[delete_key]
        with open('./Database/mapping_list.json', 'w') as db:
            json.dump(mapping_db, db)
        
        # update category db
        category_db = json.load(open('./Database/category.json'))
        del category_db[mapping_id]
        with open('./Database/category.json', 'w') as db:
            json.dump(category_db, db)
        
        return 'Delete pokemon success.'


    
