"""
Priority Queues Implementation in Python 3.0.

This is Max Priority Queue, which arranges the elements in descending order,
i.e. the element with the highest priority is dequed first.
"""

class Element(object):
    def __init__(self, priority):
        self.priority = priority
        self.next = None
        
class PriorityQueue(object):
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.length==0

    def enqueue(self, value):
        new_element = Element(value)
        new_element.next = None

        if self.length == 0:
            self.head = self.tail = new_element
        
        elif new_element.priority > self.head.priority:
            new_element.next = self.head
            self.head = new_element

        elif new_element.priority < self.tail.priority:
            self.tail.next = new_element
            self.tail = new_element

        else:
            current = self.head
            while current.next:
                if current.priority > new_element.priority:
                    current = current.next
                break
            new_element.next = current.next
            current.next = new_element
        self.length += 1

    def dequeue(self):
        self.head = self.head.next
        self.length -= 1

    def print_queue(self):
        current = self.head
        while current:
            print(current.priority)
            current = current.next
           
if __name__ == "__main__":
    # test case
    a = PriorityQueue()

    a.enqueue(1)
    a.enqueue(2)
    a.enqueue(3)
    a.enqueue(7)
    
    a.dequeue()
    a.dequeue()
    
    # output is - 
    # 2
    # 1
    a.print_queue()
    
    # even though 1 and 2 were inserted first, 7 and 3 are dequeued first
