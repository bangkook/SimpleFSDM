from Icommand import ICommand
import os, json, sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
from SchemaKeys import SchemaKeys

class CreateCommand(ICommand):
    def __init__(self, schema):
        self.__validate_schema(schema)
        self.data = json.load(open(schema, "r"))

    def __validate_schema(self, schema):
        if (schema == None or not os.path.exists(os.path.join(parent_dir, schema))):
            raise Exception("FileNotFound")
        data = json.load(open(schema, "r"))
        if not SchemaKeys.DATABASE in data:
            raise Exception("DatabaseNameIsMissing")
        
    def execute(self):    
        dir = self.data[SchemaKeys.DATABASE]
        path = os.path.join(parent_dir, dir)
        
        os.makedirs(path, exist_ok = True)
        
        if not SchemaKeys.TABLES in self.data:
            return
        
        for table in self.data[SchemaKeys.TABLES]:
            t_path = os.path.join(path, table[SchemaKeys.NAME])
            os.makedirs(t_path, exist_ok = True)
