import unittest   # The test framework
import json
import os, sys
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(root_dir)
from model.schema_keys import SchemaKeys
from commands.create_command import CreateCommand

schema_path = os.path.join(root_dir, os.path.join("tests", "schema.json"))

class Test_TestCommands(unittest.TestCase):
    def test_wrong_input(self):
        wrong_schema = "schima.json"
        self.assertRaises(Exception, CreateCommand, wrong_schema)

    def test_no_input(self):
        self.assertRaises(Exception, CreateCommand, None)

    def test_create_database(self):
        db_name = "Check-in"
        db_path = os.path.join(root_dir, db_name)
        self.assertEqual(os.path.exists(db_path), True)
        
    def test_create_tables(self):
        db_path = os.path.join(root_dir, "Check-in")
        data = None
        with open (schema_path, "r") as schema_file:
            data = json.load(schema_file)
        for table in data[SchemaKeys.TABLES]:
            table_path = os.path.join(db_path, table[SchemaKeys.NAME])
            self.assertEqual(os.path.exists(table_path), True)

    def test_wrong_db_name(self):
        db_name = "Check"
        db_path = os.path.join(root_dir, db_name)
        table = "Flights_Details"
        table_path = os.path.join(db_path, table)
        self.assertEqual(os.path.exists(table_path), False)

    def test_create_multiple_time(self):
        db_name = "Check-in"
        db_path = os.path.join(root_dir, db_name)
        for i in range(3):
            CreateCommand(schema_path).execute()
            self.assertEqual(os.path.exists(db_path), True)

if __name__ == '__main__':
    CreateCommand(schema_path).execute()
    unittest.main()