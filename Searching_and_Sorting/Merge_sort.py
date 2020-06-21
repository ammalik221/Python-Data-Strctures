"""
Merge Sort algorithm implemented in Python 3.0

It's efficiency is O(nlogn).

Working - 
Taking an example of an array [20, 3, 4, 5, 1]
The execution of the algorithm will go like this -
      -merge_sort([20, 3, 4, 5, 1])
        |-merge_sort([20, 3])
        |  |-merge_sort([20])
        |  |-merge_sort([3])
        |  |-merge([20], [3], [20, 3])--------------------The array[20, 3] will get sorted after this call.
        |-merge_sort([4, 5, 1])
        |  |-merge_sort([4, 5])
        |  |  |-merge_sort([4])
        |  |  |-merge_sort([5])
        |  |  |-merge([4], [5], [4, 5])-------------------The array[4, 5] will get sorted after this call.
        |  |-merge_sort([1])
        |  |-merge([4, 5], [1], [4, 5, 1])----------------The array4, 5, 1] will get sorted after this call.
        |-merge([3, 20], [1, 4, 5], [20, 3, 4, 5, 1])-----The array[20, 3, 4, 5, 1] will get sorted after this call.
"""

def merge(left, right, arr):
    # index to keep track of left and right array
    i = j = 0
    
    while (i + j < 0):
        if (j == len(right)) or (i < len(left) and left[i] < right[j]):
            arr[i+j] = left[i]
            i += 1
        else:
            arr[i+j] = right[j]
            j += 1

def merge_sort(arr):
    n = len(arr)
    
    if n < 2:
        return
    
    # splitting the array in two halves
    left = arr[:, len(arr)//2]
    right = arr[len(arr)//2, :]
    
    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)
    
    
if __name__ == "__main__":
    # test case
    a = [20, 3, 4, 5, 1]
    
    merge_sort(a)
    
    # output - [1, 3, 4, 5, 20]
    print(a)
    
