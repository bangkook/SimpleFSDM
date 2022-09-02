from Icommand import ICommand
import os, json, sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
from SchemaKeys import SchemaKeys

class CreateCommand(ICommand):
    def __init__(self, schema_path):
        self.__validate_and_load_schema(schema_path)

    def __validate_and_load_schema(self, schema_path):
        if (schema_path == None or not os.path.exists(os.path.join(parent_dir, schema_path))):
            raise Exception("FileNotFound")

        try:  
            self.data = json.load(open(schema_path, "r"))
        except:
            raise Exception("ErrorLoadingJsonFile")

        if not SchemaKeys.DATABASE in self.data:
            raise Exception("DatabaseNameIsMissing")
        
    def execute(self):    
        self.__create_database()
        self.__create_tables()
        return "Succefully executed create command"

    def __create_database(self):
        dir = self.data[SchemaKeys.DATABASE]
        path = os.path.join(parent_dir, dir)
        os.makedirs(path, exist_ok = True)

    def __create_tables(self):
        if not SchemaKeys.TABLES in self.data:
            return

        path = os.path.join(parent_dir, self.data[SchemaKeys.DATABASE])

        for table in self.data[SchemaKeys.TABLES]:
            t_path = os.path.join(path, table[SchemaKeys.NAME])
            os.makedirs(t_path, exist_ok = True)
