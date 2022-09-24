from create_command import *
from response.exceptions import *


class CommandFactory:
    def create(self, args):
        cmd = args.command.lower() if args.command is not None else None
        if cmd == "create":
            return CreateCommand(args.schema_path)
        else:
            raise InvalidParameterError("command is wrong or missing")
