from model.index import *

class TableMetaData:
    def __init__(self, table_schema, table_object):
        self.__table_schema = table_schema
        self.table_name = table_schema[SchemaKeys.NAME]
        self.primary_key = table_schema[SchemaKeys.PRIMARY_KEY]
        self.columns = table_schema[SchemaKeys.COLUMNS]
        self.path = table_object.get_path()
        self.indeces = self.__create_indices()
        

    def serialize(self):
        self.__serialize_table_schema()
        self.__serialize_indices()

    def __serialize_table_schema(self):
        with open(os.path.join(self.path, self.table_name + FILE_EXTENSION), 'w') as file:
            json.dump(self.__table_schema, file)

    def __create_indices(self):
        indeces = []
        for index in self.__table_schema[SchemaKeys.INDEX_KEYS]:
            index_object = Index(index, self)
            indeces.append(index_object)
        return indeces

    def __serialize_indices(self):
        for index_object in self.indeces:
            index_object.serialize()
