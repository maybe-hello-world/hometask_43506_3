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

def sort(array):
    """
    Sort array with Quicksort
    :param array: Array
    :return: sorted Array
    """
    NumpyArray=np.array(array, float)
    if (len(NumpyArray)<2):
        return NumpyArray
    else:
        opp=NumpyArray[0]
        lower = np.array([], float)  # values<opp
        upper = np.array([], float) # values>opp
        equal = np.array([], float)  # values=opp
        for x in NumpyArray:
            if (x < opp):
                lower=np.append(lower,x)
            if (x > opp):
                upper=np.append(upper, x)
            if (x == opp):
                equal= np.append(equal, x)
        return  np.concatenate((lower,equal,upper))