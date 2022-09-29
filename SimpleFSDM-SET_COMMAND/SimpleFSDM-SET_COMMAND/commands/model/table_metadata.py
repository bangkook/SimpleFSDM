import index


class TableMetaData:
    def __init__(self, table_schema, table_object):
        bleMetaData.__validate__(table_schema)
        self.__table_schema = table_schema
        self.table_name = table_schema[SchemaKeys.NAME]
        self.primary_key = table_schema[SchemaKeys.PRIMARY_KEY]
        self.columns = table_schema[SchemaKeys.COLUMNS]
        self.__path = table_object.get_path()
        self.overwrite = table_schema[SchemaKeys.OVERWRITE]
        self.indeces = self.__create_indices()

    def get_path(self):
        return self.__path

    def __validate__(table_schema):
        if table_schema[SchemaKeys.PRIMARY_KEY] is None or table_schema[SchemaKeys.PRIMARY_KEY] not in table_schema[SchemaKeys.COLUMNS]:
            raise InvalidParameterError("Primary_key not found")

    def serialize(self):
        self.__serialize_table_schema()
        self.__serialize_indices()

    def __serialize_table_schema(self):
        with open(os.path.join(self.__path, self.table_name + FILE_EXTENSION), 'w') as file:
            json.dump(self.__table_schema, file)

    def __create_indices(self):
        indeces = []
        for index in self.__table_schema[SchemaKeys.INDEX_KEYS]:
            index_object = Index(index, self)
            indeces.append(index_object)
        return indeces

    def __create_table_schema__(table_schema, path):
        indices = table_schema[SchemaKeys.INDEX_KEYS]
        table_schema.update({SchemaKeys.INDEX_KEYS: TableMetaData.get_indices_names(table_schema[SchemaKeys.INDEX_KEYS])})
        with open(os.path.join(path, "{}_schema.json".format(table_schema[SchemaKeys.NAME])), 'w') as file:
            json.dump(table_schema, file)
        table_schema.update({SchemaKeys.INDEX_KEYS: indices})

    def __serialize_indices(self):
        for index_object in self.indeces:
            index_object.serialize()
