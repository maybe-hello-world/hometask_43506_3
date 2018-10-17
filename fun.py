import numpy as np

def Check_array(arr):
    """
    Check array values for type and value
    :param arr:Array
    :return: True if all correct, else False and print Error
    """
    for i in arr:
        try:
            float(i)
        except ValueError:
            print(ValueError("Values us not correct"))
            return False
        except TypeError:
            print(TypeError("Type is not correct"))
            return False
    return True

def swap(array, firstnum, secondnum):
    """
    :param array: Array
    :param firstnum: Int position of first value 
    :param secondnum: Int position of second value 
    :return: nothing
    """
    array[firstnum],array[secondnum]=array[secondnum],array[firstnum]



def sort(array, lower, upper):
    """
    Sort array with Quicksort
    :param array: Array
    :return: nothing
    """
    if (lower<upper):
        opp=array[lower]
        i=lower
        for x in range(lower+1,upper+1):
            if (array[x] < opp):
                array[i+1], array[x] = array[x], array[i+1]
                i=i+1
        swap(array,lower,i)
        if (i-1>lower):
            sort(array,lower,i-1)
        if (i+1<upper):
            sort(array,i+1,upper)

