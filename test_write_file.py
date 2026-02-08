import unittest
from functions.write_file import *



class TestCalculator(unittest.TestCase):
    def test_1(self):
        print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    def test_2(self):    
        print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    def test_3(self):
        print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))



if __name__ == "__main__":
    unittest.main()