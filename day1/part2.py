word_to_number = {
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
    numbers = []
    string_formations = get_string_formations(input_string)
    for combination in string_formations:
        if combination in word_to_number and combination not in numbers:
            numbers.append(combination)

    return numbers


def get_string_formations(input_string):
    starting_string_formations = []

    for i in range(len(input_string)):
        string_formation = input_string[i]
        starting_string_formations.append(string_formation)

        for y in range(len(starting_string_formations)):
            if i != y:
                starting_string_formations[y] += input_string[i]

    all_formations = []
    for i in range(len(starting_string_formations)):
        all_formations.append(starting_string_formations[i])
        for y in range(len(starting_string_formations[i])):

            substring_input = input_string[i:len(input_string) - y - 1]

            if substring_input == "" or len(substring_input) < 2:
                break
            all_formations.append(substring_input)

    return all_formations


def get_calibration_values(input_string):
    numbers_as_words = get_numbers(input_string)
    digits_by_index = {}
    for i in range(len(numbers_as_words)):
        index_of_word = input_string.index(numbers_as_words[i])
        digits_by_index[index_of_word] = word_to_number[numbers_as_words[i]]

        remainder_of_string = input_string[index_of_word + len(numbers_as_words[i]) - 1:]
        while remainder_of_string.__contains__(numbers_as_words[i]):
            index_of_word = remainder_of_string.index(numbers_as_words[i]) + index_of_word + len(numbers_as_words[i]) - 1
            digits_by_index[index_of_word] = word_to_number[numbers_as_words[i]]
            remainder_of_string = input_string[index_of_word + len(numbers_as_words[i]) - 1:]

    for i in range(len(input_string)):
        if input_string[i].isdigit():
            digits_by_index[i] = int(input_string[i])

    first_digit = digits_by_index[min(digits_by_index.keys())]
    last_digit = digits_by_index[max(digits_by_index.keys())]

    combined_number = first_digit * 10 + last_digit
    return combined_number


def main():
    sum_of_calibration_values = 0
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        for line in file:
            sum_of_calibration_values += get_calibration_values(line)

    print(f"Sum of calibration values: {sum_of_calibration_values}")


if __name__ == "__main__":
    main()
