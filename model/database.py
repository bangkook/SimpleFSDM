from genericpath import exists
from re import S
from model.table import *

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

class Database:
    def __init__(self, database_obj):
        self.__validate(database_obj)
        self.database_obj = database_obj
        self.name = database_obj[SchemaKeys.DATABASE_NAME]
        self.path = os.path.join(parent_dir, self.name)
        self.tables = self.__create_tables()

    def __validate(self, database_obj):
        if not SchemaKeys.DATABASE_NAME in database_obj:
            raise MissingDataError("Database name is missing")

    def serialize(self):
        self.__create_database()
        self.__serialize_tables()

    def __create_database(self):
        os.makedirs(self.path, exist_ok=True)

    def __create_tables(self):
        tables = []
        for table in self.database_obj[SchemaKeys.TABLES]:
            table[SchemaKeys.PATH] = os.path.join(self.path, table[SchemaKeys.NAME])
            table_obj = Table(table)
            tables.append(table_obj)
        return tables

    def __serialize_tables(self):
        for table_object in self.tables:
            table_object.serialize()