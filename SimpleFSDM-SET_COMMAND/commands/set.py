from Icommand import *
from model.database import *
from response.exceptions import *


class SetCommand(ICommand):
    def __init__(self, database_name, table_name=None, data=None):
        self.data = SetCommand.validate(database_name, data)
        self.database_name = database_name
        self.table_name = table_name

    def execute(self):
        database = Database(database_name=self.database_name)
        database.set(self.table_name, self.data)


def validate(database_name, data):
    if database_name is None or len(database_name) == 0:
        raise InvalidParameterError("database_name parameter not entered")
    try:
        if data == "None":
            return {}
        return eval(data)
    except:
        return {}
