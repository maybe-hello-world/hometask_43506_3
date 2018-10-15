import unittest
from mergeSort import merge_sort


class TestBasicFunction(unittest.TestCase):
    def testEvenArray(self):
        """
        Test case on even list length.

        :return: Is it work correctly on even lists?
        """
        self.assertEqual(merge_sort([1, 3, 2, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def testOddArray(self):
        """
        Test case on odd list length.

        :return: Is it work correctly on odd lists?
        """
        self.assertEqual(merge_sort([2, 1, 4, 5, 3]), [1, 2, 3, 4, 5])

    def testIntArray(self):
        """
        Test case on list of int values.

        :return: Is it work correctly on int lists?
        """
        self.assertEqual(merge_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9])

    def testFloatArray(self):
        """
        Test case on list of float values.

        :return: Is it work correctly on float lists?
        """
        self.assertEqual(merge_sort([1.5, 1.4, 1.3, 1.2, 1.1]), [1.1, 1.2, 1.3, 1.4, 1.5])

    def testStructureTypeError(self):
        """
        Test case on non-list entry value.

        :return: Is it raises value error correctly on non-list value?
        """
        with self.assertRaises(ValueError) as context:
            merge_sort('asdasdad')

        self.assertTrue('Input value should be list.' in str(context.exception))

    def testListItemTypeError(self):
        """
        Test case on list that contains NaN values.

        :return: Is it raises value error correctly on NaN value in list?
        """
        with self.assertRaises(ValueError) as context:
            merge_sort([1, 2, 3, 'ok easy', 3, 2, 5])

        self.assertTrue('List should contain only float or integer values, but NaN value found.' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
