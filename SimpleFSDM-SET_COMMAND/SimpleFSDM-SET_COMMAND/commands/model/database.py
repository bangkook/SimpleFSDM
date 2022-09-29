import table
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))


class Database:
    def __init__(self, database_obj=None,database_name=None):
        Database.__validate(database_obj)
        self.__database_obj = database_obj
        self.name = database_obj[SchemaKeys.DATABASE_NAME]
        self.__path = os.path.join(parent_dir, self.name)
        self.tables = self.__create_tables()

    def __validate(database_obj):
        if not SchemaKeys.DATABASE_NAME in database_obj or str(SchemaKeys.DATABASE_NAME).isspace():
            raise MissingDataError("Database name is missing")

    def get_path(self):
        return self.__path

    def serialize(self):
        os.makedirs(self.__path, exist_ok=True)
        self.__serialize_tables()

    def __create_tables(self):
        tables = []
        for table in self.__database_obj[SchemaKeys.TABLES]:
            table_obj = Table(table, self)
            tables.append(table_obj)
        return tables

    def __serialize_tables(self):
        for table_object in self.tables:
            table_object.serialize()

    def get_table(self, table_name):
        if table_name not in self.tables:
            raise WrongParameterError("Wrong table entered")
        return self.tables[table_name]

    def set(self, table_name, data):
        table = self.get_table(table_name)
        table.set(data)
        