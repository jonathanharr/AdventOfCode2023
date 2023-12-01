def get_calibration_values(input_string):
    digits = [char for char in input_string if char.isdigit()]

    if digits:
        return int(digits[0] + digits[-1])
    else:
        return 0


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

    print(sum_of_calibration_values)


if __name__ == "__main__":
    main()