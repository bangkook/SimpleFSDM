from commands.create_command import CreateCommand

class CommandFactory:
    def create(self, args):
        cmd = args.command.lower()
        if (cmd == "create"):
            return CreateCommand(args.schema_path)