from response.status import Status

class FileNotFound(Exception):
    def __init__(self, message):
        self.status = Status.FileNotFound
        super().__init__(message)

class ErrorLoadingFile(Exception):
    def __init__(self, message):
        self.status = Status.ErrorLoadingFile
        super().__init__(message)

class MissingDataError(Exception):
    def __init__(self, message):
        self.status = Status.MissingDataError
        super().__init__(message)

class InvalidParameterError(Exception):
    def __init__(self, message):
        self.status = Status.InvalidParameterError
        super().__init__(message)

class MissingParameterError(Exception):
    def __init__(self, message):
        self.status = Status.MissingParameterError
        super().__init__(message)

class ColumnsNotExistInSchema(Exception):
    def __init__(self, message):
        self.status = Status.ColumnsNotExistInSchema
        super().__init__(message)
        
class DatabaseNotFound(Exception):
    def __init__(self, message):
        self.status = Status.DatabaseNotExist
        super().__init__(message)
        
class TableNotFound(Exception):
    def __init__(self, message):
        self.status = Status.TableNotExist
        super().__init__(message)
        
 class ValueNotFound(Exception):
    def __init__(self, message):
        self.status = Status.ValueNotExist
        super().__init__(message)
