from commands.create_command import CreateCommand
from commands.set_command import SetCommand
from response.exceptions import *

class CommandFactory:
    def create(self, args):
        cmd = args.command.lower() if args.command is not None else None
        if (cmd == "create"):
            return CreateCommand(args.schema_path)
        elif (cmd == "set"):
            return SetCommand(args.database, args.table, args.value)
        else:
            raise InvalidParameterError("command is wrong or missing")