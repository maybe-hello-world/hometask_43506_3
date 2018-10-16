import numpy as np

def merge_sort(entry):
    """
    Sort function with several type and structure checks.

    Keyword arguments:
    :param entry: List of int or float values.
    :return: Sorted list.
    :raises: ValueError
    """
    if isinstance(entry, list):
        for val in entry:
            if not (type(val) == int or type(val) == float):
                raise ValueError('Only int or float value type is allowed.')

        return _sort(entry)
    else:
        raise ValueError('Input value should be list.')


def _sort(m):
    """
    Merge sort. Slice list to smallest parts, sort and merge them part by part.

    Keyword arguments:
    :param m: Sorting list.
    :return: Sorted list.
    """
    if len(m) <= 1:
        return m
    else:
        return _merge(_sort(m[:int(len(m) / 2)]), _sort(m[int(len(m) / 2):]))


def _merge(left, right):
    """
    Merge two sorted lists.

    Keyword arguments:
    :param left: One list.
    :param right: Another list.
    :return: Merged sorted list.
    """
    left = np.flip(left)
    right = np.flip(right)
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[-1] <= right[-1]:
            result = np.append(result, left[-1])
            left = np.delete(left, -1)
        else:
            result = np.append(result, right[-1])
            right = np.delete(right, -1)

    if left.any():
        left = np.flip(left)
        result = np.append(result, left)
    if right.any():
        right = np.flip(right)
        result = np.append(result, right)

    return result
