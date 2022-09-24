import json
import os
from Icommand import *
from model.database import Database
from response.exceptions import *

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


class CreateCommand(ICommand):
    def __init__(self, schema_path):
        self.schema_path = schema_path
        self.__validate_and_load_schema()

    def __validate_and_load_schema(self):
        if self.schema_path is None or not os.path.exists(os.path.join(parent_dir, self.schema_path)):
            raise FileNotFound("Schema path not found")
        try:
            with open(self.schema_path, "r") as schema_file:
                self.database_obj = json.load(schema_file)
        except:
            raise ErrorLoadingFile("Error loading Json file")

    def execute(self):
        database = Database(self.database_obj)
        database.serialize()
