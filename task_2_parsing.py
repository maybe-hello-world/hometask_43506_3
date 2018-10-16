# Might not be the most rational approach for that exact task.
# It would be much quicker to just analise text in the file on the first go, then to parse file to list
# and then to work with that list, like it is made here.
# But such an approach gives some flexibility to use parser for analysing another event_ids
# or even for creation some other logic.
class Parser:
    file_path: str
    __possible_ids: [] # a list of possible event ids
    __log_dictionary: {} # a dictionary of the log's records
    __parsed_records: [] # a log from file as an array of dictionaries

    def __init__(self, file_path: str):
        assert isinstance(file_path, str), \
            'file_path should have str type'
        self.file_path = file_path
        with open(self.file_path, 'r') as file:
            self.__possible_ids = self.__get_all_possible_ids(file)
            self.__log_dictionary = self.__get_log_dictionary(file)
            self.__parsed_records = self.__parse_file(file)

    def __get_log_dictionary(self, file):
        result = {}
        for line in file:
            lower_line = line.lower()
            # Searching for the line describing log's dictionary. Since for the current task are needed id, hostname and, probably, ipaddress used only them to find it.
            if 'id' in lower_line and 'host name' in lower_line and 'ip address' in lower_line:
                keys = lower_line.split(",")
                i = 0
                for key_str in keys:
                    key = key_str.lstrip().rstrip()
                    result.update({i: key})
                    i += 1
                return result
        raise Exception('Dictionary line can not be found')



    # Method which allows to get a list of all possible ids, which are presented in the beginning of the logfile.
    def __get_all_possible_ids(self, file):
        result = []
        for line in file:
            if 'Event ID  Meaning' in line:
                break;
        for line in file:
            if line in ['\n', '\r\n']:
                return result;
            else:
                result.append(line[:3].rstrip());


    def __check_event_id(self, event_id: str):
        assert isinstance(event_id, str), \
            'event_id should have str type'
        last_id = int(self.__possible_ids[len(self.__possible_ids)-1][:2])
        assert event_id in self.__possible_ids or int(event_id) >= last_id, \
            'There is no such event_id in the log description'



    def process_event(self, event_id: str, output_path: str):
        self.__check_event_id(event_id)
        assert isinstance(output_path, str), \
            'Output path should be a str'
        event_counter = 0
        computer_lines = []
        for record in self.__parsed_records:
            if record['id'] == event_id:
                event_counter += 1
                if (record['host name'] == ''):
                    record['host name'] = 'none'
                if (record['ip address'] == ''):
                    record['ip address'] = 'none'
                computer_lines.append(str(str(event_counter) + '. Host Name: ' + record['host name'] + ', Ip Address: ' + record['ip address']) + "\n")
        with open(output_path, 'w') as file:
            writing_lines = [str('event_id: ' + event_id + "\n"),
                            str('Total amount: ' + str(event_counter) + "\n"),
                            str('List of computers:' + "\n") ]
            writing_lines.extend(computer_lines)
            file.writelines(writing_lines)


    def __parse_file(self, file):
        result = []
        for line in file:
            record_str = line.split(",")
            new_record = {}
            i = 0
            for value in record_str:
                if i < len(self.__log_dictionary):
                    new_record.update({self.__log_dictionary[i]: value})
                i += 1
            result.append(new_record)
        return result






