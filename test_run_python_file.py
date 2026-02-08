import unittest
from functions.run_python_file import *



class TestCalculator(unittest.TestCase):
    def test_1(self):
        print(run_python_file("calculator", "main.py"))

    def test_2(self):    
        print(run_python_file("calculator", "main.py", ["3 + 5"]))

    def test_3(self):
        print(run_python_file("calculator", "tests.py"))

    def test_4(self):
        print(run_python_file("calculator", "../main.py"))

    def test_5(self):
        print(run_python_file("calculator", "nonexistent.py"))

    def test_6(self):
        print(run_python_file("calculator", "lorem.txt"))


if __name__ == "__main__":
    unittest.main()