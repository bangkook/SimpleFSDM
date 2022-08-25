import json, ast
import os

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
    path = parent_dir + "/" + db + "/" + table + "/" + pk + ".json"

    if not os.path.exists(path):
        return "Primary key does not exist"

    if pk == None:
        return "Primary Key is missing"

    f = open(path,  "r")
    data = json.load(f)
    return(ast.literal_eval(json.dumps(data)))  

def delete(db, table, pk, value):
    path = parent_dir + "/" + db + "/" + table + "/" + pk + ".json"

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