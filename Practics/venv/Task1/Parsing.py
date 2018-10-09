import json

"""
Парсинг файла DhcpSrvLog-Thu.log ( Microsoft DHCP Service Activity Log )
"""
class Parsing :

    @staticmethod
    def parse(eventId: str = "11", filename: str = "DhcpSrvLog-Thu.log") -> dict:
        count = 0
        computers = set()

        with open(filename, "r") as file :
            for line in file:
                values = line.split(",")
                if values[0] == eventId:
                    ipAddress = values[4]
                    computers.add(ipAddress)
                    count += 1

        return {
            "ID": eventId,
            "EventCount": count,
            "Computers": list(computers)
        }

    @staticmethod
    def printJsonParseResult(eventId: str = "11", filename: str = "DhcpSrvLog-Thu.log") -> None :
        result = Parsing.parse(eventId, filename)
        with open('result.json', 'w') as outfile:
            json.dump( obj =  result, fp = outfile, indent = 4 )


Parsing.printJsonParseResult()