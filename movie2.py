import random;
import pylab as plt

arr = random.choices(range(500), k = 100)

def swap(arr, i, j):
    """
    Swap the ith and jth entry in the array arr.
    Assume: i != j and i, j < len(arr)
    """
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp

fig, ax = plt.subplots(1, 1)

def insertion_sort_mov(arr):
    """
    In the ith pass of the first loop, the first i elements should be
    ordered. This actually modifies the input array.
    """
    for i in range(1, len(arr)):
        for j in range(0, i):
            # convenience variables 
            # l = curent item being looked at
            # k = item preceding the curent item
            l = i - j; k = l - 1
            if arr[k] > arr[l]: # prec > curr
                swap(arr, k, l)
                ax.stem(arr)
                plt.pause(0.01)
                plt.cla()
            else:
                # Once prev <= curr stop this loop
                break
        

insertion_sort_mov(arr)
plt.show()