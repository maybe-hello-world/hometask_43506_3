import numpy as np

datalist = [1, 6, 3, 5.9, 4 ]

# Проверка на дурака
def __foolCheck(datalist=[]):
    try:
        np.array(datalist, dtype=np.float)
    except BaseException:
        print("Not-valid data!")
        return 0
    return 1

# Основная функция сортировки
def mergesort(datalist):
    if __foolCheck(datalist) == 0:
        return -1

    # Для скорости вычисления превращаем список в массив
    dataArray = np.zeros(0)
    dataArray = np.array(datalist)

    n = dataArray.shape[0]
    width = 1

    result = dataArray.copy()
    # Буферный массив
    target = np.empty_like(result)
    while width < n:
        i = 0
        while i < n:
            start = i
            mid = i + width
            end = mid + width
            i = end

            if mid > n:
                mid = n

            if end > n:
                end = n
            __merging(result, target, start, mid, end)

        # Меняем местами частично отсортированный target и result
        # чтобы продолжить сортировку
        result, target = target, result
        width *= 2

    return result

"""

Сравниваем элементы разбитого на 2 каунтерами списка
Извлекаем первый элемент из левой части (l) если он меньше
Или во второй части не осталось элементов (r == end)
Иначе извлекаем из правой части (r)

"""
def __merging(source, target, start, mid, end):
    l = start
    r = mid
    for counter in range(start, end):
        if (l < mid) and ((r == end) or (source[l] < source[r])):
            target[counter] = source[l]
            l += 1
        else:
            target[counter] = source[r]
            r += 1


print(mergesort(datalist))
