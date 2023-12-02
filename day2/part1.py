import re

color_max = {'red': 12,  'blue': 14, 'green': 13}


def get_id_if_possible_configuration(line, index):
    line = line[8: len(line)]
    if index > 8:
        line = line[1: len(line)]
    if index > 98:
        line = line[1: len(line)]

    matches = re.findall(r'(\d+) (\w+)', line)

    for count, color in matches:
        if int(count) > color_max[color]:
            return 0

    return index


def main():
    sum_of_ids_with_valid_cubes = 0
    file_name = 'input.txt'

    index = 1
    try:
        with open(file_name, 'r') as file:
            for line in file:
                sum_of_ids_with_valid_cubes += get_id_if_possible_configuration(line, index)
                index += 1
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    print(sum_of_ids_with_valid_cubes)


if __name__ == "__main__":
    main()
