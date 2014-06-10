import unittest
from math import sqrt

class TestUM(unittest.TestCase):

    def setUp(self):
        pass

    def test_numbers_3_4(self):
        self.assertEqual( sqrt(16), 4)

    def test_strings_a_3(self):
        self.assertEqual( sqrt(25), 5)

if __name__ == '__main__':
    unittest.main()