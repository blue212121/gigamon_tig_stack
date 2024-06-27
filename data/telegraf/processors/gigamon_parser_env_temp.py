import sys
from line_protocol_parser import parse_line
def main():
    while True:
        for line in sys.stdin:
            data = parse_line(line)
            unparsed = data["fields"]["temperatureSensors"].strip().replace("[", "")
            templist = unparsed.split("] ")
            for i, temp in enumerate(templist):
                splittemp = temp.split()
                try:
                    inttemp = int(splittemp[3])
                    newdata = data.copy()
                    newdata["tags"]["location_id"] = i
                    newdata["tags"]["location"] = f"{splittemp[0]}\ {splittemp[1]}"
                    newdata["fields"]["temp_c"] = inttemp
                    templine = ""
                    templine_list = []
                    templine_list.append(f"{newdata['measurement']}")
                    for key, value in newdata['tags'].items():
                        templine_list.append(f"{key}={value}")
                    templine += ','.join(templine_list)
                    templine += " "
                    templine_list = []
                    for key, value in newdata['fields'].items():
                        if isinstance(value, int):
                            templine_list.append(f"{key}={value}i")
                        elif isinstance(value, str):
                            templine_list.append(f"{key}=\"{value}\"")
                    templine += ','.join(templine_list)
                    templine += f" {newdata['time']}"

                    print(templine.strip())
                except Exception as e:
                    continue

            sys.stdout.flush()

 
if __name__ == '__main__':
    main()


