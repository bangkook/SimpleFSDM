import os
import json


class IndexValue:
    def __init__(self, index, value_name):
        self.__index = index
        self.__value_name = value_name

    def get_primary_keys(self):
        if "PrimaryKeyIndex" in str(self.__index.__class__):
            return [self.__value_name]
        primary_keys = []
        path = os.path.join(self.__index.get_path(), "{}.json".format(self.__value_name))
        if os.path.isfile(path):
            with open(path, 'r') as file:
                primary_keys = json.load(file)
        return primary_keys

    def get_index(self):
        return self.__index
