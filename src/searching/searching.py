def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    first = 0
    last = len(arr) - 1
    middle = (first+last) // 2
    while first <= last:
        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            first = middle + 1        
        else:
            last = middle -1
    # Your code here
    return -1  # not found
