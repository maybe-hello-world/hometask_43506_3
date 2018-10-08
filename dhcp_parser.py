from io import StringIO
import csv
import json

DELIMITER = ","
HEADER = "ID,Date,Time,Description,IP Address,Host Name,MAC Address,User Name, TransactionID, QResult,Probationtime, " \
                               "CorrelationID,Dhcid,VendorClass(Hex),VendorClass(ASCII),UserClass(Hex),UserClass(ASCII)," \
                               "RelayAgentInformation,DnsRegError."
ID_COLUMN_NUMBER = 0
COMPUTER_IP_COLUMN_NUMBER = 4


def log_to_csv(file_name):
    with open(file_name, "r") as src:
        data = src.read()
    return csv.reader(StringIO(data[data.find(HEADER) + len(HEADER) + 1:]), delimiter=DELIMITER)


def parse(file_name, event_id):
    reader = log_to_csv(file_name)
    data = {"Event": event_id, "Count": 0, "Computers": set()}
    for row in reader:
        if int(row[ID_COLUMN_NUMBER]) == event_id:
            data["Count"] += 1
            data["Computers"].add(row[COMPUTER_IP_COLUMN_NUMBER])
    data["Computers"] = list(data["Computers"])
    return json.dumps(data, indent=4)
