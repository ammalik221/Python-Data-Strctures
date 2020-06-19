"""
Queues Implementation in Python 3.0.

Although Python already provides queue functionality using deque class from collections module, 
but it's always nice to see how things work under the hood by implementing them on your own :)
"""

class Queue(object):
    def __init__(self, head):
        """" iniitialising a list with head """
        self.queue = [head]
        
    def enqueue(self, new_value):
        """ add a new value at the end of the queue"""
        self.queue.append(new_value)
        
    def dequeue(self):
        """ return the first element of the queue """
        return self.queue.pop(0)
      
    def front(self):
        """ look at the first element in the queue """
        return self.queue[0]
      
    def rear(self):
        """ look at the last element of the queue """
        return self.queue[-1]
    
    def print_queue(self):
        print(' '.join(map(str, self.queue)))

if __name__ == "__main__":
    # test cases
    # make a queue
    q = Queue(10)
    
    # add elements
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    
    # output is - 10 20 30 40
    q.print_queue()
    
    # look at the front and last element
    # output is 10 and 40 respectively
    print(q.front)
    print(q.rear)
    
    # remove elements from queue
    # output is 10 and 20 respectively
    print(q.dequeue)
    print(q.dequeue)
