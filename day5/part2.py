
INPUT = []
SEED_TO_SOIL = []
SOIL_TO_FERTILIZER = []
FERTILIZER_TO_WATER = []
WATER_TO_LIGHT = []
LIGHT_TO_TEMPERATURE = []
TEMPERATURE_TO_HUMIDITY = []
HUMIDITY_TO_LOCATION = []


def set_des_sour_rang_to_list(des_sour_rang_as_list, line_to_look_for):
    index = INPUT.index(line_to_look_for)
    for i in range(index + 1, len(INPUT)):
        if INPUT[i] == '':
            break
        line = INPUT[i]
        numbers_list = [int(num) for part in line.split(' ') for num in part.split()]
        des_sour_rang_as_list.append(numbers_list)


def get_destination_from_source_using_list(destination_source_range_as_list, key_to_look_for):
    for i in range(len(destination_source_range_as_list)):
        destination_source_range = destination_source_range_as_list[i]
        destination_range_start = destination_source_range[0]
        source_range_start = destination_source_range[1]
        range_amount = destination_source_range[2]
        destination_offset = source_range_start + range_amount
        if key_to_look_for > destination_offset or key_to_look_for < source_range_start:
            continue

        destination_result = destination_range_start
        key_range_offset = key_to_look_for - source_range_start
        destination_result += key_range_offset
        return destination_result

    return key_to_look_for


def get_location_to_seed(seed):
    soil = get_destination_from_source_using_list(SEED_TO_SOIL, seed)
    fertilizer = get_destination_from_source_using_list(SOIL_TO_FERTILIZER, soil)
    water = get_destination_from_source_using_list(FERTILIZER_TO_WATER, fertilizer)
    light = get_destination_from_source_using_list(WATER_TO_LIGHT, water)
    temperature = get_destination_from_source_using_list(LIGHT_TO_TEMPERATURE, light)
    humidity = get_destination_from_source_using_list(TEMPERATURE_TO_HUMIDITY, temperature)
    location = get_destination_from_source_using_list(HUMIDITY_TO_LOCATION, humidity)
    return location


def main():
    global INPUT
    file_name = 'input.txt'

    try:
        with open(file_name, 'r') as file:
            file_contents = file.read()
            lines = file_contents.split('\n')
            INPUT = lines

            set_des_sour_rang_to_list(SEED_TO_SOIL, "seed-to-soil map:")
            set_des_sour_rang_to_list(SOIL_TO_FERTILIZER, "soil-to-fertilizer map:")
            set_des_sour_rang_to_list(FERTILIZER_TO_WATER, "fertilizer-to-water map:")
            set_des_sour_rang_to_list(WATER_TO_LIGHT, "water-to-light map:")
            set_des_sour_rang_to_list(LIGHT_TO_TEMPERATURE, "light-to-temperature map:")
            set_des_sour_rang_to_list(TEMPERATURE_TO_HUMIDITY, "temperature-to-humidity map:")
            set_des_sour_rang_to_list(HUMIDITY_TO_LOCATION, "humidity-to-location map:")
    except FileNotFoundError:
        print(f"File not found: {file_name}")
        return

    lowest_location_number = 100000000000
    numbers = [int(num) for num in INPUT[0].split()[1:]]

    pairs = list(zip(numbers[::2], numbers[1::2]))

    for i in range(len(pairs)):
        seed_start = pairs[i][0]
        seed_end = seed_start + pairs[i][1]
        for seed in range(seed_start, seed_end):
            if seed % 100000 == 0:
                print(f"Now on seed={seed}, to: {seed_end} currently lowest: {lowest_location_number}")

            loc = get_location_to_seed(seed)
            if loc < lowest_location_number:
                lowest_location_number = loc

        print(f"lowest_location_number={lowest_location_number}, from seed pair {pairs[i]}")
    print(f"lowest_location_number={lowest_location_number}")


if __name__ == "__main__":
    main()