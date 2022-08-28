from commands import CreateCommand   # The code to test
from SchemaKeys import SchemaKeys
import unittest   # The test framework
import json, os

schema = "schema.json"
db_name = "Check-in"
table1 = "Reservations"
table2 = "Flights_Details"
table3 = "Flights_seats"
table4 = "Planes_Details"

parent_dir = os. getcwd()

class Test_TestCommands(unittest.TestCase):
    def test_create_database(self):
        db_path = parent_dir + "/" + db_name
        self.assertEqual(os.path.exists(db_path), True)
        
    def test_create_table1(self):
        t1_path = parent_dir + "/" + db_name + "/" + table1
        self.assertEqual(os.path.exists(t1_path), True)

    def test_create_table2(self):
        t2_path = parent_dir + "/" + db_name + "/" + table2
        self.assertEqual(os.path.exists(t2_path), True)

    def test_create_table3(self):
        t3_path = parent_dir + "/" + db_name + "/" + table3
        self.assertEqual(os.path.exists(t3_path), True)

    def test_create_table4(self):
        t4_path = parent_dir + "/" + db_name + "/" + table4
        self.assertEqual(os.path.exists(t4_path), True)
    

if __name__ == '__main__':
    CreateCommand(schema).execute()
    unittest.main()