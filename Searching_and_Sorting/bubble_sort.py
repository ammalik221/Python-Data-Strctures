"""
Bubble Sort Algorithm implementation in python 3.0

I have implemented three functions in this file, each implementing bubble sort but each with
some extra technique which can drastically affect runtime, as the size of array increases.

To compare the running time of each, I have used a variable num_of_comparisions.
"""

def bubble_sort(arr):
    """ Naive approach of bubble sort """
    num_of_comparisions = 0
    for i in range(len(arr)-1):
        # number of comparisions in each iteration is len(array) - 1 
        for j in range(len(arr)-1):
            num_of_comparisions += 1
            # compare the two elements
            # if the first element is greater than the one after it, swap them
            # after the all the comparisions, the biggest element ends up at the last position of the array
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    print(num_of_comparisions)
    return arr
  

def bubble_sort_intermediate(arr):
    """ The difference here is that, I am stopping the iterations once the array is sorted. """
    num_of_comparisions = 0
    for i in range(len(arr)-1):
        count = 0
        for j in range(len(arr)-1):
            num_of_comparisions += 1
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                count += 1
        # Checks, if the array is sorted
        if count == 0:
            break
    print(num_of_comparisions)
    return arr
  

def bubble_sort_advanced(arr):
    """ The difference here is at each iteration, I am reducing the length variable,
        which stops the extra number of steps that the code was taking by comparing the elements
        that were already sorted. """
    num_of_comparisions = 0
    length = len(arr) - 1
    for i in range(len(arr)-1):
        count = 0
        for j in range(length):
            num_of_comparisions += 1
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
                count += 1
        length -= 1
        if count == 0:
            break
    print(num_of_comparisions)
    return arr
  
  
if __name__ == "__main__":
    # test case
    a = [1,24,35,45,34,4,89,77,7,87,76,7,56,53,44,6,4,43,54,54,6,8,78,23,4,7,78,77,4,42,34,23,23]
    
    # output - 
    # num_of_comparisions = 1024
    # [1, 4, 4, 4, 4, 6, 6, 7, 7, 7, 8, 23, 23, 23, 24, 34, 34, 35, 42, 43, 44, 45, 53, 54, 54, 56, 76, 77, 77, 78, 78, 87, 89]
    print(bubble_sort(a))
    
    # output - 
    # num_of_comparisions = 800
    # [1, 4, 4, 4, 4, 6, 6, 7, 7, 7, 8, 23, 23, 23, 24, 34, 34, 35, 42, 43, 44, 45, 53, 54, 54, 56, 76, 77, 77, 78, 78, 87, 89]
    a = [1,24,35,45,34,4,89,77,7,87,76,7,56,53,44,6,4,43,54,54,6,8,78,23,4,7,78,77,4,42,34,23,23]
    print(bubble_sort_intermediate(a))
    
    # output - 
    # num_of_comparisions = 500
    # [1, 4, 4, 4, 4, 6, 6, 7, 7, 7, 8, 23, 23, 23, 24, 34, 34, 35, 42, 43, 44, 45, 53, 54, 54, 56, 76, 77, 77, 78, 78, 87, 89]
    a = [1,24,35,45,34,4,89,77,7,87,76,7,56,53,44,6,4,43,54,54,6,8,78,23,4,7,78,77,4,42,34,23,23]
    print(bubble_sort_advanced(a))
