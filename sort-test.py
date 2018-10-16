import sort

if sort.sort([])==[]:
    print('Test 1: []->[]');
else:
    print('Empty list error')

if sort.sort([10,5,0,2,6,9,1,3,8,7,4,-1])==[-1,0,1,2,3,4,5,6,7,8,9,10]:
    print("Test 2: [10,5,0,2,6,9,1,3,8,7,4,-1] -> [-1,0,1,2,3,4,5,6,7,8,9,10]",)
else:
    print('List of int was not sorted')

if sort.sort([-1.1,1.2,-1.3,1.4,-1.5,1.6,-1.7])==[-1.7,-1.5,-1.3,-1.1,1.2,1.4,1.6]:
    print ("Test 3: [-1.1,1.2,-1.3,1.4,-1.5,1.6,-1.7]) -> [-1.7,-1.5,-1.3,-1.1,1.2,1.4,1.6]")
else:
   print('List of float was not sorted')

try:
    sort(123)
except Exception:
    print("Test 4: Ошибка передачи не-списка удачно поймана")

try:
    sort((1,2,'lol',3,4))
except Exception:
    print("Test 5: Ошибка передачи списка не численных значений удачно поймана")