from parse_input import parse_args
from commands.command_factory import CommandFactory
from response.command_output import CommandOutput
import json

if __name__ == "__main__":
   try:
      args = parse_args()
      command = CommandFactory().create(args)
      result = command.execute()
      command_output = CommandOutput(command=args.command, result=result)
   except Exception as e:
      command_output = CommandOutput(command=args.command, exception=e)

   print(json.dumps(command_output.__dict__))