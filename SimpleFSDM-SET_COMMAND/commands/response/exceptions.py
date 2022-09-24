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
