import json
import os
import pathlib
from response.exceptions import *
from schema_keys import SchemaKeys

FILE_EXTENSION = ".json"
PRIMARY_KEYS = "primary_keys"


class Index:
    def __init__(self, index_name, metadata):
        self.__path = os.path.join(metadata.get_path(), SchemaKeys.INDEX_KEYS, index_name)
        self.name = index_name

    def serialize(self):
        os.makedirs(self.__path, exist_ok=True)

    @staticmethod
    def __validate_index__(index_name, table_columns):
        if index_name not in table_columns:
            raise InvalidParameterError("Index {} not found".format(index_name))

    @staticmethod
    def __validate_value_name__(value_name):
        if len(value_name) == 0 or value_name.isspace():
            raise MissingParameterError("value_name parameter not entered")

    def __validate_index__(index_name, table_columns):
        if index_name not in table_columns:
            raise IvalidParameterError("Index {} not found".format(index_name))

    def get_primary_keys(self, value_name):
        value_path = os.path.join(self.__path, value_name + FILE_EXTENSION)
        Index.__validate_value_name__(value_name)
        if not os.path.exists(value_path):
            return []
        with open(value_path, "r") as file:
            return json.load(file)[PRIMARY_KEYS]

    def __update_primary_keys(self, value_name, primary_keys):
        value_path = os.path.join(self.__path, value_name + FILE_EXTENSION)
        with open(value_path, "w") as file:
            json.dump({PRIMARY_KEYS: primary_keys}, file)

    def __update_value__(path, value_name, primary_keys):
        with open(os.path.join(path, "{}.json".format(value_name)), 'w') as file:
            json.dump(primary_keys, file)

    def add_index(self, value_name, pk):
        primary_keys = self.get_primary_keys(value_name)
        primary_keys.append(pk)
        self.__update_primary_keys(value_name, primary_keys)

    def add_value(self, value_name, primary_key):
        value = self.get_primary_keys(value_name)
        value.append(primary_key)
        self.__update_value__(self.__path, value_name, value)

    def remove_value(self, value_name, primary_key):
        value = self.get_primary_keys(value_name)
        if primary_key in value:
            value.remove(primary_key)
        if not value:
            pathlib.Path(os.path.join(self.__path, "{}.json".format(value_name))).unlink()
        else:
            self.__update_value__(self.__path, value_name, value)

    def remove_index(self, value_name, pk):
        primary_keys = self.get_primary_keys(value_name)
        if pk in primary_keys:
            primary_keys.remove(pk)
        if not primary_keys:  # file is empty
            os.remove(os.path.join(self.__path, value_name + FILE_EXTENSION))
        else:
            self.__update_primary_keys(value_name, primary_keys)
