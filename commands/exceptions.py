from commands.status import Status

class FileNotFound(Exception):
    def __init__(self):
        self.status = Status.FileNotFound

class ErrorLoadingFile(Exception):
    def __init__(self):
        self.status = Status.ErrorLoadingFile

class DatabaseNameIsMissing(Exception):
    def __init__(self):
        self.status = Status.DatabaseNameIsMissing
