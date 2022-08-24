import argparse
import json
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
        "--primary-key",
        type=str,
        help="Primary key is a unique key",
    )
    return parser.parse_args()

args = parse_args()

parent_dir = "C:/Users/cyber/Desktop/SimpleFSDM/"

def create(schema):
    f = open(schema, "r")
    data = json.load(f)
    dir = data['database_name']
    path = os.path.join(parent_dir, dir)
    os.mkdir(path)
    for i in data['Tables']:
        t_path = os.path.join(path, i['name'])
        os.mkdir(t_path)

def set(db, table, value):
    disallowed_characters = "{\":},"
    for character in disallowed_characters:
	    value = value.replace(character, "")
    s = value.split(" ")
    
    dictionary = {}
    for i in range(0, len(s)-1, 2):
        dictionary[s[i]] = s[i+1]
    id = s[1]
    data = json.dumps(dictionary, indent=4)
    with open(db + "/" + table + "/" + id + ".json", "w") as outfile:
        outfile.write(data)
    print(value, s)


if(args.command == "CREATE"): 
   create(args.schema)

if(args.command == "SET"):
   set(args.database, args.table, args.value)

#if(args.command == "GET"):
 #   get(args.db, args.t, args.pk, args.v)

#if(args.command == "DELETE"):
 #   delete(args.db, args.t, args.pk, args.v)

