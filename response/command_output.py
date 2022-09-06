from response.status import Status
from response.exceptions import *

class CommandOutput:
    def __init__(self, command, result=None, exception=None):
        self.result = result
        self.status = Status.SUCCESS.value if exception is None else exception.status.name
        self.message = command + " is executed successfully." if exception is None else str(exception)
    