import fun
#test array
array = [25, 45, 37, 56, -6, -6, 48, 0, -6, 7.23, 7.23, 45, 45, 56, 8.324, 1000]

print("input:",array)
# check on input value
if (fun.Check_array(array)):
    # sort array
    print("output: [", ','.join(str(i) for i in fun.sort(array)),"]")

print("end")