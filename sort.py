import numpy as np


def merge_sort(input_arr):
    """
    Merge sort for list - init method
    :param input_arr: list - input list for sorting
    :return: sorted list or type error
    """
    if isinstance(input_arr, list):
        try:
            arr = np.array(input_arr, float)
        except ValueError as e:
            return TypeError("[MergeSort]: type of list values not a float or int")
        else:
            return sort(arr).tolist()
    else:
        return TypeError("[MergeSort]: input object is not a list")


def sort(arr):
    """
    Main sorting algorithm (uses recursive call)
    :param arr: numpy array (type float) - current sub array for sorting
    :return: sorted numpy array
    """
    if len(arr) <= 1:
        return arr
    else:
        middle = int(len(arr) / 2)
        left = sort(arr[:middle])
        right = sort(arr[middle:])
        return merge(left, right)


def merge(left_arr, right_arr):
    """
    Merge two sorted arrays
    :param left_arr: numpy sorted array (type float)
    :param right_arr: numpy sorted array (type float)
    :return: result sorted numpy array (merging two input arrays)
    """
    result = np.array([], float)
    while len(left_arr) > 0 and len(right_arr) > 0:
        if left_arr[0] <= right_arr[0]:
            result = np.append(result, left_arr[0])
            left_arr = left_arr[1:]
        else:
            result = np.append(result, right_arr[0])
            right_arr = right_arr[1:]
    if len(left_arr) > 0:
        result = np.concatenate((result, left_arr))
    elif len(right_arr) > 0:
        result = np.concatenate((result, right_arr))
    return result
