from Icommand import ICommand
import os, json, sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
from SchemaKeys import SchemaKeys

class CreateCommand(ICommand):
    def __init__(self, schema):
        self._schema = schema

    def execute(self):
        if (self._schema == None or not os.path.exists(parent_dir + "/" + self._schema)):
            raise Exception("FileNotFound")

        schema_file = open(self._schema, "r")
        data = json.load(schema_file)
        dir = data[SchemaKeys().DATABASE]
        path = os.path.join(parent_dir, dir)

        if not os.path.exists(path):
            os.mkdir(path)

        for table in data[SchemaKeys().TABLES]:
            t_path = os.path.join(path, table[SchemaKeys().NAME])
            if not os.path.exists(t_path):
                os.mkdir(t_path)
