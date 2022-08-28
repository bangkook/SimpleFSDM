import commands    # The code to test
import ParseInput
import unittest   # The test framework
import os

os.system("main.py DELETE -db Check-in -t Reservations -pk 111")

path = os.getcwd() + "/Check-in/Reservations/111.json"

class Test_TestCommands(unittest.TestCase):
    def test_delete(self):
        self.assertEqual(os.path.exists(path), False)


if __name__ == '__main__':
    unittest.main()