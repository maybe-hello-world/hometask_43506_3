from numpy import array, ndarray

def quicksort(obj: list) -> list:
    """
    Сортировка массива методом быстрой сортировки
    """
    def sort(arr: ndarray, l, r) -> ndarray:
        if l < r:
            pivot = arr[(l + r) // 2]
            i = l
            j = r
            while i <= j:
                while arr[i] < pivot:
                    i += 1
                while arr[j] > pivot:
                    j -= 1
                if i >= j:
                    break
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1        
            sort(arr, l, j)
            sort(arr, j+1, r)        
        return arr

    # Выполняем проверку на корректность входных данных
    if not isinstance(obj, list):
        raise TypeError(str(type(obj)) + " is not list")

    # Сортируем массив
    res = sort(array(obj), 0, len(obj) - 1)
    return res.tolist()
