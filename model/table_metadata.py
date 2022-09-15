from model.index import *

class TableMetaData:
    def __init__(self, table):
        self.table = table
        self.table_name = table[SchemaKeys.NAME]
        self.primary_key = table[SchemaKeys.PRIMARY_KEY]
        self.columns = table[SchemaKeys.COLUMNS]
        self.path = table[SchemaKeys.PATH]
        self.indeces = self.__create_indices()
        

    def serialize(self):
        self.__create_table_schema()
        self.__serialize_indices()

    def __create_table_schema(self):
        with open(os.path.join(self.path, "{}_schema.json".format(self.table_name)), 'w') as file:
            json.dump(self.table, file)

    def __create_indices(self):
        indeces = []
        for index in self.table[SchemaKeys.INDEX_KEYS]:
            index_object = Index(index, self.path)
            indeces.append(index_object)
        return indeces

    def __serialize_indices(self):
        indeces_path = os.path.join(self.path, SchemaKeys.INDEX_KEYS)
        os.makedirs(indeces_path, exist_ok=True)
        for index_object in self.indeces:
            index_object.serialize()
