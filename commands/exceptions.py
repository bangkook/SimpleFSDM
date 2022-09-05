from commands.status import Status

class FileNotFound(Exception):
    def __init__(self, message):
        self.status = Status.FileNotFound
        self.message = message

class ErrorLoadingFile(Exception):
    def __init__(self, message):
        self.status = Status.ErrorLoadingFile
        self.message = message

class MissingDataError(Exception):
    def __init__(self, message):
        self.status = Status.MissingDataError
        self.message = message

class InvalidParameterError(Exception):
    def __init__(self, message):
        self.status = Status.InvalidParameterError
        self.message = message

class MissingParameterError(Exception):
    def __init__(self, message):
        self.status = Status.MissingParameterError
        self.message = message
