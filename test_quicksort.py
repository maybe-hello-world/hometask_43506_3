from QuickSort import quicksort
from numpy.testing import assert_array_equal

tests = [
    [3, 5, 4, 1, 9, 7, 8, 2, 6],
    [4, 4, 4, 4, 0, -1000, -1, -1, 999, 32, 54, -342, 845],
    [1.1, 1.12, 1.123, 0.1, 0., 1.09],
    [999.1, 222.3, 333.6, 444.0, 111, 0, 2, 3, 4, 5],
    [ i for i in range(9999, -1, -2)],
    [1, 1, 1, 2, 2, 2, 0, 0, 0, -2, -3, -4, -4],
    [],
    [0]    
]

for test in tests:
    assert_array_equal(quicksort(test), sorted(test))

print("OK!")