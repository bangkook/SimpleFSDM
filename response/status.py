from enum import Enum

class Status(Enum):
    SUCCESS = 0
    FileNotFound = 1
    ErrorLoadingFile = 2
    MissingDataError = 3
    InvalidParameterError = 4
    MissingParameterError = 5
    ColumnsNotExistInSchema = 6
    DatabaseNotExist = 7
    TabelNotExist = 8
    ValueNotExist = 9
