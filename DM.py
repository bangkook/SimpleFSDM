import argparse
import json, ast
import os

def parse_args():
    parser = argparse.ArgumentParser(description="Auto Sizer agent")
    parser.add_argument(
        'command',
        type=str,
        help="command is CREATE, GET, SET or DELETE",
    )
    parser.add_argument(
        "-sc",
        "--schema",
        type=str,
        help="This is the database schema, it is a json object.",
    )
    parser.add_argument(
        "-db",
        "--database",
        type=str,
        help="Database name",
    )
    parser.add_argument(
        "-t",
        "--table",
        type=str,
        help="Table name",
    )
    parser.add_argument(
        "-v",
        "--value",
        type=str,
        help="Value to be set, a JSON object. example: {id: 1, name : 'Mohamed'}",
    )
    parser.add_argument(
        "-pk",
        "--primary_key",
        type=str,
        help="Primary key is a unique key",
    )
    return parser.parse_args()

args = parse_args()

parent_dir = os. getcwd() 

def create(schema):
    f = open(schema, "r")
    data = json.load(f)
    dir = data['database_name']
    path = os.path.join(parent_dir, dir)
    os.mkdir(path)
    for i in data['Tables']:
        t_path = os.path.join(path, i['name'])
        os.mkdir(t_path)

def set(db, table, pk, value):
    if pk == None:
        return "Primary Key is Missing"

    disallowed_characters = "{\":},"
    for character in disallowed_characters:
	    value = value.replace(character, "")
    s = value.split(" ")
    
    path = parent_dir + "/" + db + "/" + table + "/" + pk + ".json"

    if os.path.exists(path):
        return "Item Exists With Same PK"

    dictionary = {}
    for i in range(0, len(s)-1, 2):
        dictionary[s[i]] = s[i+1]

    data = json.dumps(dictionary, indent=4)
    with open(path, "w") as outfile:
        outfile.write(data)
    return "Successfully set"

def get(db, table, pk, value):
    f = open(db + "/" + table + "/" + pk + ".json", "r")
    data = json.load(f)
    data = ast.literal_eval(json.dumps(data))
    
    if value == None:
        print(data)
    else:
        s = value.split(" ")
        dic = {}
        for i in s:
            dic[i] = data[i]
        print(dic)

def delete(db, table, pk, value):
    path = parent_dir + db + "/" + table + "/" + pk + ".json"

    if not os.path.exists(path):
        print("primary key does not exist")

    elif value == None:
        os.remove(path)
    
    else:
        s = value.split(" ")

        with open(db + "/" + table + "/" + pk + ".json", "r") as f:
            data = json.load(f)
        for w in s:
            del data[w]

        with open(db + "/" + table + "/" + pk + ".json", "w") as f:
            json.dump(data, f, indent=4)
    
if(args.command == "CREATE"): 
   create(args.schema)

if(args.command == "SET"):
   print(set(args.database, args.table, args.primary_key, args.value))

if(args.command == "GET"):
   get(args.database, args.table, args.primary_key, args.value)

if(args.command == "DELETE"):
   delete(args.database, args.table, args.primary_key, args.value)

