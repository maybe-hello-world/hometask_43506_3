ID      = '31'
INFILE  = 'DhcpSrvLog-Thu.log'
OUTFILE = 'result.txt'

count = 0
computers = set()

with open(INFILE) as logs:
    for i in range(34):
        logs.readline() #начинаем считывать с 35й строки
    for line in logs:
        if line[:2] == ID:
            count +=1
            x = line.split(',')
            #print(x)
            computers.add(x[4])

computers = sorted(list(computers))

with open(OUTFILE, "w") as f:
    print(count, file = f)
    for computer in computers:
        print(computer, file = f)

print("Done!")
