from parse_input import parse_args
from commands.command_factory import CommandFactory
from commands.command_output import CommandOutput
from commands.status import Status

if __name__ == "__main__":
   args = parse_args()
   command = CommandFactory().create(args)
   status = command.execute()
   command_output = None
   if status == Status.SUCCESS:
      command_output = CommandOutput.success(args.command.lower())
   else:
      command_output = CommandOutput.failure(status)
   print(command_output)