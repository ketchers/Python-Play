
def swap(arr, i, j):
    """
    Swap the ith and jth entry in the array arr.
    Assume: i != j and i, j < len(arr)
    """
    tmp = arr[i]
    arr[i] = arr[j]
    arr[j] = tmp


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


def main():
    print("Hello")


if __name__ == "__main__":
    arr = []

    while True:
        try:
            item = input("Enter a value: ")
            if item != 'q':
                insert(int(item), arr)
                print(arr)
            else:
                break
        except (KeyboardInterrupt, EOFError) as e:
            break
        except ValueError as e:
            print("Only numeric values are accepted.")

    print(arr)
