# test_get_files_info.py

import unittest
from functions.get_files_info import *



class TestCalculator(unittest.TestCase):
    def test_1(self):
        print(get_files_info("calculator", "."))

    def test_2(self):    
        print(get_files_info("calculator", "pkg"))

    def test_3(self):
        print(get_files_info("calculator", "/bin"))



if __name__ == "__main__":
    unittest.main()