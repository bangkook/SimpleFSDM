from commands import CreateCommand   # The code to test
from SchemaKeys import SchemaKeys
import unittest   # The test framework
import json, os

schema = "schema.json"

parent_dir = os. getcwd()

class Test_TestCommands(unittest.TestCase):
    def test_create_database(self):
        CreateCommand(schema).execute()
        data = json.load(open(schema, "r"))
        db_path = parent_dir + "/" + data[SchemaKeys().DATABASE]
        self.assertEqual(os.path.exists(db_path), True)
        for table in data[SchemaKeys().TABLES]:
            t_path = db_path + "/" + table[SchemaKeys().NAME]
            self.assertEqual(os.path.exists(t_path), True)
    

if __name__ == '__main__':
    unittest.main()