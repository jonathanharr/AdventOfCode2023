import re


def find_nearby_numbers(numbers_as_pairs_by_start_end_index, x):
    nearby_positions = set()
    neighbor_numbers_horizontally = [x - 1, x, x + 1]
    for (start, end), row_value in numbers_as_pairs_by_start_end_index:
        for i in range(start, end + 1):
            if i in neighbor_numbers_horizontally:
                nearby_positions.add(((start, end), row_value))

    return nearby_positions


def get_sum_of_geared_part(lines, numbers_as_pairs_by_start_end_index, gear):
    nearby_numbers = find_nearby_numbers(numbers_as_pairs_by_start_end_index, gear)

    if len(nearby_numbers) == 2:
        prev_number = -1
        for position in nearby_numbers:
            x_start = position[0][0]
            x_end = position[0][1]
            y = position[1]

            number = int(lines[y][x_start: x_end + 1])
            if prev_number == -1:
                prev_number = number
            else:
                return prev_number * number

    return 0


def get_sum_of_geared_row(lines, line, i, gear_positions):
    sum_of_geared_row = 0
    prev_line = lines[i - 1]
    next_line = lines[i + 1]

    number_parts_start_end_index_pairs = [(match.start(), match.end() - 1) for match in re.finditer(r'\d+', line)]
    number_parts_start_end_index_pairs_prev = [(match.start(), match.end() - 1) for match in re.finditer(r'\d+', prev_line)]
    number_parts_start_end_index_pairs_next = [(match.start(), match.end() - 1) for match in re.finditer(r'\d+', next_line)]

    combined_list = []
    for pairs in [number_parts_start_end_index_pairs_prev]:
        combined_list.extend([(pair, i-1) for pair in pairs])

    for pairs in [number_parts_start_end_index_pairs]:
        combined_list.extend([(pair, i) for pair in pairs])

    for pairs in [number_parts_start_end_index_pairs_next]:
        combined_list.extend([(pair, i+1) for pair in pairs])

    for gear in gear_positions:
        sum_of_geared_row += get_sum_of_geared_part(lines, combined_list, gear)

    return sum_of_geared_row


def get_gear_sum_of_row(lines, line, i):
    gear_positions = [match.start() for match in re.finditer(r'\*', line)]
    sum_of_row = 0
    if gear_positions:
        sum_of_row += get_sum_of_geared_row(lines, line, i, gear_positions)

    return sum_of_row


def main():
    sum_of_all_gear_ratios = 0
    file_name = 'input.txt'

    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()

            lines = file_contents.split('\n')
            for i, line in enumerate(lines):
                sum_of_all_gear_ratios += get_gear_sum_of_row(lines, line, i)
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    print(f"Sum of all of the gear ratios: {sum_of_all_gear_ratios}")


if __name__ == "__main__":
    main()
