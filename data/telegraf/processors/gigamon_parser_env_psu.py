import sys
from line_protocol_parser import parse_line
def main():
    while True:
        for line in sys.stdin:
            data = parse_line(line)
            unparsed = data["fields"]["powerSupply"].strip().replace("[", "")
            psulist = unparsed.split("] ")
            for i, psu in enumerate(psulist):
                splitpsu = psu.split()
                try:
                    newdata = data.copy()
                    newdata["tags"]["psu_id"] = i
                    newdata["tags"]["psu_name"] = splitpsu[0]
                    newdata["fields"]["psu_state"] = splitpsu[2].replace("]", "")
                    psuline = ""
                    psuline_list = []
                    psuline_list.append(f"{newdata['measurement']}")
                    for key, value in newdata['tags'].items():
                        psuline_list.append(f"{key}={value}")
                    psuline += ','.join(psuline_list)
                    psuline += " "
                    psuline_list = []
                    for key, value in newdata['fields'].items():
                        if isinstance(value, int):
                            psuline_list.append(f"{key}={value}i")
                        elif isinstance(value, str):
                            psuline_list.append(f"{key}=\"{value}\"")
                    psuline += ','.join(psuline_list)
                    psuline += f" {newdata['time']}"

                    print(psuline.strip())
                except Exception as e:
                    continue

            sys.stdout.flush()

 
if __name__ == '__main__':
    main()


