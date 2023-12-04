def get_schematics(file_name):
    """TODO"""

    schematics = []
    prev_number = ""
    indexes = []
    with open(file_name) as file:
        for schem in file:
            result = []
            for i, char in enumerate(schem):
                if char == "\n":
                    continue
                if char.isdigit():
                    prev_number += char
                    indexes.append(i)
                else:
                    if prev_number:
                        for digit in prev_number:
                            result.append((digit, prev_number, "unused", indexes))
                    if char == ".":
                        result.append((char, "dote", "", []))
                    else:
                        result.append((char, "special", "", []))
                    prev_number = ""
                    indexes = []
            # handle the last number
            if prev_number:
                for digit in prev_number:
                    result.append((digit, prev_number, "unused", indexes))
            schematics.append(result)

    return schematics


def array_has_index(array, index):
    try:
        array[index]
        return True
    except IndexError:
        return False


def add_input(schema, index_to_check):
    if array_has_index(schema, index_to_check):
        h_1 = schema[index_to_check]
        if h_1[2] == "unused":
            for number in h_1[3]:
                schema[number] = ("0", "0", "USED", [])
                if len(schema) > 140:
                    print(len(schema))
                    print(schema)
                    print(index_to_check)
                    print("=====")
                    raise Exception("ERROR")
            # print(int(h_1[1]))
            return int(h_1[1])
    return 0


def get_sum(schematics):
    sum = 0
    parts = []
    for line, schema in enumerate(schematics):
        
        for index, input in enumerate(schema):
            if len(schema) > 140:
                print(len(schema))
            previous_line = None
            next_line = None
            if input[1] != "special":
                continue

            # CURRENT LINE
            print(input)
            print(line)
            part = add_input(schema, (index - 1))
            if part > 0:
                parts.append(part)
                sum += part

            part = add_input(schema, (index + 1))
            if part > 0:
                parts.append(part)
                sum += part

            # PREVIOUS LINE
            if line > 0:
                previous_line = schematics[line - 1]

                part = add_input(previous_line, (index - 1))
                if part > 0:
                    parts.append(part)
                    sum += part

                part = add_input(previous_line, index)
                if part > 0:
                    parts.append(part)
                    sum += part

                part = add_input(previous_line, (index + 1))
                if part > 0:
                    parts.append(part)
                    sum += part

            # NEXT LINE
            if array_has_index(schematics, (line + 1)):
                next_line = schematics[line + 1]

                part = add_input(next_line, (index - 1))
                if part > 0:
                    parts.append(part)
                    sum += part
                # j_1 = next_line[index - 1]
                # if j_1[2] == "unused":
                #     sum += int(j_1[1])
                #     for number in j_1[3]:
                #         next_line[number] = ("0", "0", "USED", [])

                part = add_input(next_line, index)
                if part > 0:
                    parts.append(part)
                    sum += part
                # j_2 = next_line[index]
                # if j_2[2] == "unused":
                #     sum += int(j_2[1])
                #     for number in j_2[3]:
                #         next_line[number] = ("0", "0", "USED", [])

                part = add_input(next_line, (index + 1))
                if part > 0:
                    parts.append(part)
                    sum += part
                # j_3 = next_line[index + 1]
                # if j_3[2] == "unused":
                #     sum += int(j_3[1])
                #     for number in j_3[3]:
                #         next_line[number] = ("0", "0", "USED", [])
    print(parts)
    return sum


codes = get_schematics("./3/input.txt")
print(get_sum(codes))
