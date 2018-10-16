from sys import stderr
from numpy import arange, ndarray, array, shape, copy

def quicksort(arr):
    """
    Быстрая сортировка с помощью алгоритма Хоара.
    Принимает range, list, numpy.ndarray.
    """
    def swap(A, m, n):
        A[m], A[n] = A[n], A[m]

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

    def arrange(A, leftIndex, rightIndex):
        """
        Переставляет элементы в массиве между
        двумя индексами так, что все элементы левой
        половины меньше элементов правой
        """
        center = int((leftIndex + rightIndex) / 2)
        x = A[center]
        i = leftIndex - 1
        j = rightIndex + 1
        while True:
            i +=1
            while A[i] < x:
                i +=1

            j -= 1
            while A[j] > x:
                j -= 1

            if i >= j:
                return j

            swap(A, i, j)

    def sort(A, leftIndex, rightIndex):
        "Сортировка Хоара"
        if leftIndex < rightIndex:
            p = arrange(A, leftIndex, rightIndex)
            sort(A, leftIndex, p)
            sort(A, p+1, rightIndex)

    sort(arr, 0, len(arr)-1)
    return arr

maximum = 10000
a = arange(maximum, 0, -1)
print(a)
sortedArray = quicksort(a)
print(sortedArray)



print("privet brat")
