import timeit
import numpy as np

from MergeSorting import MergeSorting
from MergeSortingFixed import MergeSortingFixed

N = 20


def _checker(arr):
	return np.all(np.diff(arr) >= 0)


arr = [i for i in range(10**5, 0, -1)]

print("MAKPETR Sorted: {}".format(_checker(MergeSorting.sort(arr.copy()))))
print("MAKPETR Fixed Sorted: {}".format(_checker(MergeSortingFixed.sort(arr.copy()))))

print("Timeit MAKPETR: " + str(timeit.timeit(lambda: MergeSorting.sort(arr.copy()), number=N) / N))
print("Timeit MAKPETR Fixed: " + str(timeit.timeit(lambda: MergeSortingFixed.sort(arr.copy()), number=N) / N))
