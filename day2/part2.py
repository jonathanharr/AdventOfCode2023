import re

def get_power_of_min_cube_setup(line, index):
    line = line[8: len(line)]
    if index > 9:
        line = line[1: len(line)]
    if index > 99:
        line = line[1: len(line)]

    matches = re.findall(r'(\d+) (\w+)', line)

    color_counts = {'red': 0, 'blue': 0, 'green': 0}
    colors_that_have_been_found = {'red': False, 'blue': False, 'green': False}
    for count, color in matches:
        if not colors_that_have_been_found[color]:
            colors_that_have_been_found[color] = True
            color_counts[color] = int(count)

        if int(count) > color_counts[color]:
            color_counts[color] = int(count)

    power = color_counts['red'] * color_counts['blue'] * color_counts['green']
    return power


def main():
    sum_of_all_min_cube_setups = 0
    file_name = 'input.txt'

    index = 1
    try:
        with open(file_name, 'r') as file:
            for line in file:
                sum_of_all_min_cube_setups += get_power_of_min_cube_setup(line, index)
                index += 1
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    print(sum_of_all_min_cube_setups)


if __name__ == "__main__":
    main()
