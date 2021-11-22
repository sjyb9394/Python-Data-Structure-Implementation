"""
    Stack Implementation (LIFO)

    Required Methods
1. empty() – Returns whether the stack is empty – Time Complexity: O(1)
2. size() – Returns the size of the stack – Time Complexity: O(1)
3. top() – Returns a reference to the topmost element of the stack – Time Complexity: O(1)
4. push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
5. pop() – Deletes the topmost element of the stack – Time Complexity: O(1)
"""

class Stack:
    length : int = 0

    def __init__(self):
        self.stack = []

    def empty(self):
        return self.length == 0

    @property
    def size(self):
        return self.length

    def top(self):
        if self.length == 0:
            raise IndexError('Stack is Empty')
        
        else:
            return self.stack[-1]

    def push(self, value):
        self.stack.append(value)
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise IndexError('Stack is Empty')
        else:
            self.stack.pop(self.length-1)
            self.length-=1 
        

    def __str__(self):
        res = ''

        for val in self.stack:
            res += str(val)+' '

        res = res.strip()
        return res
