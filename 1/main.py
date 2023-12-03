import re


def calculate_calibration(file_path):
    sum = 0
    with open(file_path, "r") as file:
        for line in file:
            numbers = re.findall("\d", line)  # trouve tous les chiffres
            calibration_value = int(
                numbers[0] + numbers[-1]
            )  # combine first and last digit
            sum += calibration_value  # add to sum
    return sum


# print(calculate_calibration("./1/input.txt"))


# Mapping of words to numbers
word_to_num = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
pattern = r"(?=((\d)|one|two|three|four|five|six|seven|eight|nine))"


def get_number(word):
    # Check if word is a number
    if word.isdigit():
        return word
    # Convert word to number
    if word in word_to_num:
        return str(word_to_num[word])
    return None


def calculate_calibration_2(file_path):
    total = 0
    cpt = 0
    with open(file_path, "r") as file:
        for line in file:
            words = re.findall(pattern, line)  # Finds all words and numbers
            words = [ (w[0][0] if w[0].isdigit() else get_number(w[0])) for w in words ]
            words = list(filter(None, words))  # Remove None values

            if len(words) > 0:
                calibration_value = int(
                    words[0] + words[-1]
                )  # Combine first and last digit
                print(calibration_value)
                total += calibration_value  # Add to total
                cpt += 1
    print(cpt)
    return total


print(calculate_calibration_2("./1/input_2.txt"))
