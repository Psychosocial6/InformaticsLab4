import yaml

def yaml_to_csv(yaml_file, csv_file):
    with open(yaml_file, "r", encoding="utf8") as f:
        yaml_parsed = yaml.safe_load(f)
    #print(yaml_parsed)
    data_csv = {}
    for k1 in yaml_parsed:
        if isinstance(yaml_parsed[k1], list):
            data_csv[k1] = yaml_parsed[k1]

        elif isinstance(yaml_parsed[k1], str):
            if k1 not in data_csv: #строка
                data_csv[k1] = [yaml_parsed[k1]]
            else:
                data_csv[k1].append(yaml_parsed[k1])

        elif isinstance(yaml_parsed[k1], dict): #словарь
            for k2 in yaml_parsed[k1]:
                if k1 not in data_csv:
                    data_csv[k1] = [k2]
                else:
                    data_csv[k1].append(k2)
                for k3 in yaml_parsed[k1][k2]:
                    if k3 not in data_csv:
                        data_csv[k3] = [yaml_parsed[k1][k2][k3]]
                    else:
                        data_csv[k3].append(yaml_parsed[k1][k2][k3])
    #print(data_csv)
    with open(csv_file, "w", encoding="utf8") as f:
        for key in data_csv:
            result_string = key + ";"
            for i in data_csv[key]:
                result_string += str(i) + ";"
            result_string = result_string[:-1] + "\n"
            f.write(result_string)

yaml_to_csv("tuesdaySchedule.yml", "tuesdaySchedule.csv")
yaml_to_csv("thursdaySchedule.yml", "thursdaySchedule.csv")
