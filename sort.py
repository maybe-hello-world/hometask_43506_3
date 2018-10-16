import numpy as np


def mergesort(a):  # функция сортировки слиянием массива, состоящего из элементов типа int
    """

    :param a: список элементов типа int или float
    """
    # делим на половинки, половинки на половинки и т.д.,
    # потом собираем обратно, поэтапно сортируя
    if len(a) > 1:
        mid = np.floor_divide(len(a), 2)
        left = a[:mid].copy()    # левая половина
        right = a[mid:].copy()   # правая половина
        mergesort(left)
        mergesort(right)

        i = 0
        j = 0
        k = 0

        # сборка и сортировка получившихся половинок в последовательности, в порядке возрастания
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i = i+1
            else:
                a[k] = right[j]
                j = j+1
            k = k+1

        while i < len(left):
            a[k] = left[i]
            i = i+1
            k = k+1

        while j < len(right):
            a[k] = right[j]
            j = j+1
            k = k+1


def isint(value):  # функция проверки введенного числа
    """

    :param value: проверяемый введенный элемент
    :return: true или false, в зависимости от соответствия
    """
    if value.isdigit():
        return True
    else:
     try:
        float(value)
        return True
     except ValueError:
        return False


a = np.array([])
n = int(input('Введите количество элементов массива  '))
for i in range(n):
    new_element = input('Введите элемент массива  ')
    if isint(new_element):
        a = np.append(a, new_element)
    else:
        print('Введенный элемент не является числом и не будет учтен при сортировке')
print('Введенный массив: ', a)
mergesort(a)
print('Отсортированный массив: ', a)
