from commands.Icommand import ICommand
from commands.exceptions import *
import os, json, sys
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir)
from schema_keys import SchemaKeys

class CreateCommand(ICommand):
    def __init__(self, schema_path):
        self.schema_path = schema_path
        self.__validate_and_load_schema()  

    def __validate_and_load_schema(self):
        if (self.schema_path == None or not os.path.exists(os.path.join(parent_dir, self.schema_path))):
            raise FileNotFound()
        try:  
            with open (self.schema_path, "r") as schema_file:
                self.data = json.load(schema_file)
        except:
            raise ErrorLoadingFile()

        if not SchemaKeys.DATABASE in self.data:
            raise DatabaseNameIsMissing()
        
    def execute(self):  
        self.__create_database()
        self.__create_tables()

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
