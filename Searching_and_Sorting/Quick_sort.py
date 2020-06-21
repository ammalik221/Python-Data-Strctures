"""
Qiuck Sort algorithm implementation in Python 3.0

The efficiency is O(nlogn) on the average case.
"""

def quick_sort(arr, lower_index, upper_index):
    
    # already sorted
    if lower_index >= upper_index:
        return
    
    # selecting the last element as the pivot
    pivot = arr[-1]
    left = lower_index
    right = upper_index - 1
    
    while left <= right:
        # keep increasing left until a number greater than pivot is found
        while left <= right and arr[left] < pivot:
            left += 1
        
        # keep decreasing right until a number lesser than pivot is found
        while left <= right and arr[right] > pivot:
            right -= 1
            
        if left <= right:
            # swapping the two numbers
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    
    # swap left element with pivot element,
    # to bring the pivot element to its appropritate position
    arr[left], arr[upper_index] = arr[upper_index], arr[left]
    quick_sort(arr, 0, left-1)
    quick_sort(arr, left+1, upper_index)
    
if __name__ == "__main__":
    # test case
    a = [24, 2, 2, 5, 1, 76, 12, 88]
    
    # output - [24, 2, 2, 5, 1, 76, 12, 88]
    print(a)
    quicksort(a, 0, len(a)-1)
    
    # output - [1, 2, 2, 5, 12, 24, 76, 88]
    print(a)
