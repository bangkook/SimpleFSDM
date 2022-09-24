from table_metadata import *
from row import *
from response.exceptions import *


class Table:
    def __init__(self, database, table_name, table_schema=None):
        self.__path = os.path.join(database.get_path(), table_name)
        if table_schema is None:
            table_schema = TableMetaData.get_table_schema(self.__path, table_name)
        self.table_schema = table_schema
        self.__table_metadata__ = TableMetaData(self)

    def serialize(self):
        os.makedirs(self.__path, exist_ok=True)
        self.__table_metadata__.serialize()

    def get_name(self):
        return self.__table_metadata__.name

    def get_path(self):
        return self.__path

    def __get_data_path__(self):
        return os.path.join(self.__path, "data")

    def get_primary_key(self):
        return self.__table_metadata.primary_key

    def __get_primary_key_from_path(self, path):
        return str(path).replace(self.__path, '').replace(".json", '').replace("data", '')

    def overwrite(self):
        return self.__table_metadata.overwrite

    def get_indices(self):
        return self.__table_metadata.index_keys

    def set(self, data):
        primary_key = data.get(self.get_primary_key())
        existing_row = None
        if primary_key is not None:
            existing_row = self.get_by_primary_key(primary_key)
        try:
            row = Row(self, data)
            row.serialize()
            existing_row.delete_index() if existing_row else None
        except Exception:
            raise OverwriteError("data exists")

    def get_by_primary_key(self, primary_key):
        path = self.__get_primary_key_path(primary_key)
        if path is None or not os.path.isfile(path):
            return None
        with open(path, 'r') as file:
            data = json.load(file)
        return Row(self, data)

    def __get_primary_key_path(self, primary_key):
        path = os.path.join(self.__get_data_path(), "{}.json".format(primary_key))
        if os.path.isfile(path):
            return path
        return None
