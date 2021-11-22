import unittest
from stack import Stack as stack

class Test_Stack(unittest.TestCase):
    def setUp(self):
        case1 = stack()
        case1.push(1)
        case1.push(2)
        case1.push(3)
        case1.push(4)
        case1.push(5)
        case2 = stack()

        self.cases = [case1, case2]

    def tearDown(self):
        pass

    def test_empty(self):
        self.assertEqual(self.cases[0].empty(), False)
        self.assertEqual(self.cases[1].empty(), True)

        self.cases[1].push(1)

        self.assertEqual(self.cases[1].empty(), False)

    def test_size(self):
        self.assertEqual(self.cases[0].size, 5)
        self.assertEqual(self.cases[1].size, 0)

        self.cases[0].push(1)
        self.cases[1].push(1)

        self.assertEqual(self.cases[0].size, 6)
        self.assertEqual(self.cases[1].size, 1)

    def test_top(self):
        self.assertEqual(self.cases[0].top(), 5)
        
        with self.assertRaises(IndexError):
            self.cases[1].top()
        
        self.cases[0].push(2)
        self.cases[1].push(1)

        self.assertEqual(self.cases[0].top(), 2)
        self.assertEqual(self.cases[1].top(), 1)

    def test_push(self):
        self.assertEqual(self.cases[0].__str__(), '1 2 3 4 5')
        self.assertEqual(self.cases[1].__str__(), '')

        self.cases[0].push(2)
        self.cases[1].push(3)

        self.assertEqual(self.cases[0].__str__(),'1 2 3 4 5 2')
        self.assertEqual(self.cases[1].__str__(), '3')

    def test_pop(self):
        self.cases[0].pop()

        self.assertEqual(self.cases[0].__str__(), '1 2 3 4')
        
        with self.assertRaises(IndexError):
            self.cases[1].pop()

        self.cases[0].pop()
        self.assertEqual(self.cases[0].__str__(), '1 2 3')


if __name__ == '__main__':
    unittest.main()