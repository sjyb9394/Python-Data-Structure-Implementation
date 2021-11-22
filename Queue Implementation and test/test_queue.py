import unittest
from queue import Queue

class Test_Qeueue(unittest.TestCase):
    def setUp(self):
        queue_1 = Queue()
        queue_2 = Queue()

        queue_1.enQueue(2)
        queue_1.enQueue(4)
        queue_1.enQueue(6)
        queue_1.enQueue(8)

        self.cases = [queue_1, queue_2]

    def tearDown(self):
        pass

    def test_isEmpty(self):
        self.assertEqual(self.cases[0].isEmpty(), False)
        self.assertEqual(self.cases[1].isEmpty(), True)

    def test_enQueue(self):
        self.assertEqual(self.cases[0].__str__(), '2 4 6 8')
        self.assertEqual(self.cases[1].__str__(), '')

        self.cases[0].enQueue(2)
        self.cases[1].enQueue(2)

        self.assertEqual(self.cases[0].__str__(), '2 4 6 8 2')
        self.assertEqual(self.cases[1].__str__(), '2')


    def test_deQueue(self):
        self.assertEqual(self.cases[0].__str__(), '2 4 6 8')
        self.assertEqual(self.cases[1].__str__(), '')

        with self.assertRaises(ValueError):
            self.cases[1].deQueue()

        self.assertEqual(self.cases[0].deQueue(), 2)
        self.assertEqual(self.cases[0].__str__(), '4 6 8')

        self.assertEqual(self.cases[0].deQueue(), 4)
        self.assertEqual(self.cases[0].__str__(), '6 8')

    def test_size(self):
        self.assertEqual(self.cases[0].size, 4)
        self.assertEqual(self.cases[1].size, 0)

        self.cases[0].deQueue()
        self.cases[1].enQueue(2)

        self.assertEqual(self.cases[0].size, 3)
        self.assertEqual(self.cases[1].size, 1)

if __name__ == '__main__':
    unittest.main()