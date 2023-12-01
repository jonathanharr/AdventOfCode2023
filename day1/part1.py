def get_calibration_values(input_string):
    first_digit_found = False
    first_digit = 0
    last_digit = 0
    for i in range(len(input_string)):
        if (input_string[i].isdigit()) and (first_digit_found is False):
            first_digit = input_string[i]

            first_digit_found = True

        if (input_string[i].isdigit()) and (first_digit_found is True):
            last_digit = input_string[i]

    total = int(first_digit + last_digit)
    return total


def main():
    sum_of_calibration_values = 0
    file_name = 'input.txt'
    with open(file_name, 'r') as file:
        for line in file:
            sum_of_calibration_values += get_calibration_values(line)

    print(sum_of_calibration_values)


if __name__ == "__main__":
    main()
