import re


def has_symbol_in_neighbor_line(line, first_index, last_index):
    first_index = 0 if first_index == 0 else first_index - 1
    last_index = len(line) - 1 if last_index == len(line) - 1 else last_index + 2
    neighbor = line[first_index: last_index]
    return bool(re.search(r'[^.a-zA-Z0-9]', neighbor))


def return_value_if_adjacent_to_symbol(lines, first_index, last_index, i, part_number):
    if first_index != 0:
        left_symbol = lines[i][first_index - 1]
        if left_symbol != '.':
            return int(part_number)

    if last_index != len(lines[i]) - 1:
        right_symbol = lines[i][last_index + 1]
        if right_symbol != '.':
            return int(part_number)

    prev_line = "" if i == 0 else lines[i - 1]
    next_line = "" if i == len(lines) - 1 else lines[i + 1]

    has_symbol_in_neighbor = has_symbol_in_neighbor_line(prev_line, first_index, last_index) or \
                             has_symbol_in_neighbor_line(next_line, first_index, last_index)

    if has_symbol_in_neighbor:
        return int(part_number)
    return 0


def get_sum_of_row(lines, line, i):
    number_parts_start_end_index_pairs = [(match.start(), match.end() - 1) for match in re.finditer(r'\d+', line)]

    sum_of_parts = 0
    for start_index_and_end_index_pair in number_parts_start_end_index_pairs:
        first_index = start_index_and_end_index_pair[0]
        last_index = start_index_and_end_index_pair[1]
        part_number = line[first_index: last_index + 1]
        return_sum = return_value_if_adjacent_to_symbol(lines, first_index, last_index, i, part_number)
        sum_of_parts += return_sum

    return sum_of_parts


def main():
    sum_of_calibration_values = 0
    file_name = 'input.txt'

    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()
            lines = file_contents.split('\n')
            for i, line in enumerate(lines):
                sum_of_calibration_values += get_sum_of_row(lines, line, i)
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    print(sum_of_calibration_values)


if __name__ == "__main__":
    main()
