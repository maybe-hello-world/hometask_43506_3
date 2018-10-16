import json


ID='32'
file_name='DhcpSrvLog-Thu.log'
file_out='output.txt'
with open(file_name, "r") as file:
    counter=0
    users=[]
    for line in file:
        Line=line.split(',')
        if (Line[0]==ID):
            counter=counter+1
            users.append(Line[4])
    DictResult = {"ID": ID, "Count": counter, "Users": users}
with open(file_out, 'w')as outfile:
    outfile.write(json.dumps(DictResult, indent=4))
