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


def create_raw(db, table, pk):
    path = parent_dir + "/" + db + "/" + table + "/" + pk + ".json"
    f = open(path, "w")

    data = json.load(open("schema.json", "r"))

    for tab in data['Tables']:
        if tab['name'] == table:
            f.write(json.dumps({tab['primary_key']: pk}, indent=4))

    f.close()

# if pk not found, create new file, else update it
def set(db, table, pk, value):
    if pk == None:
        raise Exception("PrimaryKeyIsMissing")

    path = parent_dir + "/" + db + "/" + table + "/" + pk + ".json"

    if not os.path.exists(path):
        create_raw(db, table, pk)

    f = open(path, "r")
    data = json.load(f)
    f.close()
    
    if(value == None):
        return

    disallowed_characters = "{\":},"
    for character in disallowed_characters:
	    value = value.replace(character, "")
    s = value.split(" ")
     
    for i in range(0, len(s)-1, 2):
        data[s[i]] = s[i+1]

    f = open(path, "w")
    json.dump(data, f)
    f.close()


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