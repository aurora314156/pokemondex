
from abc import ABCMeta, abstractmethod

class Handler(metaclass=ABCMeta):
    def __init__(self):
        pass
    
    @abstractmethod
    def get_mapping_info(self, pokemon_entity):
        pass
    

