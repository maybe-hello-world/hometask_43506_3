import unittest

from MergeSorting import MergeSorting

"""
Тестирование сортировки слиянием - на работоспособность и на проверку "от дурака"
"""
class MergeSortingTest(unittest.TestCase) :

    def test_shouldSort(self) :
        unsorted = [5,1,2,3,7,9,0,4,8,6]
        expected = [0,1,2,3,4,5,6,7,8,9]
        realArray = MergeSorting.sort(unsorted)

        self.assertEqual(expected, realArray, "Sorting algorithm doesn't work!")

    def test_shouldFailBecauseDataIsNotList(self) :
        input = "1234"
        with self.assertRaises(TypeError) :
            MergeSorting.sort(input)

    def test_shouldFailBecauseListContainsNotIntFloatType(self) :
        input = ["1234", "5678"]
        with self.assertRaises(TypeError) :
            MergeSorting.sort(input)

if __name__ == '__main__':
    unittest.main()