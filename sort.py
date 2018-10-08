def swap(arr, i, j):
    """Меняет местами элементы i и j входного массива arr."""
    arr[i], arr[j] = arr[j], arr[i]


def quick_sort(arr: list):
    """Сортирует входной массив arr методом быстрой сортировки."""
    if not isinstance(arr, list):
        raise TypeError("Input parameter 'arr' (", str(type(arr)), " type) is not a list!")
    length = len(arr)
    if length > 1:
        quick_sort_private(arr, 0, length - 1)


def quick_sort_private(arr, first, last):
    """Приватная функция. Используйте функцию quick_sort вместо неё."""
    if first < last:
        e = sort(arr, first, last)
        quick_sort_private(arr, first, e - 1)
        quick_sort_private(arr, e + 1, last)


def sort(arr, first, last):
    """Приватная функция сортировки, используемая в алгоритме. Не для внешнего использования! Для сортировки используйте
    функцию quick_sort"""
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