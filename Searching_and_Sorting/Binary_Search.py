"""
Binary Search Implementation in Python 3.0

This file has binary search implemented using loops.
Check out Binary_search_recursion.py for the implementation using recursion.
"""


def binary_search(array, value):
    """ searching for the element starting from the middle """
    lower = 0
    higher = len(array)
    while(higher >= lower):
        # keep calculating middle value again and again according to updated lower and higher value
        mid = (lower + higher)//2
        if array[mid] == value:
            # value found
            return mid
        elif array[mid] > value:
            # search the left side of array
            higher = mid - 1
        else:
            # search the right side of array
            lower = mid + 1
    return -1
  
if __name__ == "__main__":
    # test case
    a = [4, 5, 6, 10, 13, 14, 16, 18, 19, 25, 45, 67]
    value_1 = 10
    value_2 = 23
    value_3 = 67
    
    # outputs will be 3, -1 and 11 respectively
    print(binary_search(a, value_1))
    print(binary_search(a, value_2))
    print(binary_search(a, value_3))
    
