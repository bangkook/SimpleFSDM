from ParseInput import parse_args
import os, sys
sys.path.append(os.path.join(os.getcwd(), "commands"))
from command_factory import CommandFactory

    
if __name__ == "__main__":
   args = parse_args()
   command = CommandFactory().create(args)
   message = command.execute()
   print(message)
   
