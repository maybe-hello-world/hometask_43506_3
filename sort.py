import numpy as np


# starting method, values check
def merge_sort(input_arr):
    if isinstance(input_arr, list):
        try:
            arr = np.array(input_arr, float)
        except ValueError as e:
            return TypeError("[MergeSort]: type of list values not a float or int")
        else:
            return sort(arr).tolist()
    else:
        return TypeError("[MergeSort]: input object is not a list")


# main sorting method
def sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        middle = int(len(arr) / 2)
        left = sort(arr[:middle])
        right = sort(arr[middle:])
        return merge(left, right)


# merge two arrays for sort
def merge(left_arr, right_arr):
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
