from commands.Icommand import Icommand
import os, json
from commands.schema_keys import SchemaKeys
import os.path
from response.exception import *

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))

class GetCommand(Icommand):
    
    def validate(db, table, value):
        cur_dir = os.getcwd()
        found = False

        while ~found:
            file_list = os.listdir(cur_dir)
            parent_dir = os.path.dirname(cur_dir)
            if db in file_list:
                found = True                    #db found
            else:
                raise DatabaseNotExist("Database not found")
                return None
        if found:
            dict = json.loads(db)
            foundT = False
            while ~foundT:
                for i in range(3):
                  if(table == dict['name'][i]):
                    foundT = True
                
                if(~foundT):
                    raise TableNotExist("Table not found")
                    return None
        
        #db and table found
        foundV = False
        if value in dict.values():
            foundV = True
        else:
            raise ValueNotExist("Value not found")
            return None
        print("Found")
        


            
