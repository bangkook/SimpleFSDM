from table import Table
import os
from schema_keys import *
from response.exceptions import *

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


class Database:
    def __init__(self, database_obj=None, database_name=None):
        Database.__validate(database_obj, database_name)
        if database_obj is not None:
            self.__initialize_by_schema_data__(database_obj)
        else:
            self.__initialize_by_database_name__(database_name)

    def __initialize_by_schema_data__(self, database_obj):
        self.__path = os.path.join(parent_dir, database_obj[SchemaKeys.DATABASE_NAME])
        self.__database_name = database_obj[SchemaKeys.DATABASE_NAME]
        self.__create_tables(database_obj[SchemaKeys.TABLES])

    def __initialize_by_database_name__(self, database_name):
        self.__path = os.path.join(parent_dir, database_name)
        if not os.path.exists(self.__path):
            raise InvalidParameterError("Wrong database entered")
        self.__database_name = database_name
        self.__create_tables(os.listdir(self.__path))

    def __validate(database_obj, database_name):
        if ((database_obj is None or database_obj[SchemaKeys.DATABASE_NAME].isspace()) and
                (database_name is None or str(database_name).isspace())):
            raise MissingDataError("Database name is missing")

    def get_path(self):
        return self.__path

    def serialize(self):
        os.makedirs(self.__path, exist_ok=True)
        self.__serialize_tables()

    def __create_tables(self, tables_data):
        self.tables = {}
        for table_name in tables_data:
            self.tables[table_name] = Table(self, table_name=table_name)

    def __serialize_tables(self):
        for table_object in self.tables:
            table_object.serialize()

    def get_table(self, table_name):
        if table_name not in self.tables:
            raise InvalidParameterError ("Invalid table is entered")
        return self.tables[table_name]

    def set(self, table_name, data):
        table = self.get_table(table_name)
        table.set(data)
