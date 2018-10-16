import numpy


class Quicksorter:

    # To check if list contains only floats and ints and can be processed.
    @staticmethod
    def __check_for_numeric_list(list_to_check):
        assert  isinstance(list_to_check, list), 'The list is not a list.'
        for element in list_to_check:
            assert isinstance(element, (int, float)), 'List is not numeric.'
        return True

    # Not sure if it is really legit, but there is quicksort in numpy already, so this method is using it. Just in case.
    @staticmethod
    def do_numpy_quicksort(sorting_list):
        Quicksorter.__for_numeric_list(sorting_list)
        sorting_array = numpy.asarray(sorting_list)
        sorting_array = numpy.sort(sorting_array, kind='quicksort')
        sorting_list = list(sorting_array)
        return sorting_list

    # Inner quicksort function, working with numeric array.
    @staticmethod
    def __quicksort(sorting_array: numpy.ndarray, first: int, last: int):
        if first >= last:
            return
        i = first
        j = last
        pivot = sorting_array[int((first+last)/2)]
        while i <= j:
            while sorting_array[i] < pivot:
                i += 1
            while sorting_array[j] > pivot:
                j -= 1
            if (i <= j):
                sorting_array[i], sorting_array[j] = sorting_array[j], sorting_array[i]
                i, j = i + 1, j - 1
            Quicksorter.__quicksort(sorting_array, first, j)
            Quicksorter.__quicksort(sorting_array, i, last)

    # Quicksort function for the task.
    @staticmethod
    def quicksort_list(sorting_list):
        Quicksorter.__check_for_numeric_list(sorting_list)
        sorting_array = numpy.asarray(sorting_list)
        Quicksorter.__quicksort(sorting_array, 0, len(sorting_array)-1)
        sorting_list = Quicksorter.__removeIntsFraction(list(sorting_array))
        return sorting_list

    # Not sure if it is necessary for floats to be transformed back to ints. But, well, now they are.
    @staticmethod
    def __removeIntsFraction(processing_list):
        i = 0
        while i < len(processing_list):
            element = processing_list[i]
            if element.is_integer():
                processing_list[i] = int(element)
            i += 1

        return processing_list