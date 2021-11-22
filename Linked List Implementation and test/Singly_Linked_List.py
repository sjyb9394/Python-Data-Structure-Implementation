"""
Singly Linked List

Methods
1. add(Node) => used to append the specified element to the end of a list
2. add(int index, Node) => used to insert the specified element at the specified position index in a list
3. addFirst(Node) => used to insert the given element at the beginning of a list
4. clear() => used to remove all the elements from a list
5. contains(Node) => used to return true if a list contains a specified element
6. get(int index) => used to return the element at the specified position in a list
7. getFirst() => used to return the first element in a list
8. getLast() => used to return the last element in a list
9. remove(int index) => used to remove the element at the specified position in a list
10. removeFirst() => used to removes and return the first element from a list
11. removeLast() => used to remove and return the last element from a list
12. getSize() => used to return the number of elements in a list
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    size:int = 0

    def __init__(self, Node = None):
        self.head = Node
        if Node: self.size += 1

    # if index > size of list, just append at last
    def add(self, Node, index = None):
        if not self.head:
            self.head = Node
            return
        elif index == 0:
            self.addFirst(Node)
            return

        if not index or index >= self.getSize():
            cur = self.head

            while cur.next:
                cur = cur.next

            cur.next = Node
            self.size += 1
        else:
            current_idx = 0
            current_node = self.head

            while current_idx < index-1:
                current_node = current_node.next
                current_idx += 1
            
            nextNode = current_node.next
            current_node.next = Node
            Node.next = nextNode


    def addFirst(self, Node):
        temp = self.head
        self.head = Node
        Node.next = temp

    def clear(self):
        self.head = None

    def contains(self, Node):
        current_Node = self.head

        while current_Node:
            if current_Node.value == Node.value:
                return True
            current_Node = current_Node.next

        return False

    # when duplicates exist, just return the first one
    def get(self, index):
        pass

    def getFirst(self):
        if not self.head: return ''
        return self.head.__str__()

    def getLast(self):
        pass

    def remove(self, index):
        pass

    def removeFirst(self):
        pass

    def removeLast(self):
        pass

    def getSize(self):
        return self.size

    def __str__(self):
        res = ''
        current_node = self.head

        while current_node:
            res += str(current_node.value)+' '
            current_node = current_node.next

        res = res.strip()
        res = "->".join(res.split(' '))
        return res