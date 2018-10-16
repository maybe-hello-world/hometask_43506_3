import json
from sys import argv

def get_data(path: str = 'DhcpSrvLog-Thu.log'):
    """
    Чтение из файла и построчная запись в lines
    Каждая line парсится на эелменты, разделенные запятой
    Возвразается словарь списков с элементами-значениями из исходного logfile
    :param path:
    :return:
    """

    with open(path, 'r') as f:
        lines = [line.strip() for line in f]
    data = {}
    for index,item in enumerate(lines):
        user = item.split(',', -1)
        data[index] = user
    return data;


"""
Если запущено без аргументов или аргумент не может быть прочитан как индекс - ищется 32 эвент
Иначе используется int-аргумент, ищется по нему
Функция интеративно проходит по словарю, сравнивая первое знаение в списке с event_id, в случае соответствия
в set(для отсутствия повторов) делается соответствующая запись
На основе set'a пишется требуемый json
"""


if __name__ == '__main__':
    data = get_data()
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