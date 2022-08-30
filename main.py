from ParseInput import parse_args
import os, sys
sys.path.append(os.getcwd() + "/commands")
from command_factory import CommandFactory

    
if __name__ == "__main__":
   args = parse_args()
   CommandFactory().create(args)

