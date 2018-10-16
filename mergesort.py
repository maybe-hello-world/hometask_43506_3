import numpy as np

datalist = [1, 6, 3, 5.9, 4]


def __foolCheck(datalist=[]):
    """
    Проверка на дурака.
    Проверяем каждый элемент списка.
    Если не int или float, то вызываем исключение.
    """
    for e in datalist:
        if (type(e) != int and type(e) != float):
            raise TypeError("Not-valid data!")
    TypeError.__traceback__


# Основная функция сортировки
def mergesort(datalist):

    """
        Проходим по подмассивам исходного массива начиная с длины 1, последовательно сортируем
        и увеличиваем длину в 2 раза каждый подмассив (объединяем по парам) и сливая отсортированные
        части в исходный пока не привысим длину исходного, после этого получим отсортированный массив.
    """
    __foolCheck(datalist)

    # Для скорости вычисления превращаем список в массив
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




def __merging(source, target, start, mid, end):
    """

    Сравниваем элементы разбитого на 2 каунтерами списка.
    Извлекаем первый элемент из левой части (l) если он меньше
    или во второй части не осталось элементов (r == end).
    Иначе извлекаем из правой части (r).

    """

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
