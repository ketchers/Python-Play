def swap(arr, i, j):
    """
    Swap the ith and jth entry in the array arr.
    Assume: i != j and i, j < len(arr)
    """
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

def is_ordered(arr):
    i = 0
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def insertion_sort(arr):
    """
    Warning: This modifies the input array

    In the ith pass of the first loop, the first i elements should be
    ordered.
    """
    for i in range(1, len(arr) - 1):
        for j in range(0, i):
            # convenience variables
            # curr = current item being looked at
            # prev = item preceding the current item
            curr = i - j;
            prev = curr - 1
            if arr[prev] > arr[curr]:  # prec > curr
                swap(arr, prev, curr)
            else:
                # Once prev <= curr stop this loop
                break


def insert(item, arr=[]):
    """
    Warning: This does alter the input array.

    Inserts item into an already sorted array and returns the resulting array.
    This is intended to be use with stream insertion sort.
    """
    curr = len(arr)
    arr.append(item)
    while curr > 0:
        curr = curr - 1
        if arr[curr] > item:
            swap(arr, curr, curr + 1)
        else:
            break


def selection_sort(arr):
    """
    Warning: This modifies the input array

    In the ith pass of the first loop, the first i elements should be
    ordered.
    """
    for i in range(len(arr)):
        curr = i  # The current location of the min in arr[i:]
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[curr]:  # prec > curr
                curr = j
        swap(arr, i, curr)


def bubble_sort(arr):
    """
    Warning: This modifies the input array

    In the ith pass of the first loop, the last i elements should be
    ordered.
    """
    arr_len = len(arr)
    swaps = True  # Used for optimization
    for i in range(0, arr_len):
        if not swaps:  # As soon as there are no swaps we might as well stop
            break
        swaps = False  # If there is a swap this will get set to True
        for j in range(1, arr_len - i):
            if arr[j] < arr[j - 1]:
                swaps = True
                swap(arr, j, j - 1)
