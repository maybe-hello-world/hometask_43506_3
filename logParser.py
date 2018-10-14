import json


# parse log file
def log_parse(event_id, file_name):
    users = []
    counter = 0
    with open(file_name, "r") as file:
        for line in file:
            data = line.split(",")
            if data[0] == event_id:
                counter += 1
                users.append(data[4])
    file.close()
    create_result_file({"eventId": event_id, "count": counter, "userIPs": users})


# create result json file
def create_result_file(data):
    with open('result.json', 'w') as file:
        json.dump(data, file)
    print("File result.json created")
