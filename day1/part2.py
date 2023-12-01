WORD_TO_NUMBER = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def get_numbers(input_string):
    numbers = set()
    string_formations = get_string_formations(input_string)

    for combination in string_formations:
        if combination in WORD_TO_NUMBER:
            numbers.add(combination)

    return list(numbers)


def get_string_formations(input_string):
    formations = list()

    for i, formation in enumerate(input_string):
        for j in range(len(input_string[i:])):
            substring_input = input_string[i:len(input_string) - j - 1]
            if len(substring_input) < 2:
                break
            formations.append(substring_input)

    return formations


def get_calibration_values(input_string):
    numbers_as_words = get_numbers(input_string)
    digits_by_index = {}

    for word in numbers_as_words:
        index = input_string.index(word)
        digits_by_index[index] = WORD_TO_NUMBER[word]

        remainder_of_string = input_string[index + len(word) - 1:]

        while word in remainder_of_string:
            index = remainder_of_string.index(word) + index + len(word) - 1
            digits_by_index[index] = WORD_TO_NUMBER[word]
            remainder_of_string = input_string[index + len(word) - 1:]

    for i, char in enumerate(input_string):
        if char.isdigit():
            digits_by_index[i] = int(char)

    first_digit = digits_by_index[min(digits_by_index.keys())]
    last_digit = digits_by_index[max(digits_by_index.keys())]

    combined_number = first_digit * 10 + last_digit
    return combined_number


def main():
    sum_of_calibration_values = 0
    file_name = 'input.txt'

    try:
        with open(file_name, 'r') as file:
            for line in file:
                sum_of_calibration_values += get_calibration_values(line)
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    print(f"Sum of calibration values: {sum_of_calibration_values}")


if __name__ == "__main__":
    main()
