from abc import ABC

class SchemaKeys(ABC):
    TABLES = "Tables"
    DATABASE = "database_name"
    NAME = "name"
    COLUMNS = "columns"
    PRIMARY_KEY = "primary_key"
    INDEX_KEYS = "Index_keys"
    CONSISTENCY = "consistency"
    OVERWRITE = "overwrite"