#!/usr/bin/python3

# Test Yeah

from sort import quicksort
from numpy import array, arange
from numpy.testing import assert_array_equal

A1 = [1, 2, 3, 4, 5, 0, 22, 33, 11, 11, 123]
A1_must = array([0, 1, 2, 3, 4, 5, 11, 11, 22, 33, 123])
A2 = array([999.1, 222.3, 333.6, 444.0, 111, 0, 2, 3, 4, 5])
A2_must = array([0, 2, 3, 4, 5, 111, 222.3, 333.6, 444.0, 999.1])
A3 = range(99, -1, -1)          # [99, 98, ..., 1, 0]
A3_must = arange(0, 100)        # [0, 1, ..., 98, 99]
A4 = array([1, 1, 1, 2, 2, 2, 0, 0, 0, -2, -3, -4, -4])
A4_must = array([-4, -4, -3, -2, 0, 0, 0, 1, 1, 1, 2, 2, 2])

assert_array_equal(quicksort(A1), A1_must)
assert_array_equal(quicksort(A2), A2_must)
assert_array_equal(quicksort(A3), A3_must)
assert_array_equal(quicksort(A4), A4_must)
print("HA! Working.")
