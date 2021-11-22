import unittest
from Singly_Linked_List import LinkedList, Node
from test_cases import get_test_cases

class Test_Linked_List(unittest.TestCase):
    def setUp(self):
        self.test_cases = get_test_cases()

    def tearDown(self):
        pass

    # test if all nodes are created and connected properly
    def test_properly_created(self):
        self.answers = [ 
            '1',
            '10->15->20->30',
            '',
            '0->150->200',
            '10->15->2->3->1->2->3->30'
        ]

        self.assertEqual(self.test_cases[0].__str__(), self.answers[0])
        self.assertEqual(self.test_cases[1].__str__(), self.answers[1])
        self.assertEqual(self.test_cases[2].__str__(), self.answers[2])
        self.assertEqual(self.test_cases[3].__str__(), self.answers[3])
        self.assertEqual(self.test_cases[4].__str__(), self.answers[4])

    # test add operation (append to the last element)
    def test_add_to_last_position(self):
        # case 1
        self.test_cases[0].add(Node(2))
        self.test_cases[0].add(Node(3))

        # case 2
        self.test_cases[1].add(Node(3))
        self.test_cases[1].add(Node(5))

        # case 3
        self.test_cases[2].add(Node(13))
        self.test_cases[2].add(Node(25))

        # case 4
        self.test_cases[3].add(Node(73))
        self.test_cases[3].add(Node(56))

        # case 4
        self.test_cases[4].add(Node(32))
        self.test_cases[4].add(Node(52))

        self.answers = [ 
            '1->2->3',
            '10->15->20->30->3->5',
            '13->25',
            '0->150->200->73->56',
            '10->15->2->3->1->2->3->30->32->52'
        ]


        self.assertEqual(self.test_cases[0].__str__(), self.answers[0])
        self.assertEqual(self.test_cases[1].__str__(), self.answers[1])
        self.assertEqual(self.test_cases[2].__str__(), self.answers[2])
        self.assertEqual(self.test_cases[3].__str__(), self.answers[3])
        self.assertEqual(self.test_cases[4].__str__(), self.answers[4])

    # test add specific position
    def test_add_to_specific_position(self):
        # case 1
        self.test_cases[0].add(Node(2),1)
        self.test_cases[0].add(Node(3),1)

        # case 2
        self.test_cases[1].add(Node(3),2)
        self.test_cases[1].add(Node(5),6)

        # case 3
        self.test_cases[2].add(Node(13),2)
        self.test_cases[2].add(Node(25),0)

        # case 4
        self.test_cases[3].add(Node(73),0)
        self.test_cases[3].add(Node(56),10)

        # case 4
        self.test_cases[4].add(Node(32),2)
        self.test_cases[4].add(Node(52),5)

        self.answers = [
            '1->3->2',
            '10->15->3->20->30->5',
            '25->13',
            '73->0->150->200->56',
            '10->15->32->2->3->52->1->2->3->30'
        ]

        self.assertEqual(self.test_cases[0].__str__(), self.answers[0])
        self.assertEqual(self.test_cases[1].__str__(), self.answers[1])
        self.assertEqual(self.test_cases[2].__str__(), self.answers[2])
        self.assertEqual(self.test_cases[3].__str__(), self.answers[3])
        self.assertEqual(self.test_cases[4].__str__(), self.answers[4])

    # test add to first position
    def test_add_to_first_position(self):
        # case 1
        self.test_cases[0].addFirst(Node(2))
        self.test_cases[0].addFirst(Node(3))

        # case 2
        self.test_cases[1].addFirst(Node(3))
        self.test_cases[1].addFirst(Node(5))

        # case 3
        self.test_cases[2].addFirst(Node(13))
        self.test_cases[2].addFirst(Node(25))

        # case 4
        self.test_cases[3].addFirst(Node(73))
        self.test_cases[3].addFirst(Node(56),)

        # case 4
        self.test_cases[4].addFirst(Node(32))
        self.test_cases[4].addFirst(Node(52))

        self.answers = [ 
            '3->2->1',
            '5->3->10->15->20->30',
            '25->13',
            '56->73->0->150->200',
            '52->32->10->15->2->3->1->2->3->30'
        ]

        self.assertEqual(self.test_cases[0].__str__(), self.answers[0])
        self.assertEqual(self.test_cases[1].__str__(), self.answers[1])
        self.assertEqual(self.test_cases[2].__str__(), self.answers[2])
        self.assertEqual(self.test_cases[3].__str__(), self.answers[3])
        self.assertEqual(self.test_cases[4].__str__(), self.answers[4])

    # test clear method
    def test_clear(self):
        for cases in self.test_cases:
            cases.clear()
        
        self.assertEqual(self.test_cases[0].__str__(), '')
        self.assertEqual(self.test_cases[1].__str__(), '')
        self.assertEqual(self.test_cases[2].__str__(), '')
        self.assertEqual(self.test_cases[3].__str__(), '')
        self.assertEqual(self.test_cases[4].__str__(), '')

    # test contain method
    def test_contains(self):
        self.assertEqual(self.test_cases[0].contains(Node(1)), True)
        self.assertEqual(self.test_cases[0].contains(Node(4)), False)
        self.assertEqual(self.test_cases[1].contains(Node(30)), True)
        self.assertEqual(self.test_cases[1].contains(Node(100)), False)
        self.assertEqual(self.test_cases[2].contains(Node(1)), False)
        self.assertEqual(self.test_cases[2].contains(Node(2)), False)
        self.assertEqual(self.test_cases[3].contains(Node(0)), True)
        self.assertEqual(self.test_cases[3].contains(Node(-3)), False)
        self.assertEqual(self.test_cases[4].contains(Node(30)), True)
        self.assertEqual(self.test_cases[4].contains(Node(200)), False)

    
    # # test get node from specific index 
    # def test_get_specific_position(self):
    #     pass
    
    # test get node from first position
    def test_getFirst(self):
        self.assertEqual(self.test_cases[0].getFirst(), '1')
        self.assertEqual(self.test_cases[1].getFirst(), '10')
        self.assertEqual(self.test_cases[2].getFirst(), '')
        self.assertEqual(self.test_cases[3].getFirst(), '0')
        self.assertEqual(self.test_cases[4].getFirst(), '10')

    # # test get node frmo last position
    # def test_getLast(self):
    #     pass

    # # test remove node from specific index
    # def test_remove_node_from_specific_position(self):
    #     pass

    # # test remove node from first position
    # def test_removeFirst(self):
    #     pass

    # # test remove node from last position
    # def test_removeLast(self):
    #     pass

    # test size of the lists
    def test_size(self):
        self.answers = [1,4,0,3,8]

        self.assertEqual(self.test_cases[0].getSize(), self.answers[0])
        self.assertEqual(self.test_cases[1].getSize(), self.answers[1])
        self.assertEqual(self.test_cases[2].getSize(), self.answers[2])
        self.assertEqual(self.test_cases[3].getSize(), self.answers[3])
        self.assertEqual(self.test_cases[4].getSize(), self.answers[4])

if __name__ == '__main__':
    unittest.main()