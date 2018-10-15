from collections import Counter
import json


def log_parse(event, file_path):
    """
    Parse file with the structure similar to the standard
    dhcp server logs and save results to the json file,
    named dhcpDump.json in the same folder.

    Keyword arguments:
    :param event: Numeric ID of event, from the dhcp table with events meaning.
    :param file_path: String with a path to the file, containing dhcp logs.
    """
    with open(file_path, 'r') as file:
        arrIds = []
        for line in file:
            data = line.split(',')
            if data[0] == str(event):
                arrIds.append(data[4])

        file.close()
        cnt = Counter(arrIds)

        sum = 0

        res = {}
        res['records'] = []

        for c in cnt:
            sum += cnt[c]

            record = {}
            record['ip'] = c
            record['asks_count'] = cnt[c]

            res['records'].append(record)

        res['total_records'] = sum

        with open('dhcpDump.json', 'w') as file:
            json.dump(res, file)
        file.close()
        print('Dump created.')


log_parse(11, 'DhcpSrvLog-Thu.log')
