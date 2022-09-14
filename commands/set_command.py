from commands.Icommand import ICommand
from response.exceptions import *
import os, json
from commands.schema_keys import SchemaKeys

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

class SetCommand(ICommand):
    def __init__(self, db, table, value): 
        self.db = db
        self.table = table
        self.value = value
        self.__validate_path() 
        self.__validate_value()

    def __validate_path(self):
        if self.db is None:
            raise MissingParameterError("Database name is missing.")
        if self.table is None:
            raise MissingParameterError("Table name is missing.")

        db_path = os.path.join(parent_dir, self.db)
        if not os.path.exists(db_path):
            raise InvalidParameterError("Database does not exist.")

        table_path = os.path.join(db_path, self.table)
        if not os.path.exists(table_path):
            raise InvalidParameterError("Table does not exist.")

    def __validate_value(self):
        if(self.value == None):
            raise MissingParameterError("Value to be set is missing.")

        self.values = eval(self.value)
        file = open(os.path.join(parent_dir, self.db, self.table, self.table + "_schema.json"), "r")
        table_schema = json.load(file)
        pk = table_schema[SchemaKeys.PRIMARY_KEY]
        file.close()

        if pk not in self.values:
            raise MissingParameterError("Primary key is missing.")
        self.pk = str(self.values[pk])
        
        for key in self.values:
            if key not in table_schema[SchemaKeys.COLUMNS]:
                raise ColumnsNotExistInSchema(key + " is not a column in " + self.table + " table.")
            
        self.file_path = os.path.join(parent_dir, self.db, self.table, self.pk + ".json")
        
        if os.path.exists(self.file_path) and table_schema[SchemaKeys.OVERWRITE] == "False":
            raise InvalidParameterError("Primary key already exists.")
        
    def execute(self): 
        data = {}
        if os.path.exists(self.file_path):
            file = open(self.file_path, "r")
            data = json.load(file)
            self.__remove_from_indices(data)
            file.close()
        self.__add_to_indices()
        file = open(self.file_path, "w")
        data.update(self.values)
        json.dump(data, file)
        file.close()
    
    def __add_to_indices(self):
        for key in self.values:
            idx_path = os.path.join(self.db, self.table, SchemaKeys.INDEX_KEYS, key + ".json")
            # File does not exist means that key is not an index key for the corresponding table 
            if not os.path.exists(idx_path):
                continue 
            file = open(idx_path, "r")
            value = self.values[key]
            data = {}
            try:
                data = json.load(file)
                if value in data:
                    data[value].append(self.pk)
                else:
                    data[value] = [self.pk]
            except json.decoder.JSONDecodeError: # Json file is empty
                data[value] = [self.pk]
            file.close()
            with open(idx_path, "w") as file:
                json.dump(data, file)

    def __remove_from_indices(self, data):
        for key in self.values:
            idx_path = os.path.join(self.db, self.table, SchemaKeys.INDEX_KEYS, key + ".json")
            if not os.path.exists(idx_path):
                continue
            if key in data:
                file = open(idx_path, "r")
                pks = json.load(file)
                file.close()
                pks[data[key]].remove(self.pk)
                # delete key if it has no value
                if not pks[data[key]]:
                    del pks[data[key]]
                file = open(idx_path, "w")
                json.dump(pks, file)
                file.close()


            