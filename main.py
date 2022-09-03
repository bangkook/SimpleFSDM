from parse_input import parse_args
import os, sys
from commands.command_factory import CommandFactory

    
if __name__ == "__main__":
   args = parse_args()
   command = CommandFactory().create(args)
   message = command.execute()
