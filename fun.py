#check input values
def Check_array(arr):
    for i in arr:
        try:
            float(i)
        except BaseException:
            return False
    return True

#sort array with QuickSort
def sort(array):
    if (len(array)<2):
        return array
    else:
        opp=array[0]
        lower = []  # values<opp
        upper = []  # values>opp
        equal = []  # values=opp
        for x in array:
            if (x < opp):
                lower.append(x)
            if (x > opp):
                upper.append(x)
            if (x == opp):
                equal.append(x)
        return sort(lower) + equal + sort(upper)