import commands    # The code to test
import ParseInput
import unittest   # The test framework
import os

os.system("main.py GET -db Check-in -t Reservations -pk 1")
#os.system("main.py DELETE -db Check-in -t Reservations -pk 111")

db = "Check-in"
t = "Reservations"
pk = "111"
value = "{id: 1, name: \"Mohamed\"}"
db_path = os. getcwd() + "/" + db
file_path = db_path + "/" + t + "/" + pk + ".json"
class Test_TestCommands(unittest.TestCase):
    def test_create(self):
        self.assertEqual(os.path.exists(db_path), True)
    def test_set(self):
        self.assertEqual(os.path.exists(file_path), True)

if __name__ == '__main__':
    unittest.main()