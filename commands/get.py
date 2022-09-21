import json
from model.database import *
from commands.Icommand import *
import os.path

pd = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

class GetAPI(ICommand):


    def __init__(self, db, table, value):
        self.db = db
        self.table = table
        self.value = value

    def validate(db, table, value):
     pd = os.getcwd()
     file_list = os.listdir(pd)
     if db not in file_list:
         raise InvalidParameterError("database not found")
     if Table not in GetAPI.get_data(db):
         raise InvalidParameterError("table not found")
     if value not in GetAPI.get_data(db).values():
         raise InvalidParameterError("value not found")
     return

    def get_data(self, db):
        f = open(db)
        data = json.load(f)
        return data

    def execute(db, table, value, files=None):
        if db != "":
            if table != "":
                return GetAPI.get_data(db)[value]
            else:
                return GetAPI.get_data(db)
        else:
            files[]
            for file in os.listdir(pd):
                files.append(os.path.join(pd, file))
            for file in files:
                if value in GetAPI.get_data(db).values():
                    print(GetAPI.get_data(db))
