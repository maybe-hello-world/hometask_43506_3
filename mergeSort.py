def mergeSort(m):
    left = []
    right = []
    result = []
    if len(m) <= 1:
        return m
    else:
        middle = int(len(m) / 2)
        left = m[:middle]
        right = m[middle:]
        left = mergeSort(left)
        right = mergeSort(right)
        return merge(left, right)


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
