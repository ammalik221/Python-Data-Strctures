"""
Queues Implementation in Python 3.0.

Although Python already provides queue functionality using deque class from collections module, 
but it's always nice to see how things work under the hood by implementing them on your own :)
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue(object):
    def __init__(self, head):
        self.head = head
        self.tail = head
        
    def enqueue(self, new_element):
        if self.head:
            self.tail.next = new_element
            self.tail = new_element
        else:
            self.head = self.tail = new_element
            
    def dequeue(self):
        if self.head:
            self.head = self.head.next
        else:
            return "Queue Empty"
          
    def front(self):
        if self.head:
            return self.head.value
        else:
            return "Queue Empty"
          
    def print_queue(self):
        current = self.head
        while current:
            print(current.value)
            if current == self.tail:
                break
            current = current.next
            
            
if __name__ == "__main__":
    # test cases
    a = Element(10)
    b = Element(20)
    c = Element(30)
    d = Element(40)
    # make a queue
    q = Queue(a)
    
    # add elements
    q.enqueue(b)
    q.enqueue(c)
    q.enqueue(d)
    
    # output is - 10 20 30 40
    q.print_queue()
    
    # look at the front element
    # output is 10
    print(q.front())
    
    # remove elements from queue
    # output is 30 and 40 respectively
    q.dequeue()
    q.dequeue()
    
    q.print_queue()
