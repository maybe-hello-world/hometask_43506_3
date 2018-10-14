from sort import merge_sort
from logParser import log_parse
from numpy.testing import assert_array_equal

# test sorting function
arrays = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1],
    [66.34, 22.33, 565.8, 0],
    [-100, 67676, 55, 76.8, 22],
    [1]
]

for arr in arrays:
    try:
        assert_array_equal(merge_sort(arr), sorted(arr))
    except AssertionError:
        print("Module MergeSort not work correctly")
    else:
        print("Input list: [" + ','.join(str(x) for x in arr) + "]")
        print("Result: [" + ','.join(str(x) for x in merge_sort(arr)) + "]")


# start parse

log_parse("17", "DhcpSrvLog-Thu.log")

