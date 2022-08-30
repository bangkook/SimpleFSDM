from create_command import CreateCommand

class CommandFactory:
    def create(self, args):
        cmd = args.command.lower()
        if (cmd == "create"):
            CreateCommand(args.schema).execute()