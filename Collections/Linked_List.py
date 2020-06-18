if __name__ == "__main__":
    #test cases
    a = Element(10)
    b = Element(22)
    
    linked_list = LinkedList(a)
    linked_list.append(a)
    linked_list.append(b)
    
    linked_list.print_list()
