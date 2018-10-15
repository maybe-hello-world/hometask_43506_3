import json
from sys import argv

def get_data(path: str = 'DhcpSrvLog-Thu.log') :
    """Чтение из файла и построчная запись в lines"""
    f = open(path)
    lines = [line.strip() for line in f]
    f.close()
    data = {}
    k=0
    for i in lines:
        user = i.split(',', -1)
        data[k] = user
        k += 1
    return data;


if __name__ == '__main__':
    data = get_data()
    """По умолчанию считаем для пользователя id=32"""
    if len(argv) == 1 :
        event_id=32
        print("Default user's id was set to 32")
    else:
        try:
            event_id=int(argv[1])
        except ValueError:
            print("Use int argument to set user's id. Default id is 32 for now")
            event_id=32

    users = set()
    counter = 0
    for i in range(1, len(data)):
        try:
            if int(data[i][0])==event_id:
                counter+=1
                users.add(data[i][4])
        except ValueError:
            pass
    json_file = {'Event_id' : event_id, 'Counter':counter, 'Users': list(users)}
    with open('Event_{}_result.json'.format(event_id), 'w') as outfile:
        json.dump(json_file, outfile, indent=4, ensure_ascii=False)