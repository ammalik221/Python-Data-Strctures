"""
Stacks Implementation in Python 3.0.

Although Python already provides stack functionality using .pop() and .append() function, 
but it's always nice to see how things work under the hood by implementing them on your own :)
"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_element):
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
            
    def insert_top(self, new_element):
        if self.head:
            new_element.next = self.head
            self.head = new_element
        else:
            self.head = new_element
            
    def delete_top(self):
        if self.head:
            temp = self.head
            self.head = temp.next
            return temp
        else:
            return "Stack is Empty"
          
    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
          
 
class Stack(object):
    def __init__(self, top=None):
        self.ll = LinkedList(top)
        
    def push(self, new_element):
        self.ll.insert_top(new_element)
    
    def pop(self):
        return self.ll.delete_top()
      
    def printStack(self):
        self.ll.print_list()
      
if __name__ == "__main__":
    # test cases
    a = Element(10)
    b = Element(24)
    c = Element(28)
    d = Element(30)
    
    # creating a stack with top a
    stack = Stack(a)
    
    # push two elements in the stack
    stack.push(b)
    stack.push(c)
    
    # output is - 
    # 28
    # 24 
    # 10
    stack.printStack()
    
    # output is 28 and 24 respectively
    print(stack.pop().value)
    print(stack.pop().value)

    stack.push(d)
    
    # output is -
    # 30
    # 10
    stack.printStack()
