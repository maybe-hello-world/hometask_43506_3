import numpy as np

"""
На вход подается 1 аргумент. Функция проверяет, список ли это. Если нет - бросается исключение
Далее идет проверка всех элементов на соотвествие численному типу, при нахождение другого типа бросается исключение
Если встречается хотя бы один float - возвращаемый список будет из float'ов, иначе из int'ов
Исходный список преобразуется в numpy.array и сортируется функцией __merge__
Полученный результат сортировки приводится к определенному ранее численному типу, преобразуется в list и возвращается
"""


def sort(data: list) -> list:
    """
    :param data:
    :type data:
    :return:
    """
    assert isinstance(data,list), "Not a list!"
    list_type=int
    for elem in data:
        assert not isinstance(elem,int) or not isinstance(elem,float),"At least one element in list is not a number!"
        if isinstance(elem,float):
            list_type=float
    arr = np.array(data, float)
    return np.array(_merge(arr), list_type).tolist()


"""
Функция получает на вход numpy.array
Если он пустой или состоит из 1 элемента, то сразу же возвращается, т.к. является отсортированным
Массив разбивается на два подмассива left/right, которые рекурсивно сортируются
Для отсортированных массивов создаются указатели, указывающие на первые(наименьшие) элементы этих массивов
Итеративно начинает создаваться новый numpy.array - акцептор, в который добавляется наименьший из 
элементов массивов, на который указывает указатель. После каждой операции указатель массива-донора сдвигается вправо
Когда один из указателей пройдет весь массив, в массив-акцептор добавляется вся оставшаяся часть другого массива-донора
Полученный массив отсортирован
"""


def _merge(arr: np.array) -> np.array:
    if len(arr)<=1:
        return arr
    else:
        middle = round(len(arr)/2)
        left = _merge(arr[0:middle])
        right = _merge(arr[middle:])
        left_i = right_i = 0
        summary = np.array([],float)
        while left_i < middle and right_i < len(right):
            if left[left_i] < right[right_i]:
                summary = np.append(summary,left[left_i])
                left_i+=1
            else:
                summary = np.append(summary,right[right_i])
                right_i+=1
        if left_i>=middle:
            summary = np.append(summary, right[right_i:])
        else:
            summary = np.append(summary, left[left_i:])
        return summary