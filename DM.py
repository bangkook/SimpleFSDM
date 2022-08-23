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

def create(schema):
    f = open(schema, "r")
    data = json.load(f)
    dir = data['database_name']
    parent_dir = "C:/Users/cyber/Desktop/SimpleFSDM/"
    path = os.path.join(parent_dir, dir)
    os.mkdir(path)
    for i in data['Tables']:
        t_path = os.path.join(path, i['name'])
        os.mkdir(t_path)

if(args.command == "CREATE"): 
   create(args.schema)

#if(args.command == "SET"):
 #   set(args.db, args.t, args.v)

#if(args.command == "GET"):
 #   get(args.db, args.t, args.pk, args.v)

#if(args.command == "DELETE"):
 #   delete(args.db, args.t, args.pk, args.v)

