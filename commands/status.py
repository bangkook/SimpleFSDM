from enum import Enum
from sre_constants import SUCCESS

class Status(Enum):
    SUCCESS = 0
    FileNotFound = 1
    ErrorLoadingJsonFile = 2
    DatabaseNameIsMissing = 3
    