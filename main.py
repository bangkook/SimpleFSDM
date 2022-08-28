from ParseInput import parse_args
from commands import CommandFactory
import os

    
if __name__ == "__main__":
   args = parse_args()
   CommandFactory().create(args)

