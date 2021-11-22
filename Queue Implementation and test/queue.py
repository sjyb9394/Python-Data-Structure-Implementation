"""
Queue Implementation (FIFO)

1. isEmpty() : return true if queue is empty 
2. enQueue(a) : add element to the queue
3. deQueue() : remove element from queue and return that element
4. size() : return the size of the queue
"""

class Queue:
    length : int = 0

    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return self.size == 0

    def enQueue(self, value):
        self.queue.append(value)
        self.length += 1

    def deQueue(self):
        if self.size == 0:
            raise ValueError('Queue is Empty')
        else:
            self.length -= 1
            return self.queue.pop(0)

    @property
    def size(self):
        return self.length

    def __str__(self):
        res = ''

        for value in self.queue:
            res += str(value) + ' '

        res = res.strip()
        return res