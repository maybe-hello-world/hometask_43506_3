from sys import argv, stderr
from numpy import arange, ndarray, array, shape, copy


def quicksort(arr):
    "Quick sort maafaka"
    if isinstance(arr, range):
        arr = list(arr)
    elif isinstance(arr, list):
        arr = array(arr)
    elif not isinstance(arr, ndarray):
        raise Exception("You should provide list or numpy.ndarray")
    else:
        arr = copy(arr)

    if len(shape(arr)) != 1:
        raise Exception("You must provide a one dimensional list or numpy.ndarray")

    def swap(A, i, j):
        A[i], A[j] = A[j], A[i]

    def sort(A, left, right):
        center = int((left + right) / 2)
        elem = A[center]
        i = left - 1
        j = right + 1
        while True:
            i += 1
            while A[i] < elem:
                i += 1

            j -= 1
            while A[j] > elem:
                j -= 1

            if i >= j:
                return j

            swap(A, i, j)

    def _quicksort(A, left, right):
        if left < right:
            p = sort(A, left, right)
            _quicksort(A, left, p)
            _quicksort(A, p +1, right)

    _quicksort(arr, 0, len(arr)-1)
    return arr

if __name__ == '__main__':
    try:
        maximum = int(argv[1])
    except ValueError:
        stderr.write("You must provide an integral number")
    a = arange(maximum, 0, -1)
    print(a)
    sortedarr = quicksort(a)
    print(sortedarr)
