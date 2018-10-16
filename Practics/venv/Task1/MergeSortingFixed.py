"""
Сортировка слиянием списка, состоящего из элементов типа int/float
"""
import numpy as np


class MergeSortingFixed:
	"""
	Главный метод - сортировка
	Используется итеративный метод (не рекурсивный)
	В цикле сначала проходятся подмассивы длиной 1 элемент - они сливаются в массивы длиной 2.
	Полученный слиянием массив записывается в соответствующую часть исходного массива
	Затем проходятся подмассивы длиной 2 и сливаются в массивы длиной 4
	И так далее
	На каждой итерации длина подмассива увеличивается в 2 раза, пока не превзойдет длину изначального массива.
	Когда это произойдет, последняя итерация заменит полностью исходный массив на отсортированный
	"""
	@staticmethod
	def sort(array: list) -> list:
		MergeSorting.__verifyInput(array)
		length = array.__len__()
		i = 1
		while i <= length:
			for j in range(0, length - i + 1, 2 * i):
				startLeftArray = j
				endLeftArray = j+i-1
				leftArray = array[startLeftArray:endLeftArray + 1]

				startRightArray = j+i
				endRightArray = min(j+2*i-1, length)
				rightArray = array[startRightArray: endRightArray + 1]

				mergedArray = MergeSorting.__mergeArrays(leftArray, rightArray)
				array[startLeftArray : endRightArray + 1] = mergedArray
			i *= 2
		return array
	"""
	Проверка входных данных - список (List) с элементами типа int и float
	"""
	@staticmethod
	def __verifyInput(input: list) -> None :
		if not isinstance(input, list):
			raise TypeError("List input expected! Get - ", str(type(input)), " type")
		for elem in input:
			elemType = type(elem)
			if elemType != int and elemType != float:
				raise TypeError("List's element is not int/float, but - ", str(elemType), " type")
	"""
	Слияние двух массивов
	В цикле сравниваются первые элементы входных списков
	Если в первом списке он меньше, то из первого списка извлекается первый элемент (удаляется) 
		и помещается в конец результирующего списка
	Также это происходит, если во втором списке не осталось элементов
	Во всех остальных случаях первый элемент извлекается из второго списка
	"""
	@staticmethod
	def __mergeArrays(array1, array2):
		length1 = len(array1)
		length2 = len(array2)
		mergedArray = np.empty(length1 + length2)

		ind1 = 0
		ind2 = 0
		for i in range(0, length1 + length2):
			if ind2 >= length2 or ind1 < length1 and array1[0] < array2[0]:
				mergedArray[i] = array1[ind1]
				ind1 += 1
			else:
				mergedArray[i] = array2[ind2]
				ind2 += 1
		return mergedArray
