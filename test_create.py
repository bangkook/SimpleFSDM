import unittest   # The test framework
import json
import os, sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(root_dir)
from commands.SchemaKeys import SchemaKeys
sys.path.append(os.path.join(root_dir, "commands"))
from commands.create_command import CreateCommand

schema = os.path.join(root_dir, "schema.json")

class Test_TestCommands(unittest.TestCase):
    def test_wrong_input(self):
        wrong_schema = "schima.json"
        self.assertRaises(Exception, CreateCommand, wrong_schema)

    def test_no_input(self):
        self.assertRaises(Exception, CreateCommand, None)

    def test_create_database(self):
        db_name = "Check-in"
        db_path = root_dir + "/" + db_name
        self.assertEqual(os.path.exists(db_path), True)
        
    def test_create_tables(self):
        db_name = "Check-in"
        for table in json.load(open(schema, "r"))[SchemaKeys.TABLES]:
            table_path = root_dir + "/" + db_name + "/" + table[SchemaKeys.NAME]
            self.assertEqual(os.path.exists(table_path), True)

    def test_wrong_db_name(self):
        db_name = "Check"
        table = "Flights_Details"
        t_path = root_dir + "/" + db_name + "/" + table
        self.assertEqual(os.path.exists(t_path), False)

    def test_create_multiple_time(self):
        db_name = "Check-in"
        db_path = root_dir + "/" + db_name
        for i in range(3):
            CreateCommand(schema).execute()
            self.assertEqual(os.path.exists(db_path), True)
    

if __name__ == '__main__':
    CreateCommand(schema)
    unittest.main()
