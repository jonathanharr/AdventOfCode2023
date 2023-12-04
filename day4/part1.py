import re


def get_sum_of_row(line):
    pattern = re.compile(r'Card\s+(\d+): (.+)')
    match = pattern.match(line)
    card_number, numbers = match.groups()

    numbers_lists = [list(map(int, part.split())) for part in numbers.split('|')]
    points_from_row = 0
    for i in range(len(numbers_lists[1])):
        if int(numbers_lists[1][i]) in numbers_lists[0]:
            if points_from_row == 0:
                points_from_row += 1
            else:
                points_from_row += points_from_row

    return points_from_row


def main():
    sum_of_calibration_values = 0
    file_name = 'input.txt'

    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()
            lines = file_contents.split('\n')
            for i, line in enumerate(lines):
                sum_of_calibration_values += get_sum_of_row(line)
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    print(sum_of_calibration_values)


if __name__ == "__main__":
    main()
