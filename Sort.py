import fun
import numpy as np
#test array
array = [42,35,87,42,91,33,78,23,87,21]

print("input:",array)
# check on input value
if (fun.Check_array(array)):
    # sort array
    fun.sort(np.array(array, float), 0, len(array) - 1)
    print(array)
    print("output: [", ','.join(str(i) for i in array),"]")
print("end")