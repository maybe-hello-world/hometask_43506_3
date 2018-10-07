def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr):
    quick_sort_private(arr, 0, len(arr) - 1)


def quick_sort_private(arr, first, last):
    if first < last:
        e = sort(arr, first, last)
        quick_sort_private(arr, first, e - 1)
        quick_sort_private(arr, e + 1, last)


def sort(arr, first, last):
    pivot = arr[first]
    left = first + 1
    right = last
    while True:
        while left <= right and arr[left] <= pivot:
            left = left + 1
        while arr[right] >= pivot and right >= left:
            right = right - 1
        if right < left:
            break
        else:
            swap(arr, left, right)
    swap(arr, first, right)
    return right