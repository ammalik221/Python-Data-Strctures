"""
Depth First Search implementation on a binary Tree in Python 3.0

Working - 
recursion calls associated with printing the tree are in the following order - 
        - print(1, "")
          |- traversal = "1"
          |- print(2, "1")
          |  |- traversal = "12"
          |  |- print(4, "12")
          |  |  |- traversal = "124"
          |  |  |- print(None, "124")
          |  |  |- print(None, "124")
          |  |- print(5, "124")
          |  |  |- traversal = "1245"
          |  |  |- print(None, "1245")
          |  |  |- print(None, "1245")
          |- print(3, "1245")
          |  |- traversal = "12453"
          |  |- print(None, "12453")
          |  |- print(None, "12453")
          

recursion calls associated in searching are in the following order - 
        - search(1, 5)                ----------------- True
          |- search(2,5)              ----------------- True
          |  |- search(4, 5)          ----------------- False
          |  |  |- search(None, 5)    ----------------- False
          |  |  |- search(None, 5)    ----------------- False
          |  |- search(5,5)           ----------------- True
          |- search(3, 5)             ----------------- False
          |  |-search(None, 5)        ----------------- False
          |  |- search(None, 5)       ----------------- False
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
        
    def print_binary_tree(self):
        return self.preorder_print(self.root, "")
      
    def preorder_print(self, start, traversal):
        if start:
            traversal += str(start.value)
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
      
    def search_element(self, element):
        return self.preorder_search(self.root, element)
      
    def preorder_search(self, start, element):
        if start:
            if start.value == element:
                return True
            else:
                return self.preorder_search(start.left, element) or self.preorder_search(start.right, element)
        else:
            return False
          
if __name__ == "__main__":
    # test case
    # add nodes to the tree
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    
    #               1
    #             /   \
    #            2     3
    #           / \
    #          4   5

    # output is True
    print(tree.search(4))
    # output is False
    print(tree.search(6))

    # output is 12453
    print(tree.print_binary_tree())
          
