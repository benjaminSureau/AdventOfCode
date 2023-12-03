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
            return int(h_1[1])
    return 0


def get_sum(schematics):
    sum = 0
    for line, schema in enumerate(schematics):
        for index, input in enumerate(schema):
            if input[1] != "special":
                continue

            print(input)
            # CURRENT LINE
            sum += add_input(schema, (index - 1))
            # h_1 = schema[index - 1]
            # if h_1[2] == "unused":
            #     sum += int(h_1[1])
            #     for number in h_1[3]:
            #         schema[number] = ("0", "0", "USED", [])

            sum += add_input(schema, (index + 1))
            # h_2 = schema[index + 1]
            # if h_2[2] == "unused":
            #     sum += int(h_2[1])
            #     for number in h_2[3]:
            #         schema[number] = ("0", "0", "USED", [])

            # PREVIOUS LINE
            if line > 0:
                previous_line = schematics[line - 1]

                sum += add_input(previous_line, (index - 1))
                # i_1 = previous_line[index - 1]
                # if i_1[2] == "unused":
                #     sum += int(i_1[1])
                #     for number in i_1[3]:
                #         previous_line[number] = ("0", "0", "USED", [])

                sum += add_input(previous_line, index)
                # i_2 = previous_line[index]
                # if i_2[2] == "unused":
                #     sum += int(i_2[1])
                #     for number in i_2[3]:
                #         previous_line[number] = ("0", "0", "USED", [])

                sum += add_input(previous_line, (index + 1))
                # i_3 = previous_line[index + 1]
                # if i_3[2] == "unused":
                #     sum += int(i_3[1])
                #     for number in i_3[3]:
                #         previous_line[number] = ("0", "0", "USED", [])

            # NEXT LINE
            if array_has_index(schematics, (line + 1)):
                next_line = schematics[line + 1]

                sum += add_input(next_line, (index - 1))
                # j_1 = next_line[index - 1]
                # if j_1[2] == "unused":
                #     sum += int(j_1[1])
                #     for number in j_1[3]:
                #         next_line[number] = ("0", "0", "USED", [])

                sum += add_input(next_line, index)
                # j_2 = next_line[index]
                # if j_2[2] == "unused":
                #     sum += int(j_2[1])
                #     for number in j_2[3]:
                #         next_line[number] = ("0", "0", "USED", [])

                sum += add_input(next_line, (index + 1))
                # j_3 = next_line[index + 1]
                # if j_3[2] == "unused":
                #     sum += int(j_3[1])
                #     for number in j_3[3]:
                #         next_line[number] = ("0", "0", "USED", [])
    return sum


codes = get_schematics("./3/input.txt")
print(get_sum(codes))
