from io import StringIO
import json
import csv


THEAD = "ID,Date,Time,Description,IP Address,Host Name,MAC Address,User Name, TransactionID, QResult,Probationtime, " \
        "CorrelationID,Dhcid,VendorClass(Hex),VendorClass(ASCII),UserClass(Hex),UserClass(ASCII)," \
        "RelayAgentInformation,DnsRegError."

file = 'DhcpSrvLog-Thu.log'

def readlog(file):
    with open(file, "r") as log:
        data = log.read()
    return csv.reader(StringIO(data[data.find(THEAD) + len(THEAD) + 1:]), delimiter=',')


def parse(file, event):
    reader = readlog(file)
    result = {"event": event, "quantity": 0, "computers": set()}
    for row in reader:
        if int(row[0]) == event: # Колонка в логе с событиями
            result["quantity"] += 1
            result["computers"].add(row[4]) # Колонка в логе с компьютерами
    result["computers"] = list(result["computers"])
    return json.dumps(result, indent=3)


with open('data/result.json', 'w') as res:
    string = parse(file, 11)
    res.write(string)
