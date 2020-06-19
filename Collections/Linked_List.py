class Element(object):
    def __init__(self, value):
        """ an element has two componenets, a value and a reference to the next node """
        self.value = value
        self.next = None

if __name__ == "__main__":
    # test cases
    # creating 3 Linked List elements
    a = Element(10)
    b = Element(22)
    c = Element(24)
    d = Element(28)
    e = Element(30)
    
    # creating a Linked List with head a
    linked_list = LinkedList(a)
    
    # appending two elements at the end of the linked list
    linked_list.append(b)
    linked_list.append(c)
    
    """ output is - 
        10 
        22 
        24 """
    linked_list.print_list()
    
    # output is 10 and 24 respectively
    print(linked_list.get_element_position(1).value)
    print(linked_list.get_element_position(2).value)

    linked_list.insert_element(d, 2)
    linked_list.insert_element(e, 5)
    
    """output is -
        10
        28
        22
        24
        30"""
    linked_list.print_list()
    
    linked_list.delete_value(10)
    """output is - 
        28
        22
        24
        30"""
    linked_list.print_list()
