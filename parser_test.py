from sys import argv
import dhcp_parser

if __name__ == '__main__':
    event_number = -1
    file_name = ""
    try:
        file_name = argv[1]
        event_number = int(argv[2])
    except (IndexError, TypeError, ValueError):
        print("Incorrect input args")
        exit(1)
    print(dhcp_parser.parse(file_name, event_number))
