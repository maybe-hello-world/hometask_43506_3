import numpy as np


#
def merge_sort(entry):
    """
    Sort function with several type and structure checks.

    Keyword arguments:
    :param entry: List of int or float values.
    :return: Sorted list.
    :raises: ValueError
    """
    if isinstance(entry, list):
        try:
             np.array(entry, float)
        except ValueError:
            raise ValueError('List should contain only float or integer values, but NaN value found.')
        else:
            for val in entry:
                if val is None:
                    raise ValueError('List should not contain any None values. Only int or float is allowed.')

            return sort(entry)
    else:
        raise ValueError('Input value should be list.')


def sort(m):
    """
    Merge sort. Slice list to smallest parts, sort and merge them part by part.

    Keyword arguments:
    :param m: Sorting list.
    :return: Sorted list.
    """
    if len(m) <= 1:
        return m
    else:
        return merge(sort(m[:int(len(m) / 2)]), sort(m[int(len(m) / 2):]))


def merge(left, right):
    """
    Merge two sorted lists.

    Keyword arguments:
    :param left: One list.
    :param right: Another list.
    :return: Merged sorted list.
    """
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result
