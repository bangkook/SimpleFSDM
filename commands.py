import json, ast
import os

parent_dir = os. getcwd() 

def create(schema):
    f = open(schema, "r")
    data = json.load(f)
    dir = data['database_name']
    path = os.path.join(parent_dir, dir)

    if(os.path.exists(path)):
        raise Exception("DatabaseExistsWithSameName")

    os.mkdir(path)
    for i in data['Tables']:
        t_path = os.path.join(path, i['name'])
        os.mkdir(t_path)


def set(db, table, pk, value):
    if pk == None:
        raise Exception("PrimaryKeyIsMissing")

    disallowed_characters = "{\":},"
    for character in disallowed_characters:
	    value = value.replace(character, "")
    s = value.split(" ")
    
    path = parent_dir + "/" + db + "/" + table + "/" + pk + ".json"

    if os.path.exists(path):
        raise Exception("ItemExistsWithSamePK")

    dictionary = {}
    for i in range(0, len(s)-1, 2):
        dictionary[s[i]] = s[i+1]

    data = json.dumps(dictionary, indent=4)
    with open(path, "w") as outfile:
        outfile.write(data)


def get(db, table, pk, value):
    path = parent_dir + "/" + db + "/" + table + "/" + pk + ".json"

    if not os.path.exists(path):
        raise Exception("PrimaryKeyNotFound")

    if pk == None:
        raise Exception("PrimaryKeyIsMissing")

    f = open(path,  "r")
    data = json.load(f)
    print(ast.literal_eval(json.dumps(data)))  


def delete(db, table, pk, value):
    path = parent_dir + "/" + db + "/" + table + "/" + pk + ".json"

    if not os.path.exists(path):
        raise Exception("PrimaryKeyNotFound")

    os.remove(path)  