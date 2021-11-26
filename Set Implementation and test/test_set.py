import unittest
from test_cases import *

class Test_Set(unittest.TestCase):
    def setUp(self):
        self.l_cases = linear_set_test_cases()
        self.h_cases = hash_set_test_cases()

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()