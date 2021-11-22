from Singly_Linked_List import LinkedList as ll, Node

def get_test_cases():
    # case 1 (list of size 1)
    case1 = ll(Node(1))

    # case 2 (list of size 4)
    case2 = ll(Node(10))
    case2.add(Node(15))
    case2.add(Node(20))
    case2.add(Node(30))

    # case 3 (empty list)
    case3 = ll()

    # case 4 (list of size 3)
    case4 = ll(Node(0))
    case4.add(Node(150))
    case4.add(Node(200))

    # case 5 (list of size 8)
    case5 = ll(Node(10))
    case5.add(Node(15))
    case5.add(Node(2))
    case5.add(Node(3))
    case5.add(Node(1))
    case5.add(Node(2))
    case5.add(Node(3))
    case5.add(Node(30))

    test_cases = [case1, case2, case3, case4, case5]

    return test_cases