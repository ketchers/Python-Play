import random
import time

import sorts


def timer(f, *args, **kwargs):
    start = time.perf_counter_ns()
    f(*args, **kwargs)
    return time.perf_counter_ns() - start


arr_test = random.choices(range(500), k=10)
#arr = arr_test[:]
#print(timer(sorts.selection_sort, arr))
#arr = arr_test[:]
#print(timer(sorts.insertion_sort, arr))
arr = arr_test[:]
print(timer(sorts.bubble_sort, arr))

