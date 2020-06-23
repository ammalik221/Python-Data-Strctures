"""
Binary Search Tree implementation in Python 3.0.

Main difference between a normal tree and a binary search tree is the ordering of elements.
In binary search tree, the parent node is greater than the left child and smaller than the right child.

By using this condition, the runtime of operations like inserting decreases from O(n) to O(logn)
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BST(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def search(self, val):
        return self.preorder_search(self.root, val)
      
    def preorder_search(self, start, val):
        if start:
            if start.value == val:
                return True
            else:
                if start.value > val:
                    return preorder_search(start.left, val)
                else:
                    return preorder_search(start.right, val)
        return False
    
    def insert(self, new_element):
        self.preorder_insert(self.root, new_element)
            
    def preorder_insert(self, start, new_element):
        if start.value < new_element:
            if start.right:
                self.preorder_insert(start.right, new_element)
            else:
                start.right = Node(new_element)
        else:
            if start.left:
                self.preorder_insert(start.left, new_element)
            else:
                start.left = Node(new_element)
                
    def print_tree(self):
        return self.preorder_print(self.root, "")
    
    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value)
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
      
if __name__ == "__main__":
    # test case
    tree = BST(4)
    
    #         4
    #       /   \
    #      2     5
    #     / \
    #    1   3
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)
    
    # output is True
    print(tree.search(4))
    
    # output is False
    print(tree.search(6))
    
    # output is 42135
    print(tree.print_tree())
