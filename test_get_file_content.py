# test_get_files_content.py

import unittest
from functions.get_file_content import *

class TestCalculator(unittest.TestCase):
    def test_1(self):
        print(get_file_content("calculator", "lorem.txt"))

    def test_2(self):
        print(get_file_content("calculator", "main.py"))

    def test_3(self):
        print(get_file_content("calculator", "pkg/calculator.py"))

    def test_4(self):
        print(get_file_content("calculator", "/bin/cat"))

    def test_5(self):
        print(get_file_content("calculator", "pkg/does_not_exist.py"))


if __name__ == "__main__":
    unittest.main()