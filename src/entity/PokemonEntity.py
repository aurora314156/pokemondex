
class PokemonEntity:
    def __init__(self, identifier = 'None', info = 'None'):
        self.identifier = identifier
        self.info = info
    
    def set_identifier(self, identifier = 'None'):
        self.identifier = identifier
    
    def set_info(self, info = 'None'):
        self.info = info

    def get_identifier(self):
        return self.identifier
    
    def get_info(self):
        return self.info