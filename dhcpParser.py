from collections import Counter
import json

# Parse file with the structure similar to the standard dhcp server logs and save results to the file.
def log_parse(event, file_path):
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
