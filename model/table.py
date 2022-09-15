from model.table_metadata import *

class Table:
    def __init__(self, table):
        self.table_metadata = TableMetaData(table)

    def serialize(self):
        self.__create_table()
        self.table_metadata.serialize()

    def __create_table(self):
        os.makedirs(self.table_metadata.path, exist_ok=True)
