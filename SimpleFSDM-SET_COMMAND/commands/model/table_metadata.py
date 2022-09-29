from index import *
from schema_keys import *
from response.exceptions import *


class TableMetaData:
    def __init__(self, table):
        TableMetaData.__validate__(table.table_schema)
        self.__path = table.get_path()
        self.name = table.table_schema[SchemaKeys.NAME]
        self.primary_key = table.table_schema[SchemaKeys.PRIMARY_KEY]
        self.columns = table.table_schema[SchemaKeys.COLUMNS]
        self.overwrite = table.table_schema[SchemaKeys.OVERWRITE]
        self.index_SchemaKeys = {}
        for index_name in table.table_schema[SchemaKeys.INDEX_KEYS]:
            self.index_keys[index_name] = Index(index_name, self)

    def get_path(self):
        return self.__path

    def serialize(self):
        TableMetaData.__create_table_schema(self.__dict__, self.__path)
        self.__serialize_indices()

    @staticmethod
    def __validate__(table_schema):
        if table_schema[SchemaKeys.PRIMARY_KEY] is None or table_schema[SchemaKeys.PRIMARY_KEY] not in table_schema[
            SchemaKeys.COLUMNS]:
            raise InvalidParameterError("Primary_key not found")

    @staticmethod
    def __create_table_schema(table_schema, path):
        indices = table_schema[SchemaKeys.INDEX_KEYS]
        table_schema.update(
            {SchemaKeys.INDEX_KEYS: TableMetaData.get_indices_names(table_schema[SchemaKeys.INDEX_KEYS])})
        with open(os.path.join(path, "{}_schema.json".format(table_schema[SchemaKeys.NAME])), 'w') as file:
            json.dump(table_schema, file)
        table_schema.update({SchemaKeys.INDEX_KEYS: indices})

    def __serialize_indices(self):
        for index_name in self.index_keys:
            self.index_keys[index_name].serialize()

    @staticmethod
    def get_indices_names(index_keys):
        indices_names = []
        for index_name in index_keys:
            indices_names.append(index_name)
        return indices_names

    @staticmethod
    def get_table_schema(path, table_name):
        with open(os.path.join(path, "{}_schema.json".format(table_name)), 'r') as file:
            return json.load(file)
