from Icommand import ICommand
import os, json, sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
from SchemaKeys import SchemaKeys

class CreateCommand(ICommand):
    def __init__(self, schema):
        self.schema = schema
        self.data = json.load(open(schema, "r"))

    def execute(self):
        if (self.schema == None or not os.path.exists(os.path.join(parent_dir, self.schema))):
            raise Exception("FileNotFound")

        dir = self.data[SchemaKeys().DATABASE]
        path = os.path.join(parent_dir, dir)
        
        os.makedirs(path, exist_ok = True)

        for table in data[SchemaKeys().TABLES]:
            t_path = os.path.join(path, table[SchemaKeys().NAME])
            os.makedirs(t_path, exist_ok = True)
