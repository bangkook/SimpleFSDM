from enum import Enum

class Status(Enum):
    SUCCESS = 0
    FileNotFound = 1
    ErrorLoadingFile = 2
    DatabaseNameIsMissing = 3
    