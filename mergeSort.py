import numpy as np


# Sort function entry with several type and structure checks.
def merge_sort(entry):
    if isinstance(entry, list):
        try:
             np.array(entry, float)
        except ValueError:
            raise ValueError('List should contain only float or integer values, but NaN value found.')
        else:
            return sort(entry)
    else:
        raise ValueError('Input value should be list.')


# Main sort func. Slice array and use func for parts.
def sort(m):
    if len(m) <= 1:
        return m
    else:
        return merge(sort(m[:int(len(m) / 2)]), sort(m[int(len(m) / 2):]))


# Merge two sorted arrays.
def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result
