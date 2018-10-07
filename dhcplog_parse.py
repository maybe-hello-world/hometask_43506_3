#!/usr/bin/python3

from re import compile, X
from os.path import basename, isfile
from sys import argv
from json import dumps

# Accepts 2 optional args:
#     log file
#     number of an action

ID      = '31'
INFILE  = 'DhcpSrvLog-Thu.log'
OUTFILE = 'result.txt'
PATTERN = """^(?P<id>          @id@              ),
              (?P<date>        \d{2}/\d{2}/\d{2} ),
              (?P<time>        \d{2}:\d{2}:\d{2} ),
              (?P<description> [^,]+             ),
              (?P<ip>          [\d.]+            ),
              (?P<hostname>    [^,]+             ),"""

def usage():
    filename = basename(__file__)
    print(f'Usage: python {filename} <Log file name> <ID>')

def main(filename: str, id: str) -> dict:
    regexp = compile(PATTERN.replace("@id@", id), X)
    count = 0
    computers = set()
    with open(filename) as logs:
        for line in logs:
            match = regexp.match(line)
            if match:
                computers.add(match.group('ip'))
                count += 1

    return {
        "id": id,
        "count": count,
        "computers": sorted(list(computers)),
    }


def write_file(filename, entrances):
    with open(filename, "w") as f:
        print(dumps(entrances, indent=4), file=f)

if __name__ == '__main__':
    # Could use argparser, but I don't see any reasons to complicate
    # The second argument is an ID
    if len(argv) < 3:
        usage()
        print("Using default parameters for ungiven arguments")
        id = ID
    else:
        id = argv[2]

    # The first argument is the log file
    if len(argv) < 2:
        filename = INFILE
    else:
        filename = argv[1]

    if len(id) == 1:
        id = f'0{id}'

    if not isfile(filename):
        usage()
        print(f'{filename} is not an existing file')
        exit(1)

    entrances = main(filename, id)
    write_file(OUTFILE, entrances)
    print('Done!')
