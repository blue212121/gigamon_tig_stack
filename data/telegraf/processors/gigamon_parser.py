import sys
from line_protocol_parser import parse_line
def main():
    while True:
        for line in sys.stdin:
            if line.startswith("gigamon_env_fans"):
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

            elif line.startswith("gigamon_env_temp"):
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

            elif line.startswith("gigamon_env_psu"):
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

            else:
                print(line.rstrip())            
            sys.stdout.flush()

 
if __name__ == '__main__':
    main()


