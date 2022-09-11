from commands.Icommand import ICommand
from response.exceptions import *
import os, json
from commands.schema_keys import SchemaKeys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

class SetCommand(ICommand):
    def __init__(self, db, table, value, disable_overwrite=False):
        self.db = db
        self.table = table
        self.value = value
        self.disable_overwrite = disable_overwrite
        self.__validate()  

    def __validate(self):
        if(self.value == None):
            raise MissingParameterError("Value to be set is missing.")

        table_path = os.path.join(parent_dir, self.db, self.table)
        if not os.path.exists(table_path):
            raise InvalidParameterError("table does not exist.")

        pk = None
        file = open(os.path.join(table_path, self.table + "_schema.json"), "r")
        table_schema = json.load(file)
        pk = table_schema[SchemaKeys.PRIMARY_KEY]
        file.close()

        disallowed_characters = "{\":},"
        for character in disallowed_characters:
	        self.value = self.value.replace(character, "")
        self.values = self.value.split(" ")

        found_pk = False
        file_name = None
        for i in range(0, len(self.values)-1, 2):
            if self.values[i] not in table_schema[SchemaKeys.COLUMNS]:
                raise ColumnsNotExistInSchema(self.values[i] + " is not a column in " + self.table + " table.")
            if self.values[i] == pk:
                found_pk = True
                file_name = self.values[i+1] + ".json"
        
        if not found_pk:
            raise MissingParameterError("Primary key is missing.")

        self.file_path = os.path.join(table_path, file_name)
        #check if file exists and it is disabled for overwriting
        
    def execute(self): 
        data = {}
        if os.path.exists(self.file_path):
            file = open(self.file_path, "r")
            data = json.load(file)
            file.close()
        
        for i in range(0, len(self.values)-1, 2):
            data[self.values[i]] = self.values[i+1]

        file = open(self.file_path, "w")
        json.dump(data, file)
        file.close()
        