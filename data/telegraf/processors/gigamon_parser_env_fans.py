import sys
from line_protocol_parser import parse_line
def main():
    while True:
        for line in sys.stdin:
            data = parse_line(line)
            unparsed = data["fields"]["fans"].strip().replace("[", "")
            rpmlist = unparsed.split("] ")
            for i, rpm in enumerate(rpmlist):
                splitrpm = rpm.split()
                for part in splitrpm:
                    if part.isdigit():
                        try:
                            intrpm = int(part)
                            newdata = data.copy()
                            newdata["tags"]["fan_id"] = i
                            newdata["fields"]["fan_rpm"] = intrpm
                            fanline = ""
                            fanline_list = []
                            fanline_list.append(f"{newdata['measurement']}")
                            for key, value in newdata['tags'].items():
                                fanline_list.append(f"{key}={value}")
                            fanline += ','.join(fanline_list)
                            fanline += " "
                            fanline_list = []
                            for key, value in newdata['fields'].items():
                                if isinstance(value, int):
                                    fanline_list.append(f"{key}={value}i")
                                elif isinstance(value, str):
                                    fanline_list.append(f"{key}=\"{value}\"")
                            fanline += ','.join(fanline_list)
                            fanline += f" {newdata['time']}"
 
                            print(fanline.strip())
                        except Exception as e:
                            continue

            sys.stdout.flush()

 
if __name__ == '__main__':
    main()


