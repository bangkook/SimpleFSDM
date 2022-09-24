import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--command",
        type=str,
        help="command is CREATE, GET, SET or DELETE",
    )
    parser.add_argument(
        "-sc",
        "--schema_path",
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