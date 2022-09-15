from response.exceptions import *
from commands.schema_keys import SchemaKeys
import os, json

FILE_EXTENSION = ".json"
PRIMARY_KEYS = "primary_keys"

class Index:
    def __init__(self, index_name, metadata):
        self.__path = os.path.join(metadata.path, SchemaKeys.INDEX_KEYS, index_name)
        self.name = index_name
        
    def serialize(self):
        os.makedirs(self.__path, exist_ok=True)

    def get_primary_keys(self, value_name):
        value_path = os.path.join(self.__path, value_name + FILE_EXTENSION)
        if not os.path.exists(value_path):
            raise InvalidParameterError()
        with open(value_path, "r") as file:
            return json.load(file)[PRIMARY_KEYS]

    def add_index(self, value_name, pk):
        value_path = os.path.join(self.__path, value_name + FILE_EXTENSION)
        primary_keys = None
        if os.path.exists(value_path):
            primary_keys = self.get_primary_keys(value_name)
            primary_keys.append(pk)
        else:
            primary_keys = [pk]

        with open(value_path, "w") as file:
            json.dump({PRIMARY_KEYS : primary_keys}, file)

    def remove_index(self, value_name, pk):
        value_path = os.path.join(self.__path, value_name + FILE_EXTENSION)
        if not os.path.exists(value_path):
            raise InvalidParameterError()

        primary_keys = self.get_primary_keys(value_name)
        if pk in primary_keys: 
            primary_keys.remove(pk)
        
        if not primary_keys: # file is empty
            os.remove(value_path)
        else:
            with open(value_path, "w") as file:
                json.dump({PRIMARY_KEYS : primary_keys}, file)