from model.table_metadata import *

class Table:
    def __init__(self, table, database):
        self.__path = os.path.join(database.get_path(), table[SchemaKeys.NAME])
        self.__table_metadata = TableMetaData(table, self)

    def serialize(self):
        os.makedirs(self.__path, exist_ok=True)
        self.__table_metadata.serialize()

    def get_path(self):
        return self.__path
